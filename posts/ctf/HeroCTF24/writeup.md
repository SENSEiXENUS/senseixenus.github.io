---------------------

### CTF: HEROCTF

--------------------

![image](https://github.com/user-attachments/assets/c46c04c5-79a0-4415-8d28-ffde384b5481)

--------------------

### CHALLENGES:

- Misc:
  - Einstein
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

----------------------

### MOO

----------------------

![image](https://github.com/user-attachments/assets/2d4568c9-25e2-45f8-903c-ac519c5e380e)

- I sshed to the instance and discovered that it is a restricted shell because I could not run regular commands.

![image](https://github.com/user-attachments/assets/2c0bc90b-3fff-4833-876b-4ccd49e8619e)

- I ran export to check for binary path and noticed that it runs only binaries located in `/usr/local/rbin`.

![image](https://github.com/user-attachments/assets/20a761de-9f99-4f8c-94cb-3b3cae550674)

- Later, I noticed that I could not specify paths because `\` was blacklisted.In the binaries' directories,I discovered a binary `cowsay`.

![image](https://github.com/user-attachments/assets/ca738579-5a5e-43d7-865f-5c650f074913)

- I checked `gtfobins` and found that `cowsay` can run perl code in a file.I used vim to write the code in a file and ran it.

![image](https://github.com/user-attachments/assets/56973b8c-d6f7-4a7c-a950-117003601e16)

- I used vim to write the code in a file and ran it.Now,we have broken out of the restricted shell.I was able to read the `/etc/passwd` file.

![image](https://github.com/user-attachments/assets/b45ee0b4-2932-481f-ba89-c0f3733deedf)

- Flag-:```Hero{s0m3_s4cr3d_c0w}```

![image](https://github.com/user-attachments/assets/8257b5c7-0a92-4d8d-bab8-11a3eebe3bf2)








