---------------------

### CTF: HEROCTF

--------------------

![image](https://github.com/user-attachments/assets/c46c04c5-79a0-4415-8d28-ffde384b5481)

--------------------

### CHALLENGES:

- Misc:
  - Moo
- Web:

-------------------

### MISC:
### Einstein:

![image](https://github.com/user-attachments/assets/ff278c3a-6dc1-44be-ade9-ee6e0bdfcfc1)

-------------------

- I sshed to the server with credential `user:password`.

![image](https://github.com/user-attachments/assets/bdf3c0a2-186c-444a-963c-8588777c2f3d)

- The directory contains 2 files, a `C` source code and the compiled code belonging to user `einstein` with suid permissions.

![image](https://github.com/user-attachments/assets/1d6dd633-3ac8-4755-97ed-23b335a1f5f6)

- After checking the source code, I noticed the code is vulnerable to linux file path hijacking because the file path for binary `cat` was not specified.

![image](https://github.com/user-attachments/assets/425a3dff-ba77-45a7-993d-b92bd890b5de)

- I created a new `cat` file in directory `tmp` and set the path variable to `/tmp`.I added a bash code to the malicious `cat`to read the txt files in user
`Einstein`'s directory.

![image](https://github.com/user-attachments/assets/3ea5ef67-aa15-44e2-89e0-c10eff99fd97)

- I ran the `learn` binary and got the flag.

![image](https://github.com/user-attachments/assets/fd568a7f-ea6a-4d66-9692-76aac2c922e1)

- Flag-:```Hero{th30ry_of_r3l4tiv3_p4th5}```






