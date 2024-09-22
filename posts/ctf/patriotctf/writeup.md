--------------

### CTF: PATRIOTCTF

--------------

![image](https://github.com/user-attachments/assets/ba12119a-dda7-4411-9c7e-f30e71a1bae6)

--------------

- WEB
  - Giraffe-notes
  - Impersonate

-----------------

### Impersonate

![image](https://github.com/user-attachments/assets/01003049-3c72-408b-ad2d-e7620ef2bb49)

### Source Code review

- The app is a flask web app which is a python web framework.The app uses the `datetime.datetime.now()` to grab the current date which is when the server got booted.Then,it converts
the date into string using function `strftime()` and format `%Y%m%d%H%M%S`.Lastly, it hashes it and store the result as the flask app session key.

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
- Lastly, the `status` route presents the uptime and current_time.The current time is the present time, while the `uptime` is the `currenttime` - `server_xtart_time` which is then formatted.There is a certain twist not specified in the code, the server gets rebooted every 5 mins.

          current_time = datetime.now()
          uptime = current_time - server_start_time
          formatted_uptime = str(uptime).split('.')[0]

### Exploitation

- I visited the status page to get the `year|month|date|hour` since the hour remains static but subject to change as time moves.Then,I can create a wordlist generator that adds the minutes and seconds.We  need only 4 figures whill will between range `0000-9999`.

