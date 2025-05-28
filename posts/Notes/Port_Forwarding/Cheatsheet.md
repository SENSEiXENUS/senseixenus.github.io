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
- 
