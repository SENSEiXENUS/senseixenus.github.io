-----------------

### CTF: QUESTCONCTF

------------------

![image](https://github.com/user-attachments/assets/201d3478-4cce-4604-a4d3-be0e79a1d0f1)

------------------

### Challenges:

- Web
  - Direction
  - Theadmin
  - Temp

------------------

### WEB:

### Direction:

![image](https://github.com/user-attachments/assets/4f776a65-e2c5-4f76-b044-18c3d0f4c467)

- I loaded the site and got this

![image](https://github.com/user-attachments/assets/c01101fe-8612-40fd-93de-7997ec52e9ff)

- I decided to check for the common file `robots.txt` that we all try to find and got a disallowed page.

![image](https://github.com/user-attachments/assets/29d877b6-a391-4a21-9497-0a8a4615cba0)

- I proceeded with curl and noticed an header containing a portion of the flag and automatically redirects to the next page.At first,I couldn't use `GET` for it.I used header `OPTIONS` to find allowed http headers.

![image](https://github.com/user-attachments/assets/9ae29c4e-5969-40cc-a455-77f463277e94)

- Flag portion 1 is shown below and the next flag stop will be the path in the `Location` header.

![image](https://github.com/user-attachments/assets/05c38c13-3f18-4440-bf62-8606f38c8a79)








