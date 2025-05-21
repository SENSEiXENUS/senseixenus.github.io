* * *

### LAB: Environment
### CTF: HACKTHEBOX

* * *

- Rustscan's output-:

```bash
❯ rustscan -a environment.htb -- -Pn -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/sensei/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.11.67:22
Open 10.10.11.67:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-05-13 15:49 WAT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:49
Completed NSE at 15:49, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:49
Completed NSE at 15:49, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:49
Completed NSE at 15:49, 0.00s elapsed
Initiating Connect Scan at 15:49
Scanning environment.htb (10.10.11.67) [2 ports]
Discovered open port 22/tcp on 10.10.11.67
Discovered open port 80/tcp on 10.10.11.67
Completed Connect Scan at 15:49, 2.25s elapsed (2 total ports)
Initiating Service scan at 15:49
Scanning 2 services on environment.htb (10.10.11.67)
Completed Service scan at 15:49, 6.64s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.67.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:49
Completed NSE at 15:49, 17.51s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:49
Completed NSE at 15:49, 2.92s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:49
Completed NSE at 15:49, 0.00s elapsed
Nmap scan report for environment.htb (10.10.11.67)
Host is up, received user-set (0.25s latency).
Scanned at 2025-05-13 15:49:15 WAT for 30s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 9.2p1 Debian 2+deb12u5 (protocol 2.0)
| ssh-hostkey: 
|   256 5c:02:33:95:ef:44:e2:80:cd:3a:96:02:23:f1:92:64 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGrihP7aP61ww7KrHUutuC/GKOyHifRmeM070LMF7b6vguneFJ3dokS/UwZxcp+H82U2LL+patf3wEpLZz1oZdQ=
|   256 1f:3d:c2:19:55:28:a1:77:59:51:48:10:c4:4b:74:ab (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ7xeTjQWBwI6WERkd6C7qIKOCnXxGGtesEDTnFtL2f2
80/tcp open  http    syn-ack nginx 1.22.1
|_http-title: Save the Environment | environment.htb
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-server-header: nginx/1.22.1
| http-methods: 
|_  Supported Methods: GET HEAD
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- I identified Laravel's version because debug mode is enabled.I made a `GET` request to the directory upload and encountered an error which exposed the php and laravel build

![image](https://github.com/user-attachments/assets/be5c2345-a912-4073-9df4-2b90c4049ad4)

- I googled for CVES related to this version and got [one](https://github.com/Nyamort/CVE-2024-52301).Laravel is vulnerable to argument injection which occurs if the `register_argc_argv` option is enabled in the php.ini.This setting loads command-line arguments and query params into `$_SERVER['argv']`.The vulnerability allows us to set the environment that the laravel web app will load which signifies that we can load old environments that can be vulnerable.

POC-:
```<url>/?env--=production
```

- Our next task is to find pre-existing enviroment before `production`.I tried to trigger more errors to discover more parts of the source code.I tried to login with no values in the params and I got another error/


