------------------

### CTF BSIDESCTF MUMBAI

------------------

![image](https://github.com/user-attachments/assets/a4b42a64-1f70-4091-b3ae-4aa84d952a30)


--------------------

- Web-:
 - Phantom-Binding

---------------------

### [Web]Phantom Binding

----------------------

![image](https://github.com/user-attachments/assets/a965b09f-e7d8-4b06-8b86-42ae916c4476)

-----------------------

- Ffuf's output-:

![image](https://github.com/user-attachments/assets/9d6a9321-1805-47cf-ab05-6569fdf954ee)


- Users get greeted with the login and register page.I followed the normal sequence by creating an account and logging in.

![image](https://github.com/user-attachments/assets/8d53fcbe-0e53-4760-8c75-adf5fcffe96e)

- I noticed a functionality that allows us to upload image through files or url.This can be an interesting point to try out ServerSide Request Forgery.

![image](https://github.com/user-attachments/assets/1fe12180-6655-43b8-a4a3-da665ef2804a)

- I tried to access internal port with the localhost but I didn't get a hit because it got filtered.

![image](https://github.com/user-attachments/assets/7b5d308f-119e-464d-b5a4-c95819f5455e)

- I decided to try this ssrf trick that requires `@`.Any host placed after `@` will get loaded and not the host before it.

```
google.com@127.0.0.1
```

- The `127.0.0.1` will get picked over `google.com`.In my case, I used an ngrok host.

![image](https://github.com/user-attachments/assets/7bcc45d7-acb9-4df8-ab94-8e91fc0e4d3d)

- 


