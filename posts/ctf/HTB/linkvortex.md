--------------

### CTF-: Hackthebox
### Lab-: LinkVortex

---------------

![image](https://github.com/user-attachments/assets/8d634aaf-9e9d-4915-8758-c94e67d0d2b4)

-----------------

- Rustscan's output

```bash
❯ rustscan -a linkvortex.htb -- -Pn -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/sensei/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.11.47:22
Open 10.10.11.47:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-02-23 05:04 WAT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 05:04
Completed NSE at 05:04, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 05:04                                                                                                                            
Completed NSE at 05:04, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 05:04
Completed NSE at 05:04, 0.00s elapsed
Initiating Connect Scan at 05:04
Scanning linkvortex.htb (10.10.11.47) [2 ports]
Discovered open port 22/tcp on 10.10.11.47
Discovered open port 80/tcp on 10.10.11.47
Completed Connect Scan at 05:04, 0.21s elapsed (2 total ports)
Initiating Service scan at 05:04
Scanning 2 services on linkvortex.htb (10.10.11.47)
Completed Service scan at 05:04, 6.47s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.47.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 05:04
Completed NSE at 05:05, 7.10s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 05:05
Completed NSE at 05:05, 0.87s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 05:05
Completed NSE at 05:05, 0.00s elapsed
Nmap scan report for linkvortex.htb (10.10.11.47)
Host is up, received user-set (0.22s latency).
Scanned at 2025-02-23 05:04:49 WAT for 15s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:f8:b9:68:c8:eb:57:0f:cb:0b:47:b9:86:50:83:eb (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMHm4UQPajtDjitK8Adg02NRYua67JghmS5m3E+yMq2gwZZJQ/3sIDezw2DVl9trh0gUedrzkqAAG1IMi17G/HA=
|   256 a2:ea:6e:e1:b6:d7:e7:c5:86:69:ce:ba:05:9e:38:13 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKKLjX3ghPjmmBL2iV1RCQV9QELEU+NF06nbXTqqj4dz
80/tcp open  http    syn-ack Apache httpd
| http-methods: 
|_  Supported Methods: POST GET HEAD OPTIONS
|_http-generator: Ghost 5.58
|_http-server-header: Apache
| http-robots.txt: 4 disallowed entries 
|_/ghost/ /p/ /email/ /r/
|_http-favicon: Unknown favicon MD5: A9C6DBDCDC3AE568F4E0DAD92149A0E3
|_http-title: BitByBit Hardware
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Subdomain enumeration-:

![image](https://github.com/user-attachments/assets/89b5bd4a-9217-4c7a-ac8f-9f23834e132a)

- I discovered a git directory after fuzzing the `dev` subdomain.

![image](https://github.com/user-attachments/assets/80cfb290-a26e-4279-a885-6b5146f47385)

- I recovered the `.git` directory with this [GitHacker](https://vedantyaduvanshi.medium.com/linkvortex-htb-writeup-5ec058845d9f) tool.

![image](https://github.com/user-attachments/assets/6fb65072-6a84-4afb-bbd1-ddfb407becb0)

- I grepped for credentials and discovered a password.

![image](https://github.com/user-attachments/assets/0c4810df-10dd-4610-b2e1-e7a0f2d354a3)

- I guessed the email which I presumed should be "admin@linkvortex.htb" which worked.I am logged in as the admin.

![image](https://github.com/user-attachments/assets/0ff543bf-f0d5-455c-be15-62dcee9213bd)

- The dockerfile in the git repo showed the version of the ghost cms.

![image](https://github.com/user-attachments/assets/1e31dccb-be09-44f8-bebb-274a2e6a8ad9)

- This version of Ghost cms is vulnerable to `Arbitrary File Read`.I discovered an exploit [here](https://github.com/0xDTC/Ghost-5.58-Arbitrary-File-Read-CVE-2023-40028).I read file `/etc/passwd`.

![image](https://github.com/user-attachments/assets/375ff4d8-c98f-4b6d-8b82-75b032509c3a)

- Then,I noticed a config file provided in the `Dockerfile` which might contain necessary credentials.

![image](https://github.com/user-attachments/assets/82e7c53e-760e-44ec-b414-355b6198fbad)




