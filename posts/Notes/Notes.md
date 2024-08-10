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


### TERMUX: Adding tmux to your ~/.zlogin to prevent errors

      if [-z "$TMUX"]; then
      exec tmux
      fi
- Explanation: $TMUX vsriable prevents nested tmux instances are started on login shells. `exec` will replace current process with a new one i.e. current shell will be terminated and tmux instance with shell inside will be started, so you won't need to exit twice.
