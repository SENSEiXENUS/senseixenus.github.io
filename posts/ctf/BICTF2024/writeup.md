* * *

### CTF: BICCTF 24

* * *

------------------------

### CHALLENGES

### B2R

-     Pirate King:Question [9] - [12]

-----------------------

### Pirate King

![image](https://github.com/user-attachments/assets/53744598-c639-4c2a-9fab-074e4051614a)

- The server was hosted on ip:`54.226.229.244`
- I scanned with Rustcan and discovered 2 open ports, port 80 `http` and port 22 `ssh` respectively.

- The site's source code contains this hint to check `robots.txt` file

![image](https://github.com/user-attachments/assets/e6ee4bf9-940e-4540-b413-41652c4611b3)

- The robots.txt file disallow crawling of files `syrup.jpeg` and `kaya.txt`
![image](https://github.com/user-attachments/assets/88594d64-5b2b-462b-a829-1e020033be19)

- Kaya.txt leads us to `dev_shell.php` page where we can execute shell commands.Although the shell code filters shell commands


