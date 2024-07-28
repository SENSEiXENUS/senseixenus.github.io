* * *
NOTES
* * *
### Portforwarding with SSH and proxychains

- Edit the `/etc/proxychains` file and comment `sock4 127.0.0.1 9050` and change sock5's port value to your desired port

- Connect with dynamic portforwarding with ssh

      ssh -l id_rsa -D {proxychains' sock5 port number}

- To scan the internal network with nmap,use

      proxychains nmap -sT 127.0.0.1

- To local port forward

      sudo ssh -l id_rsa -L {port you want to forwrd through}:127.0.0.1:{remote port discovered}  

### Removing `\r` in `exploitdb` scripts

    sed -i -e 's/\r$//' <script's name>

### Port Forwarding with chisel

- Set up a server with `chisel server -p <port> --reverse` on the attacker machine
- On the client's machine, use `./chisel client [chisel server's ip]:[chisel's server port} R:[port you want it to tunnel through on the server's machine]:127.0.0.1:[internal port running a service on the victim's machine]`

### To replace the root hash by generating a new one

- Use `openssl passwd -6 (password)`
- Clear the root hash in `/etc/shadow` and replace it with your hash, notice the highlighted part

  ![image](https://github.com/user-attachments/assets/8270951c-d313-4bf8-9f28-4ac5a58db988)

   
### Installing adb-tools on Kali Linux[Ubuntu/Debian]

    sudo apt-get install android-sdk-platform-tools

   
