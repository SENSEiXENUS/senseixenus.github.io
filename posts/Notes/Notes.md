* * *
NOTES
* * *
### Portforwarding with SSH and proxychains

- Edit the `/etc/proxychains` file and comment `sock4 127.0.0.1 9050` and change sock5's port value to your desired port

- Connect with dynamic portforwarding with ssh

      ssh -l id_rsa -D {proxychains' scok5 port number}

- To scan the internal network with nmap,use

      proxychains nmap 127.0.0.1
