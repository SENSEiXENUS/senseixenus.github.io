-----------------

### CTF: TRYHACKME
### LAB: Expose

------------------

![image](https://github.com/user-attachments/assets/1f904084-8c3c-4b2d-9d78-59b279eaa519)

------------------

- Rustscan's output

```bash
❯ rustscan -a 10.10.140.248 -- -Pn -sC -sV
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
Open 10.10.140.248:21
Open 10.10.140.248:22
Open 10.10.140.248:53
Open 10.10.140.248:1883
Open 10.10.140.248:1337
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-27 12:03 WAT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:03
Completed NSE at 12:03, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:03
Completed NSE at 12:03, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:03
Completed NSE at 12:03, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 12:03
Completed Parallel DNS resolution of 1 host. at 12:03, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:03
Scanning 10.10.140.248 [5 ports]
Discovered open port 21/tcp on 10.10.140.248
Discovered open port 22/tcp on 10.10.140.248
Discovered open port 53/tcp on 10.10.140.248
Discovered open port 1883/tcp on 10.10.140.248
Discovered open port 1337/tcp on 10.10.140.248
Completed Connect Scan at 12:03, 0.41s elapsed (5 total ports)
Initiating Service scan at 12:03
Scanning 5 services on 10.10.140.248
Completed Service scan at 12:04, 11.73s elapsed (5 services on 1 host)
NSE: Script scanning 10.10.140.248.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:04
NSE: [ftp-bounce 10.10.140.248:21] PORT response: 500 Illegal PORT command.
Completed NSE at 12:04, 10.07s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 1.60s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
Nmap scan report for 10.10.140.248
Host is up, received user-set (0.41s latency).
Scanned at 2024-11-27 12:03:52 WAT for 24s

PORT     STATE SERVICE                 REASON  VERSION
21/tcp   open  ftp                     syn-ack vsftpd 2.0.8 or later
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.23.45.35
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 5
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh                     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 ae:da:97:e5:c7:fe:6b:d1:e3:35:51:5f:ad:ad:89:d4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCsKB7ppF6NLFhtNRx7WC05tbwUkmPIKizAKBv5qxzQfiwSAwX/Cxpamkndb+azMxc8tQ7AFz/PedMdxRwjrBy8Rabwz010UZDXLmvCoDzUYcUQY9SiXRxQD0MLR+U9tts77f+HXIqm4n+FziGezS04LwjB76Bv0tB4ilVBi1u1yOCDHWkxzFCvCYb+ygvP4hLSpoWlEj53wJfk3hB7oYUX5PmGX4o2CrFgfOUKIql71Ch8qQptCA7wqb8tlcd38K2meH2XJszRcdAInCJl7t1BMVMhEf39brjFJsj6iZ1FEU7jn+L/RS9xb0xn680D/upoS7cEgtlWEqV6sqGiEXWAYCA4wlJwfyW8df4XvBhFuSW3D9Ndzm8K09EjqaWNUGhWufZwiQs8zwqBlESL+Pm9VGCkHt35kDAPjM6z5Hu9jdgnyMRCYmYoLq/vqUVqN2DRQaDVB2A4EaBhAYyFdK0JdWVek6rZUx8RmgH94sYFdvs2NkDA3UFliE6uCEAW1ak=
|   256 85:95:e6:c0:74:ab:de:2c:92:27:24:12:3b:96:c9:fc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC0m93ykBdid8g9Hmr0kaxLEkQlSgu3bgKe5+LhYws+wrluiqZ0oWY4GlClUYTk+zsvQxH9CF38WUmr0WSrmJ5g=
|   256 8f:4e:03:3c:ef:a7:8b:a0:65:54:b4:f6:a3:8c:af:0a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIClOMU/FU+0ss9IC79LV64VwUp521fQu/PsFmb1fhqIz
53/tcp   open  domain                  syn-ack ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
1337/tcp open  http                    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: EXPOSED
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
1883/tcp open  mosquitto version 1.6.9 syn-ack
| mqtt-subscribe: 
|   Topics and their most recent payloads: 
|     $SYS/broker/bytes/sent: 4
|     $SYS/broker/load/bytes/received/5min: 3.53
|     $SYS/broker/load/connections/1min: 0.91
|     $SYS/broker/load/bytes/sent/1min: 3.65
|     $SYS/broker/bytes/received: 18
|     $SYS/broker/messages/sent: 1
|     $SYS/broker/load/messages/sent/5min: 0.20
|     $SYS/broker/load/connections/15min: 0.07
|     $SYS/broker/load/connections/5min: 0.20
|     $SYS/broker/load/messages/sent/1min: 0.91
|     $SYS/broker/load/messages/sent/15min: 0.07
|     $SYS/broker/messages/received: 1
|     $SYS/broker/version: mosquitto version 1.6.9
|     $SYS/broker/load/bytes/received/15min: 1.19
|     $SYS/broker/uptime: 143 seconds
|     $SYS/broker/store/messages/bytes: 179
|     $SYS/broker/load/bytes/sent/15min: 0.27
|     $SYS/broker/load/sockets/5min: 0.56
|     $SYS/broker/load/sockets/1min: 2.19
|     $SYS/broker/load/sockets/15min: 0.19
|     $SYS/broker/load/bytes/sent/5min: 0.79
|     $SYS/broker/load/messages/received/15min: 0.07
|     $SYS/broker/load/bytes/received/1min: 16.45
|     $SYS/broker/heap/maximum: 49688
|     $SYS/broker/load/messages/received/1min: 0.91
|_    $SYS/broker/load/messages/received/5min: 0.20
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Ffuf's output for http serve ron port `1337`

![image](https://github.com/user-attachments/assets/e957d657-2132-490f-8077-330ce70b8af1)

- The admin page in directory `admin_101` hosts a login page with the username value `hacker@root.thm`.

![image](https://github.com/user-attachments/assets/8166b15b-e817-4c66-a3e3-b228203c61cf)

- I tried the basic sql injection payload `<username>'--` and got an `undefined` alert.

![image](https://github.com/user-attachments/assets/1b2fbdf1-7066-430b-beb8-3e2107e35a7b)

- Then, I tested for sql injection with the `ghauri` tool and was able to dump the data.

- Important highlights are detailed in the pictures.The first pictures shows the password for the username which we don't need because it is a rabbit hole while the second picture shows urls and a password hash.






