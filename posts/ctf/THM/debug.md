--------------------

### TRYHACKME
### Lab: Debug:

--------------------


### Recon

- Rustscan's output

      ❯ rustscan -a 10.10.201.128 -- -sC -sV
      .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
      | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
      | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
      `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
      The Modern Day Port Scanner.
      ________________________________________
      : https://discord.gg/GFrQsGy           :
      : https://github.com/RustScan/RustScan :
       --------------------------------------
      Nmap? More like slowmap.🐢
      
      [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
      [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
      [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
      Open 10.10.201.128:22
      Open 10.10.201.128:80
      [~] Starting Script(s)
      [>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")                                                                                        
                                                                                                                                                       
      [~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-17 16:03 EDT                                                                           
      NSE: Loaded 156 scripts for scanning.                                                                                                            
      NSE: Script Pre-scanning.                                                                                                                        
      NSE: Starting runlevel 1 (of 3) scan.                                                                                                            
      Initiating NSE at 16:03                                                                                                                          
      Completed NSE at 16:03, 0.00s elapsed                                                                                                            
      NSE: Starting runlevel 2 (of 3) scan.                                                                                                            
      Initiating NSE at 16:03                                                                                                                          
      Completed NSE at 16:03, 0.00s elapsed                                                                                                            
      NSE: Starting runlevel 3 (of 3) scan.                                                                                                            
      Initiating NSE at 16:03                                                                                                                          
      Completed NSE at 16:03, 0.00s elapsed                                                                                                            
      Initiating Ping Scan at 16:03                                                                                                                    
      Scanning 10.10.201.128 [2 ports]                                                                                                                 
      Completed Ping Scan at 16:03, 0.15s elapsed (1 total hosts)                                                                                      
      Initiating Parallel DNS resolution of 1 host. at 16:03                                                                                           
      Completed Parallel DNS resolution of 1 host. at 16:03, 0.02s elapsed
      DNS resolution of 1 IPs took 0.06s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
      Initiating Connect Scan at 16:03
      Scanning 10.10.201.128 [2 ports]
      Discovered open port 22/tcp on 10.10.201.128
      Discovered open port 80/tcp on 10.10.201.128
      Completed Connect Scan at 16:03, 0.18s elapsed (2 total ports)
      Initiating Service scan at 16:03
      Scanning 2 services on 10.10.201.128
      Completed Service scan at 16:03, 6.82s elapsed (2 services on 1 host)
      NSE: Script scanning 10.10.201.128.
      NSE: Starting runlevel 1 (of 3) scan.
      Initiating NSE at 16:03
      Completed NSE at 16:04, 9.48s elapsed
      NSE: Starting runlevel 2 (of 3) scan.
      Initiating NSE at 16:04
      Completed NSE at 16:04, 1.02s elapsed
      NSE: Starting runlevel 3 (of 3) scan.
      Initiating NSE at 16:04
      Completed NSE at 16:04, 0.00s elapsed
      Nmap scan report for 10.10.201.128
      Host is up, received syn-ack (0.16s latency).
      Scanned at 2024-08-17 16:03:47 EDT for 18s
      
      PORT   STATE SERVICE REASON  VERSION
      22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   2048 44:ee:1e:ba:07:2a:54:69:ff:11:e3:49:d7:db:a9:01 (RSA)
      | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDar9Wvsxi0NTtlrjfNnap7o6OD9e/Eug2nZF18xx17tNZC/iVn5eByde27ZzR4Gf10FwleJzW5B7ieEThO3Ry5/kMZYbobY2nI8F3s20R8+sb6IdWDL4NIkFPqsDudH3LORxECx0DtwNdqgMgqeh/fCys1BzU2v2MvP5alraQmX81h1AMDQPTo9nDHEJ6bc4Tt5NyoMZZSUXDfJRutsmt969AROoyDsoJOrkwdRUmYHrPqA5fvLtWsWXHYKGsWOPZSe0HIq4wUthMf65RQynFQRwErrJlQmOIKjMV9XkmWQ8c/DqA1h7xKtbfeUYa9nEfhO4HoSkwS0lCErj+l9p8h
      |   256 8b:2a:8f:d8:40:95:33:d5:fa:7a:40:6a:7f:29:e4:03 (ECDSA)
      | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBA7IA5s8W9jhxGAF1s4Q4BNSu1A52E+rSyFGBYdecgcJJ/sNZ3uL6sjZEsAfJG83m22c0HgoePkuWrkdK2oRnbs=
      |   256 65:59:e4:40:2a:c2:d7:05:77:b3:af:60:da:cd:fc:67 (ED25519)
      |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGXyfw0mC4ho9k8bd+n0BpaYrda6qT2eI1pi8TBYXKMb
      80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
      |_http-title: Apache2 Ubuntu Default Page: It works
      |_http-server-header: Apache/2.4.18 (Ubuntu)
      | http-methods: 
      |_  Supported Methods: GET HEAD POST OPTIONS
      Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- FFUF's output

![image](https://github.com/user-attachments/assets/1fa2b2c5-0673-4efb-9a8d-1ac3ee691861)

- Route `/backup` reveals the backup source code files of the site and focus will be on finding vulnerabilities in `index.php.bak`

![image](https://github.com/user-attachments/assets/2c6de75a-dbe1-4217-b4ee-e6cc3209d5ad)


### CODE REVIEW OF index.php

-


  


