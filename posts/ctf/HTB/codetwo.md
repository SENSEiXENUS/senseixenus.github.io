--------------

### CTF-: HACKTHEBOX
### LAB-: Codetwo

--------------

<img width="793" height="169" alt="image" src="https://github.com/user-attachments/assets/4c25ec09-54f9-424e-a491-fee1245cd66a" />

--------------

- Rustscan's result-:

```bash                                                                                                                                                                      ─╯
╭─   ~/labs/htb/editor                                                                                                                                                    at  13:04:33 ─╮
╰─❯ rustscan -a 10.10.11.82 -- -sC -sV                                                                                                                                                    ─╯
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: http://discord.skerritt.blog         :
: https://github.com/RustScan/RustScan :
 --------------------------------------
RustScan: allowing you to send UDP packets into the void 1200x faster than NMAP

[~] The config file is expected to be at "/home/sensei/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.11.82:22
Open 10.10.11.82:8000
[~] Starting Script(s)
[>] Running script "nmap -vvv -p {{port}} -{{ipversion}} {{ip}} -sC -sV" on ip 10.10.11.82
Depending on the complexity of the script, results may take some time to appear.
[~] Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-20 13:05 WAT
NSE: Loaded 157 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
Initiating Ping Scan at 13:05
Scanning 10.10.11.82 [4 ports]
Completed Ping Scan at 13:05, 0.24s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 13:05
Scanning codetwo (10.10.11.82) [2 ports]
Discovered open port 22/tcp on 10.10.11.82
Discovered open port 8000/tcp on 10.10.11.82
Completed SYN Stealth Scan at 13:05, 0.22s elapsed (2 total ports)
Initiating Service scan at 13:05
Scanning 2 services on codetwo (10.10.11.82)
Completed Service scan at 13:05, 7.43s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.82.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 9.47s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 1.44s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.01s elapsed
Nmap scan report for codetwo (10.10.11.82)
Host is up, received echo-reply ttl 63 (0.21s latency).
Scanned at 2025-08-20 13:05:40 WAT for 19s

PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 a0:47:b4:0c:69:67:93:3a:f9:b4:5d:b3:2f:bc:9e:23 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCnwmWCXCzed9BzxaxS90h2iYyuDOrE2LkavbNeMlEUPvMpznuB9cs8CTnUenkaIA8RBb4mOfWGxAQ6a/nmKOea1FA6rfGG+fhOE/R1g8BkVoKGkpP1hR2XWbS3DWxJx3UUoKUDgFGSLsEDuW1C+ylg8UajGokSzK9NEg23WMpc6f+FORwJeHzOzsmjVktNrWeTOZthVkvQfqiDyB4bN0cTsv1mAp1jjbNnf/pALACTUmxgEemnTOsWk3Yt1fQkkT8IEQcOqqGQtSmOV9xbUmv6Y5ZoCAssWRYQ+JcR1vrzjoposAaMG8pjkUnXUN0KF/AtdXE37rGU0DLTO9+eAHXhvdujYukhwMp8GDi1fyZagAW+8YJb8uzeJBtkeMo0PFRIkKv4h/uy934gE0eJlnvnrnoYkKcXe+wUjnXBfJ/JhBlJvKtpLTgZwwlh95FJBiGLg5iiVaLB2v45vHTkpn5xo7AsUpW93Tkf+6ezP+1f3P7tiUlg3ostgHpHL5Z9478=
|   256 7d:44:3f:f1:b1:e2:bb:3d:91:d5:da:58:0f:51:e5:ad (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBErhv1LbQSlbwl0ojaKls8F4eaTL4X4Uv6SYgH6Oe4Y+2qQddG0eQetFslxNF8dma6FK2YGcSZpICHKuY+ERh9c=
|   256 f1:6b:1d:36:18:06:7a:05:3f:07:57:e1:ef:86:b4:85 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEJovaecM3DB4YxWK2pI7sTAv9PrxTbpLG2k97nMp+FM
8000/tcp open  http    syn-ack ttl 63 Gunicorn 20.0.4
| http-methods: 
|_  Supported Methods: HEAD GET OPTIONS
|_http-server-header: gunicorn/20.0.4
|_http-title: Welcome to CodeTwo
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Port `8000`-:

<img width="717" height="710" alt="image" src="https://github.com/user-attachments/assets/8976f564-ef18-4fbe-96ee-9d4a7eea2258" />

- The app's source code was provided for the challenge.

<img width="576" height="544" alt="image" src="https://github.com/user-attachments/assets/6305dd36-9faa-473b-b23f-d8e70264e571" />

- I checked the `app.py` and discovered a vulnerable python module `js2py`.The vulnerable function `js2py.eval_js()` allows attackers to bypass the sandbox restrictions and execute python code as explained [here](https://github.com/Marven11/CVE-2024-28397-js2py-Sandbox-Escape).

```python
def run_code():
    try:
        code = request.json.get('code')
        result = js2py.eval_js(code)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
```

- 
