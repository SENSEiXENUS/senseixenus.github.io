----------------

### CTF: HTB CAMEROON meetup

-----------------

![image](https://github.com/user-attachments/assets/8e7789d6-7573-4859-bdb7-6712e3c774e9)

-----------------

### CHALLENGES-:

- WEB
  - Sequel
  - Iphoto
  - Render Quest

-----------------

### SEQUEL

![image](https://github.com/user-attachments/assets/8f33e837-cb07-496a-9c3d-1e153d1d68b6)

-----------------

- The login page is vulnerable to blind sql injection.I was able to bypass the authentiation process but I was unable to get the flag.

![image](https://github.com/user-attachments/assets/77c9a634-f80e-4b06-8762-8b558686c6f4)

- Then,I tried to exfiltrate data with `Ghauri` and got the flag.Ghauri is an sql injection exploitation tool.

![image](https://github.com/user-attachments/assets/bdaba21a-ff03-4817-8959-b09b4ebb6e63)

- Flag-:```htbmeetupcmr{5QL_1nj3c710n_M45t3ry}```

-----------------

### Iphoto

-----------------

![image](https://github.com/user-attachments/assets/ae6c96ef-8f4f-4e82-946d-3681564e05b8)

------------------

- The site has a file upload functionality and it was created with php.We can try to upload a shell annd gain remote code execution.

![image](https://github.com/user-attachments/assets/d070b161-9cf5-4ca1-9e98-a3b5a3bf0340)

- I tried to upload a regular `php` file and it got flagged immediately.

![image](https://github.com/user-attachments/assets/536adcf6-b00c-4b97-86f0-4c4be47d1231)

- Then,I tried other `php` extensions which worked.`Phtml` bypassed the filters.

![image](https://github.com/user-attachments/assets/64f9e67c-73e1-45f8-9679-c954ea16b4e9)

- RCE gained

![image](https://github.com/user-attachments/assets/cafabc5f-0bf9-4cb5-a8c1-f697500289f0)

- Shell gained

![image](https://github.com/user-attachments/assets/b6ae90b6-ba54-4abd-8eb3-73f3f36c30c6)

### PRIVESC with nmap

- I discovered a password for user in  `home` directory.

![image](https://github.com/user-attachments/assets/46ca8e13-c32c-42cb-a4db-1466ffad6ed1)

- I tried to login to `ctfuser` and it worked.

![image](https://github.com/user-attachments/assets/525f3c35-c121-4a0a-95a7-243346bfe2d5)

- I ran `sudo -l` and I discovered that I can run `nmap` as root.

![image](https://github.com/user-attachments/assets/79211845-2774-4340-82b3-a48ff6de3fc2)

- I






