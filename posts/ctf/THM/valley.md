--------------

### CTF-: Valley
### LAB-: THM

--------------

![image](https://github.com/user-attachments/assets/23beca8c-b484-4a08-bb72-6a4a7e450e70)

--------------

- Rustscan's output-:

```bash
❯ rustscan -a 10.10.57.116 -- -Pn -sC -sV
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/sensei/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.57.116:22
Open 10.10.57.116:80
Open 10.10.57.116:37370
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-31 14:29 WAT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:30
Completed NSE at 14:30, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:30
Completed NSE at 14:30, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:30
Completed NSE at 14:30, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 14:30
Completed Parallel DNS resolution of 1 host. at 14:30, 0.05s elapsed
DNS resolution of 1 IPs took 0.05s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 14:30
Scanning 10.10.57.116 [3 ports]
Discovered open port 37370/tcp on 10.10.57.116
Discovered open port 80/tcp on 10.10.57.116
Discovered open port 22/tcp on 10.10.57.116
Completed Connect Scan at 14:30, 0.24s elapsed (3 total ports)
Initiating Service scan at 14:30
Scanning 3 services on 10.10.57.116
Completed Service scan at 14:30, 6.40s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.57.116.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:30
Completed NSE at 14:30, 13.06s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:30
Completed NSE at 14:30, 1.56s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:30
Completed NSE at 14:30, 0.00s elapsed
Nmap scan report for 10.10.57.116
Host is up, received user-set (0.24s latency).
Scanned at 2024-12-31 14:30:05 WAT for 21s

PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c2:84:2a:c1:22:5a:10:f1:66:16:dd:a0:f6:04:62:95 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCf7Zvn7fOyAWUwEI2aH/k8AyPehxzzuNC1v4AAlhDa4Off4085gRIH/EXpjOoZSBvo8magsCH32JaKMMc59FSK4canP2I0VrXwkEX0F8PjA1TV4qgqXJI0zNVwFrfBORDdlCPNYiqRNFp1vaxTqLOFuHt5r34134yRwczxTsD4Uf9Z6c7Yzr0GV6NL3baGHDeSZ/msTiFKFzLTTKbFkbU4SQYc7jIWjl0ylQ6qtWivBiavEWTwkHHKWGg9WEdFpU2zjeYTrDNnaEfouD67dXznI+FiiTiFf4KC9/1C+msppC0o77nxTGI0352wtBV9KjTU/Aja+zSTMDxoGVvo/BabczvRCTwhXxzVpWNe3YTGeoNESyUGLKA6kUBfFNICrJD2JR7pXYKuZVwpJUUCpy5n6MetnonUo0SoMg/fzqMWw2nCZOpKzVo9OdD8R/ZTnX/iQKGNNvgD7RkbxxFK5OA9TlvfvuRUQQaQP7+UctsaqG2F9gUfWorSdizFwfdKvRU=
|   256 42:9e:2f:f6:3e:5a:db:51:99:62:71:c4:8c:22:3e:bb (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNIiJc4hdfcu/HtdZN1fyz/hU1SgSas1Lk/ncNc9UkfSDG2SQziJ/5SEj1AQhK0T4NdVeaMSDEunQnrmD1tJ9hg=
|   256 2e:a0:a5:6c:d9:83:e0:01:6c:b9:8a:60:9b:63:86:72 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEZhkboYdSkdR3n1G4sQtN4uO3hy89JxYkizKi6Sd/Ky
80/tcp    open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
37370/tcp open  ftp     syn-ack vsftpd 3.0.3
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel
```
- Ftp is on port `37370`.
