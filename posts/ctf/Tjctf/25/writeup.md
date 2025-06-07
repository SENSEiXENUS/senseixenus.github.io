------------------

### CTF-: TJCTF 2025

------------------

- Web-:
  - Loopy
  - Texploit
  - Chilly-site

------------------

### Loopy

------------------

![image](https://github.com/user-attachments/assets/faccb1a6-72ec-437d-bbd7-8135c2400c9f)

------------------

- The website allows users to preview site which fits a Server Side Request Forgery scenario.

![image](https://github.com/user-attachments/assets/94cfbb3c-81d6-4518-a156-996930936ce9)

- The challenge description gave a hint to load a service at port `5000`.I tried to load it with `localhost:5000` and it  didn't work.Oops, it looks like the site has a long list of filters for the service.

![image](https://github.com/user-attachments/assets/be0b14a8-cfa0-4cc5-8ff4-9c6ee91393ae)

- You can try simple ssrf bypass tricks by using a redirect or just look another represntation of localhost which worked for me. Bypass-: ```http://0:5000/admin```.

![image](https://github.com/user-attachments/assets/82997e35-23b5-4a92-8f30-8f63bb633633)

- Flag-:```tjctf{i_l0v3_ssssSsrF_9o4a8}```

--------------------

### Texploit

--------------------

![image](https://github.com/user-attachments/assets/1774ea97-8ba2-4693-925a-f6d5e5022131)

---------------------

- 




