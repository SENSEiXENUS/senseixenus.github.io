-------------

### CTF: HACKTHEBOX
### LAB-: CYPHER

-------------

![image](https://github.com/user-attachments/assets/98f18401-bf3e-4d72-af9a-48ef1777eaa8)

-------------

- Rustscan's output-:

```bash
❯ rustscan -a cypher.htb -- -Pn -sC -sV
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
Open 10.10.11.57:22
Open 10.10.11.57:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-03-27 08:43 WAT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 08:43
Completed NSE at 08:43, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 08:43
Completed NSE at 08:43, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 08:43
Completed NSE at 08:43, 0.00s elapsed
Initiating Connect Scan at 08:43
Scanning cypher.htb (10.10.11.57) [2 ports]
Discovered open port 22/tcp on 10.10.11.57
Discovered open port 80/tcp on 10.10.11.57
Completed Connect Scan at 08:43, 0.20s elapsed (2 total ports)
Initiating Service scan at 08:44
Scanning 2 services on cypher.htb (10.10.11.57)
Completed Service scan at 08:44, 14.69s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.57.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 08:44
Completed NSE at 08:44, 7.12s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 08:44
Completed NSE at 08:44, 1.07s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 08:44
Completed NSE at 08:44, 0.00s elapsed
Nmap scan report for cypher.htb (10.10.11.57)
Host is up, received user-set (0.20s latency).
Scanned at 2025-03-27 08:43:58 WAT for 25s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 9.6p1 Ubuntu 3ubuntu13.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 be:68:db:82:8e:63:32:45:54:46:b7:08:7b:3b:52:b0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMurODrr5ER4wj9mB2tWhXcLIcrm4Bo1lIEufLYIEBVY4h4ZROFj2+WFnXlGNqLG6ZB+DWQHRgG/6wg71wcElxA=
|   256 e5:5b:34:f5:54:43:93:f8:7e:b6:69:4c:ac:d6:3d:23 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEqadcsjXAxI3uSmNBA8HUMR3L4lTaePj3o6vhgPuPTi
80/tcp open  http    syn-ack nginx 1.24.0 (Ubuntu)
|_http-title: GRAPH ASM
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: nginx/1.24.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Ffuf's output

![image](https://github.com/user-attachments/assets/ceee1d75-8398-4293-b3e3-925b6e6cdc41)

- I discovered this jar in which will later be explained.It is crucial in another stage.

![image](https://github.com/user-attachments/assets/87250fcc-9f25-45fe-84bd-e3e5deb27aff)

- I tested the login page with single quote and got this giant blob of error.

![image](https://github.com/user-attachments/assets/d0fb74a9-3e97-4bc1-8447-46e2a3fadc6d)

- Lets look at it closer with curl because notification box disappears after some seconds.

![image](https://github.com/user-attachments/assets/bb3610b1-c224-4c9b-9544-c050803b49ba)

- I discovered it is a neo4j database which is a graph type of  database.A graph database is defined as a specialized, single-purpose platform for creating and manipulating graphs. Graphs contain nodes, edges, and properties, all of which are used to represent and store data in a way that relational databases are not equipped to do as explained [here](https://www.oracle.com/ng/autonomous-database/what-is-graph-database/).I got an interesting [article](https://hackmd.io/@Chivato/rkAN7Q9NY#Fun-with-Cypher-Injections) to exploit it.
- 


