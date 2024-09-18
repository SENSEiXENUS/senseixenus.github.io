---------------

### CTF: TRYHACKME
### LAB: Lunizzctf

---------------

![image](https://github.com/user-attachments/assets/41427d12-504a-47f6-b8cb-35ad3fa6d9fe)

----------------

### RECONNAISSANCE

- Rustscan's output

      ❯ rustscan -a 10.10.218.103 -- -Pn -sC -sV
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
      Open 10.10.218.103:80
      Open 10.10.218.103:3306
      Open 10.10.218.103:4444
      Open 10.10.218.103:5000
      [~] Starting Script(s)
      [>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")
      
      Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
      [~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-18 06:56 EDT
      NSE: Loaded 156 scripts for scanning.
      NSE: Script Pre-scanning.
      NSE: Starting runlevel 1 (of 3) scan.
      Initiating NSE at 06:56
      Completed NSE at 06:56, 0.00s elapsed
      NSE: Starting runlevel 2 (of 3) scan.
      Initiating NSE at 06:56
      Completed NSE at 06:56, 0.00s elapsed
      NSE: Starting runlevel 3 (of 3) scan.
      Initiating NSE at 06:56
      Completed NSE at 06:56, 0.00s elapsed
      Initiating Parallel DNS resolution of 1 host. at 06:56
      Completed Parallel DNS resolution of 1 host. at 06:56, 0.03s elapsed
      DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
      Initiating Connect Scan at 06:56
      Scanning 10.10.218.103 [4 ports]
      Discovered open port 3306/tcp on 10.10.218.103
      Discovered open port 80/tcp on 10.10.218.103
      Discovered open port 5000/tcp on 10.10.218.103
      Discovered open port 4444/tcp on 10.10.218.103
      Completed Connect Scan at 06:56, 0.16s elapsed (4 total ports)
      Initiating Service scan at 06:56
      Scanning 4 services on 10.10.218.103
      Completed Service scan at 06:56, 7.43s elapsed (4 services on 1 host)
      NSE: Script scanning 10.10.218.103.
      NSE: Starting runlevel 1 (of 3) scan.
      Initiating NSE at 06:56
      Completed NSE at 06:56, 5.89s elapsed
      NSE: Starting runlevel 2 (of 3) scan.
      Initiating NSE at 06:56
      Completed NSE at 06:56, 2.76s elapsed
      NSE: Starting runlevel 3 (of 3) scan.
      Initiating NSE at 06:56
      Completed NSE at 06:56, 0.00s elapsed
      Nmap scan report for 10.10.218.103
      Host is up, received user-set (0.16s latency).
      Scanned at 2024-09-18 06:56:04 EDT for 17s
      
      PORT     STATE SERVICE REASON  VERSION
      80/tcp   open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
      | http-methods: 
      |_  Supported Methods: GET POST OPTIONS HEAD
      |_http-title: Apache2 Ubuntu Default Page: It works
      |_http-server-header: Apache/2.4.29 (Ubuntu)
      3306/tcp open  mysql   syn-ack MySQL 5.7.33-0ubuntu0.18.04.1
      | mysql-info: 
      |   Protocol: 10
      |   Version: 5.7.33-0ubuntu0.18.04.1
      |   Thread ID: 7
      |   Capabilities flags: 65535
      |   Some Capabilities: ConnectWithDatabase, DontAllowDatabaseTableColumn, InteractiveClient, SupportsTransactions, FoundRows, ODBCClient, Support41Auth, LongColumnFlag, Speaks41ProtocolOld, IgnoreSigpipes, SwitchToSSLAfterHandshake, Speaks41ProtocolNew, SupportsCompression, IgnoreSpaceBeforeParenthesis, LongPassword, SupportsLoadDataLocal, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
      |   Status: Autocommit
      |   Salt: \x08m\x0FC\x01>*/\x15\x16\x07\x12\x1491WM^\x11\x1F
      |_  Auth Plugin Name: mysql_native_password
      |_ssl-date: TLS randomness does not represent time
      | ssl-cert: Subject: commonName=MySQL_Server_5.7.33_Auto_Generated_Server_Certificate
      | Issuer: commonName=MySQL_Server_5.7.33_Auto_Generated_CA_Certificate
      | Public Key type: rsa
      | Public Key bits: 2048
      | Signature Algorithm: sha256WithRSAEncryption
      | Not valid before: 2021-02-11T23:12:30
      | Not valid after:  2031-02-09T23:12:30
      | MD5:   0b70:1b5f:166e:4269:32e3:01be:40f8:f6e7
      | SHA-1: 2866:e1ef:d280:9bcf:6cec:b15c:27b7:af15:cde1:f92b
      | -----BEGIN CERTIFICATE-----
      | MIIDBzCCAe+gAwIBAgIBAjANBgkqhkiG9w0BAQsFADA8MTowOAYDVQQDDDFNeVNR
      | TF9TZXJ2ZXJfNS43LjMzX0F1dG9fR2VuZXJhdGVkX0NBX0NlcnRpZmljYXRlMB4X
      | DTIxMDIxMTIzMTIzMFoXDTMxMDIwOTIzMTIzMFowQDE+MDwGA1UEAww1TXlTUUxf
      | U2VydmVyXzUuNy4zM19BdXRvX0dlbmVyYXRlZF9TZXJ2ZXJfQ2VydGlmaWNhdGUw
      | ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRCvq9/K5fEQO0juxe6NG4
      | zjV1A5DR/lgWgraEiLmYANxmlN4MY6dy79NnaeCI8fRSjergQIJzFbNWc5mfm6NC
      | E3eaLq2X9eN7+KdR2q7VNjJ/fF3D7k4ewa0GnBNGbC2AyoYrFKXxAN6qGU831qU4
      | aMNcNCAXcJqqF4rW+3Vjlj8h2/ZkYkRJsVUEz5k6esNYRsVPu7JSFkRLE4lV8Xg9
      | vL9arCA9BgR4sE1FqI7mA9DLUcoEZlJXwgl67oad5sxW+GPuZeUF4jF583C8vBhN
      | WRtHWPytjQLe69N8BTthbdabtyQI2HMBEGSEDF6U2AJj8OiC3AXUs3L9p//hL/1p
      | AgMBAAGjEDAOMAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcNAQELBQADggEBAHPpnm2k
      | 2U9nkklYcE0M2LEWyQE8IJozVMLMZ3KvuTF49+eUGXUeEvoJQnOi6P5ELvc57gGY
      | 5QcAdpmqAbdE6vA1jnvK825LCl/L1zpsqXpkj4gu5Znavl2Rs0wXvhGhlj3PlNQu
      | SKoSi+s729CulT6OU+JV9NDIOQlzoSfHCHo02t0D006dnx1ko1J/CtWqFi6mPF8u
      | jqb87kTDBtMPXEO9OKrWKKjxBBQlVAIgu+VAn3TfeEX5moOZO84Uv7ul6GuJ2Xg3
      | J4tSOB1aj0YJcgRXPbYXXf8AgOnMMXv18ZW1x49P5Yro58JyjioZiY7d9bHArRy5
      | nuBjGrsuWRNAqBM=
      |_-----END CERTIFICATE-----
      4444/tcp open  krb524? syn-ack
      5000/tcp open  upnp?   syn-ack

- FFUF's output for `files fuzzing` spots `instructions.txt`

![image](https://github.com/user-attachments/assets/618ba605-03bd-4ac9-b3b0-31ebf984237f)

- FFUF's output for `directory fuzzing` spots directory `whatever` and `hidden`

![image](https://github.com/user-attachments/assets/3c83e8ad-559e-4dc0-bc28-ae4e80a49c10)

- `Instructions.txt` contains creds for a mysql user

![image](https://github.com/user-attachments/assets/1c05aef3-5254-4105-8d1a-6f1fdf902094)

- Directory `whatever` reveals a page for executing shell commands

![image](https://github.com/user-attachments/assets/85c3e1df-bb6e-4d55-bb9e-5891ff77983a)


### Enumerating Mysql

- I access the mysql user with mysql cli binary and checked for dbs with the `show databases` query.

![image](https://github.com/user-attachments/assets/29be8aa6-5043-4fb5-abfa-2d4ccf703eea)

- I logged in again and specified the db `runornot`,I  queried for tables with `show tables;` and reveealed the value of table `run` with `select * from runcheck`.

![image](https://github.com/user-attachments/assets/bae6c735-bcd8-408f-94cc-7498cda31705)

- The run value `0` is being displayed in the whatever index page and if not set to `1` in the db,no user will be able to execute commands.
- I used the `update` statement to set the value of `1` to `0`.

![image](https://github.com/user-attachments/assets/722ae014-c4e1-47bf-ac99-e2e44e51e1dc)

- Now we can execute commands

![image](https://github.com/user-attachments/assets/6102a86a-4766-4416-bea4-fd1d778525ef)

- Shell as `www-data`

![image](https://github.com/user-attachments/assets/e2bf4d21-f711-4ebe-8135-88172ed1ca14)

### Pivoting to user `adam`

- I noticed a weird directory `proct` in directory `/` which contains another directory `pass` with a python script.

![image](https://github.com/user-attachments/assets/4e11232b-3f87-49cd-be40-4bc5d9e200f7)

- The script converts password `wewillROCKYOU` to bytes and use the base64 function `b64encode` to convert it to base64.Then,it is hashed with bcrypt's function `hashpw` and a randomly generated salt.

![image](https://github.com/user-attachments/assets/81683c90-9407-425e-8bf5-9365202243b8)

### Cracking the hash

- The python code contains the hash of adam's password.To crack the hash,we need the salt,if the entire hash is passed to the `hashpw` function,bcrypt automaticaly generates the salt from it.With this flaw,we can just pass a password to it,generate the hash and compare with `adam's hash` to get th right password.In the script, I brute forced with the rockyou wordlist.












