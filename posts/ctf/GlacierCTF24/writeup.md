---------------

### CTF: GLACIER CTF 2024

---------------

![image](https://github.com/user-attachments/assets/cdce91a2-501c-40ed-8017-013608a71987)

---------------

### Challenges

- Web
  - Fuzzybytes

---------------

### Web: Fuzzybytes

![image](https://github.com/user-attachments/assets/bc6606d4-73d5-4934-b393-5305bc210a93)

---------------

### CODE REVIEW

-----------------

- The main sink can be traced with the aid of files `Dockerfile`, `upload.php` and `check_for_malicious_code.py` in the source code archive.
- Dockerfile-:

```docker
# Debian 12
# PHP 8.7.3
# Apache 2.4.59
FROM docker.io/library/php@sha256:b3ff205fcc739fc504750dab29d4c30afb2702730d37a1068a16c14f30a7d48f

RUN apt-get update && apt-get install -y python3 && apt-get clean

# Copy challenge required files
COPY ./config/php.ini $PHP_INI_DIR/php.ini
COPY ./web /var/www/html
COPY ./check_for_malicious_code.py /usr/
COPY ./flag.txt /root/flag.txt

RUN chown www-data:www-data /var/www/html/databases
RUN chmod +s /bin/tar
```

- The docker script copies the content of `web` to `/var/www/html`, copies the python script `check_for_malicious_code.py` to directory `/usr`.

```docker
COPY ./config/php.ini $PHP_INI_DIR/php.ini
COPY ./web /var/www/html
COPY ./check_for_malicious_code.py /usr/
```
- The major ones to note are outlined below,the flag file is copied to `/root/flag.txt` which means we need root privilege to read it.Secondly, ownership of directory `/var/www/html/databases` is granted to user `www-data` and lastly, suid permissions is granted to binary `tar`.

```docker
COPY ./flag.txt /root/flag.txt

RUN chown www-data:www-data /var/www/html/databases
RUN chmod +s /bin/tar
```

