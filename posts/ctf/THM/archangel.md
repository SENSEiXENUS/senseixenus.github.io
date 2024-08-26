------------------

### CTF: TRYHACKME
### Lab: Archangel

------------------

![image](https://github.com/user-attachments/assets/f7ae508e-590e-409a-92c9-355575db7c23)

-------------------

### RECONNAISSANCE

- Rustscan's output

      ❯ rustscan -a 10.10.221.102 -- -sC -sV
      .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
      | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
      | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
      `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
      The Modern Day Port Scanner.
      ________________________________________
      : https://discord.gg/GFrQsGy           :
      : https://github.com/RustScan/RustScan :
       --------------------------------------
      Real hackers hack time ⌛
      
      [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
      [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
      [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
      Open 10.10.221.102:22
      Open 10.10.221.102:80
      [~] Starting Script(s)
      [>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")                                                                                        
                                                                                                                                                       
      [~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-26 13:23 EDT                                                                           
      NSE: Loaded 156 scripts for scanning.                                                                                                            
      NSE: Script Pre-scanning.                                                                                                                        
      NSE: Starting runlevel 1 (of 3) scan.                                                                                                            
      Initiating NSE at 13:23                                                                                                                          
      Completed NSE at 13:23, 0.00s elapsed                                                                                                            
      NSE: Starting runlevel 2 (of 3) scan.                                                                                                            
      Initiating NSE at 13:23                                                                                                                          
      Completed NSE at 13:23, 0.00s elapsed                                                                                                            
      NSE: Starting runlevel 3 (of 3) scan.                                                                                                            
      Initiating NSE at 13:23                                                                                                                          
      Completed NSE at 13:23, 0.00s elapsed                                                                                                            
      Initiating Ping Scan at 13:23                                                                                                                    
      Scanning 10.10.221.102 [2 ports]                                                                                                                 
      Completed Ping Scan at 13:23, 0.17s elapsed (1 total hosts)                                                                                      
      Initiating Connect Scan at 13:23                                                                                                                 
      Scanning mafialive.thm (10.10.221.102) [2 ports]
      Discovered open port 80/tcp on 10.10.221.102
      Discovered open port 22/tcp on 10.10.221.102
      Completed Connect Scan at 13:23, 0.21s elapsed (2 total ports)
      Initiating Service scan at 13:23
      Scanning 2 services on mafialive.thm (10.10.221.102)
      Completed Service scan at 13:23, 6.67s elapsed (2 services on 1 host)
      NSE: Script scanning 10.10.221.102.
      NSE: Starting runlevel 1 (of 3) scan.
      Initiating NSE at 13:23
      Completed NSE at 13:23, 6.83s elapsed
      NSE: Starting runlevel 2 (of 3) scan.
      Initiating NSE at 13:23
      Completed NSE at 13:23, 0.74s elapsed
      NSE: Starting runlevel 3 (of 3) scan.
      Initiating NSE at 13:23
      Completed NSE at 13:23, 0.01s elapsed
      Nmap scan report for mafialive.thm (10.10.221.102)
      Host is up, received syn-ack (0.18s latency).
      Scanned at 2024-08-26 13:23:04 EDT for 15s
      
      PORT   STATE SERVICE REASON  VERSION
      22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   2048 9f:1d:2c:9d:6c:a4:0e:46:40:50:6f:ed:cf:1c:f3:8c (RSA)
      | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPrwb4vLZ/CJqefgxZMUh3zsubjXMLrKYpP8Oy5jNSRaZynNICWMQNfcuLZ2GZbR84iEQJrNqCFcbsgD+4OPyy0TXV1biJExck3OlriDBn3g9trxh6qcHTBKoUMM3CnEJtuaZ1ZPmmebbRGyrG03jzIow+w2updsJ3C0nkUxdSQ7FaNxwYOZ5S3X5XdLw2RXu/o130fs6qmFYYTm2qii6Ilf5EkyffeYRc8SbPpZKoEpT7TQ08VYEICier9ND408kGERHinsVtBDkaCec3XmWXkFsOJUdW4BYVhrD3M8JBvL1kPmReOnx8Q7JX2JpGDenXNOjEBS3BIX2vjj17Qo3V
      |   256 63:73:27:c7:61:04:25:6a:08:70:7a:36:b2:f2:84:0d (ECDSA)
      | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKhhd/akQ2OLPa2ogtMy7V/GEqDyDz8IZZQ+266QEHke6vdC9papydu1wlbdtMVdOPx1S6zxA4CzyrcIwDQSiCg=
      |   256 b6:4e:d2:9c:37:85:d6:76:53:e8:c4:e0:48:1c:ae:6c (ED25519)
      |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBE3FV9PrmRlGbT2XSUjGvDjlWoA/7nPoHjcCXLer12O
      80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
      | http-robots.txt: 1 disallowed entry 
      |_/test.php
      | http-methods: 
      |_  Supported Methods: GET POST OPTIONS HEAD
      |_http-server-header: Apache/2.4.29 (Ubuntu)
      |_http-title: Site doesn't have a title (text/html).
      Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- I discovered a possible domain while checking the index page.

![image](https://github.com/user-attachments/assets/5afc78d2-8d3c-4519-b99f-df38e104e459)

- The domain `mafialive.thm` is up. Don't forget to add to `/etc/hosts`

![image](https://github.com/user-attachments/assets/10a89299-0874-4ac1-be48-20c0a22dc7ac)

- FFUF's Fuzzing results for `mafialive.thm`

![image](https://github.com/user-attachments/assets/f189b5df-15e5-48d3-8c67-55e5c6385f7a)

- Checking `robots.txt` shows an hidden test.php

![image](https://github.com/user-attachments/assets/21682395-84c1-4593-bfa9-938b25199da8)

- Test.php

![image](https://github.com/user-attachments/assets/796d8211-a6b5-4b9c-b6df-65240e08382f)

### Local File Inclusion

- I checked the source code and noticed that the `view` query allows us to read files

![image](https://github.com/user-attachments/assets/c789dc64-80d3-4587-b548-4fa70d59a9fc)

- The page filters some characters

![image](https://github.com/user-attachments/assets/bdf74ebb-31f3-47e5-9c78-14e5f7715281)

- I used  `php://filter/convert.base64-encode/resource=[filepath]` filter to read files in base64 format.The `include()` allows an attacker to read files
in php but we need to read the code to bypass the filters.We can read the `test.php` directly, php automatically renders or execute the code.
With the aid of the encoding filter,we can pass it out in encoded form instead of php. The filter above renders the file in base64 format.

![image](https://github.com/user-attachments/assets/f1c8f735-6a4b-4252-93df-7ede63cd3d86)









