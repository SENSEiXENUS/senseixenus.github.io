--------------

### CTF: PATRIOTCTF

--------------

![image](https://github.com/user-attachments/assets/ba12119a-dda7-4411-9c7e-f30e71a1bae6)

--------------

- WEB
  - Giraffe-notes
  - Impersonate
- Crypto
  - Bigger is Better

----------------

### WEB

-----------------

### Giraffe-notes

![image](https://github.com/user-attachments/assets/5c8b0a94-9240-4e01-8ba9-bc00be6f27cb)

- The web app allows only ip `localhost` and `127.0.0.1`

      $allowed_ip = ['localhost', '127.0.0.1'];

- The web sets variable `allowed` to `True` only if the header `X-FORWARDED-FOR` is set to one of the allowed ips.We can only read the flag if variable `allowed` is set to `True`.
  
      if (isset($_SERVER['HTTP_X_FORWARDED_FOR']) && in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $allowed_ip)) {
          $allowed = true;
      } else {
          $allowed = false;
      }

### Exploitation

- I set header `X-FORWARDED-FOR` to `127.0.0.1` with curl and grepped for `CACI`.

![image](https://github.com/user-attachments/assets/2252e997-f009-48e5-84f1-189d18c1dfcb)

- Flag-:```CACI{1_lik3_g1raff3s_4_l0t}```


-----------------

### Impersonate

![image](https://github.com/user-attachments/assets/01003049-3c72-408b-ad2d-e7620ef2bb49)

### Source Code review

- The app is a flask web app which is a python web framework.The app uses the `datetime.datetime.now()` to grab the current date which is when the server got booted.Then,it converts the date into string using function `strftime()` and format `%Y%m%d%H%M%S`.Lastly, it hashes it with string `secret_key_` and store the result as the flask app session key.

      server_start_time = datetime.now()
      server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')
      secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
      app.secret_key = secure_key

- An important route required for exploitation is route `/admin` which grabs the session and check `is_admin` is set to `True` and `username` is set to `administrator`. If these conditions are
fulfilled,we get flag and if it appears otherwise.We get a 401 error.

      if session.get('is_admin') and uuid.uuid5(secret, 'administrator') and session.get('username') == 'administrator':
              return flag
          else:
              abort(401)
- Lastly, the `status` route presents the uptime and current_time.The current time is the present time, while the `uptime` is the `currenttime` - `server_start_time` which is then formatted.There is a certain twist not specified in the code, the server gets rebooted every 5 mins.

          current_time = datetime.now()
          uptime = current_time - server_start_time
          formatted_uptime = str(uptime).split('.')[0]

-------------------

### Exploitation

- I visited the status page to get the `year|month|date|hour` since the hour remains static but subject to change as time moves.Then,I created a wordlist generator that adds the minutes and seconds.We need only 4 figures which will between be range `0000-9999`.Based on the status below,the static part of the `secret_key` will be `secret_key_2024092200`.

 ![image](https://github.com/user-attachments/assets/6d0b86ff-658a-4e62-bf4a-d180a3078ef5)

- Creating a wordlist with my [wordlist script](https://github.com/SENSEiXENUS/senseixenus.github.io/blob/main/posts/ctf/patriotctf/script/Impersonate/wordlist.py)

![image](https://github.com/user-attachments/assets/e0b1b189-9456-4c9c-817a-3c98d0401779)

- I wrote another [script](https://github.com/SENSEiXENUS/senseixenus.github.io/blob/main/posts/ctf/patriotctf/script/Impersonate/exploit.py) to generate the cookie.The script requires binary `flask-unsign` to bruteforce and sign cookies.

![image](https://github.com/user-attachments/assets/c8249c2f-0355-4d91-8f9f-f73e636567ed)

- Flag with curl
```bash
❯ curl http://chal.competitivecyber.club:9999/admin -H "Cookie: session=eyJpc19hZG1pbiI6dHJ1ZSwidWlkIjoiODMwYjliZTktODUyYy01ZjU3LWIzMDYtNzEyODY3YjJkYTE5IiwidXNlcm5hbWUiOiJhZG1pbmlzdHJhdG9yIn0.Zu9jzw.LxIT56wJkC5TbhcVb2E608vHwIw"
PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}
```
Flag-:```PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}```

--------------------------

### CRYPTO

--------------------------

### BIGGER IS BETTER

![image](https://github.com/user-attachments/assets/b36c7641-7b2d-49b2-be57-277a70743c71)

-------------------------

- This challenge is based on RSA cryptography and vulnerable to the `wiener` attack which is often used when a small private key (d) is used often leading to a very large public exponent `e`, sometimes as big as the modulus (n).

- The calculation is extreme and complex, there is a python module to attack the numbers.

Download to the script's directory with curl-:```curl -O https://raw.githubusercontent.com/orisano/owiener/master/owiener.py```

- Script

      #! /usr/bin/env python3
      import owiener
      from Crypto.Util.number import *
      
      n = 0xa0d9f425fe1246c25b8c3708b9f6d7747dd5b5e7f79719831c5cbe19fb7bab66ed62719b3fc6090120d2cfe1410583190cd650c32a4151550732b0fc97130e5f02aa26cb829600b6ab452b5b11373ec69d4eaae6c392d92da8bcbea85344af9d4699e36fdca075d33f58049fd0a9f6919f3003512a261a00985dc3d9843a822974df30b81732a91ce706c44bde5ff48491a45a5fa8d5d73bba5022af803ab7bd85250e71fc0254fcf078d21eaa5d38724014a85f679e8a7a1aad6ed22602465f90e6dd8ef95df287628832850af7e3628ad09ff90a6dbdf7a0e6d74f508d2a6235d4eae5a828ac95558bbdf72f39af5641dfe3edb0cdaab362805d926106e2af
      e = 0x5af5dbe4af4005564908a094e0eabb0a921b7482483a753e2a4d560700cb2b2dc9399b608334e05140f54d90fcbef70cec097e3f75395d0c4799d9ec3e670aca41da0892a7b3d038acb7a518be1ced8d5224354ce39e465450c12be653639a8215afb1ba70b1f8f71fc1a0549853998e2337604fca7edac67dd1e7ddeb897308ebf26ade781710e6a2fe4c533a584566ea42068d0452c1b1ecef00a781b6d31fbab893de0c9e46fce69c71cefad3119e8ceebdab25726a96aaf02a7c4a6a38d2f75f413f89064fef14fbd5762599ca8eb3737122374c5e34a7422ea1b3d7c43a110d3209e1c5e23e4eece9e964da2c447c9e5e1c8a6038dc52d699f9324fd6b9
      c = 0x731ceb0ac8f10c8ff82450b61b414c4f7265ccf9f73b8e238cc7265f83c635575a9381aa625044bde7b34ad7cce901fe7512c934b7f6729584d2a77c47e8422c8c0fe2d3dd12aceda8ef904ad5896b971f8b79048e3e2f99f600bf6bac6cad32f922899c00fdc2d21fcf3d0093216bfc5829f02c08ba5e534379cc9118c347763567251c0fe57c92efe0a96c8595bac2c759837211aac914ea3b62aae096ebb8cb384c481b086e660f0c6249c9574289fe91b683609154c066de7a94eafa749c9e92d83a9d473cc88accd9d4c5754ccdbc5aa77ba9a790bc512404a81fc566df42b652a55b9b8ffb189f734d1c007b6cbdb67e14399182016843e27e6d4e5fca
      
      d = owiener.attack(e,n)
      m = pow(c,d,n)
      flag = long_to_bytes(m).decode()
      print(flag)

- Flag
  
![image](https://github.com/user-attachments/assets/7ded5a07-3ec8-49f9-be3e-0e4f271d7489)

- Flag-:```pctf{fun_w1th_l4tt1c3s_f039ab9}```


