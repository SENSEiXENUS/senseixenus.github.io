-----------------

### Active Directory Enum

-----------------

- External recon-: Gathering data on your target
  - ASN/IP registrars: [iana](https://iana.org),[arin](https://arin.net) for Americas,[ripe](https://www.ripe.net/) for Europe and [BGP toolkit](https://bgp.he.net/)
  - Domain Registrars-: [Domain tools](https://www.domaintools.com/),[PTR Archive](http://ptrarchive.com/) and [ICANN](https://lookup.icann.org/lookup)
  - Social Media-: Linkedin, Facebook, Twitter and News Article
  - Cloud and Dev storage places-: Github dorks, [Grayhatwarfare](https://grayhatwarfare.com/) and Google dorks
  - Breach Data Sources-: [HaveIbeenPwned](https://haveibeenpwned.com/) for breaches and [Dehashed](https://www.dehashed.com/) for corporate mails and passwords.

-------------------

### Initial Enumeration

-------------------

- Gathering hosts
- Wireshark can be used to gather hosts with the syntax below-:

```bash
sudo wireshark -E enss224 -A
```
- Tcpdump-:
```bash
sudo tcpdump -i ens224 
```

- Gather host with `fping`,Fping provides us with a similar capability as the standard ping application in that it utilizes ICMP requests and replies to reach out and interact with a host. 

```bash
fping -asgq 172.16.5.0/23
```

![image](https://github.com/user-attachments/assets/262fbd26-4d41-4f6a-9f40-ea6150894d0f)

- Nmap-:

```bash
sudo nmap -A -iL hosts.txt -oN result2
```

------------------

### Username Enumeration[Internal AD Username enum with Kerbrute]

------------------

- [Wordlist](https://github.com/insidetrust/statistically-likely-usernames) Use `jsmith.txt` and `jsmith2.txt` to brute force it
- Installing `kerbrute` [precompiled releases](https://github.com/ropnop/kerbrute/releases/tag/v1.0.3)

![image](https://github.com/user-attachments/assets/f1a525bf-74e3-4069-8177-1b327405adec)

- Syntax-:

```bash
kerbrute userenum -d <DOMAIN> --dc 172.16.5.5 jsmith.txt -o valid_ad_users
```

![image](https://github.com/user-attachments/assets/7976b616-25f6-4e37-91f6-a71c93d395fb)


----------------

### LLMNR/NBT-NS Poisoning

----------------

- After internal enumeration of the hosts and services, In this phase, we will work through two different techniques side-by-side: network poisoning and password spraying. We will perform these actions with the goal of acquiring valid cleartext credentials for a domain user account, thereby granting us a foothold in the domain to begin the next phase of enumeration from a credentialed standpoint.
- LLMNR-: port 5355
- NBT-NS: 137
- A Man-in-the-Middle attack on Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) broadcasts. Depending on the network, this attack may provide low-privileged or administrative level password hashes that can be cracked offline or even cleartext credentials. Though not covered in this module, these hashes can also sometimes be used to perform an SMB Relay attack to authenticate to a host or multiple hosts in the domain with administrative privileges without having to crack the password hash offline. Let's dive in!Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification that can be used when DNS fails
- LLMNR/NBT-NS can be used for name resolution and this is where responder comes in.We can spoof an authoritative name resolution source ( in this case, a host that's supposed to belong in the network segment ) in the broadcast domain by responding to LLMNR and NBT-NS traffic as if they have an answer for the requesting host.his poisoning effort is done to get the victims to communicate with our system by pretending that our rogue system knows the location of the requested host. If the requested host requires name resolution or authentication actions, we can capture the NetNTLM hash and subject it to an offline brute force attack in an attempt to retrieve the cleartext password. The captured authentication request can also be relayed to access another host or used against a different protocol (such as LDAP) on the same host.
- Quick Explanation-:
  - A host attempts to connect to the print server at \\print01.inlanefreight.local, but accidentally types in \\printer01.inlanefreight.local.
  - The DNS server responds, stating that this host is unknown.
  - The host then broadcasts out to the entire local network asking if anyone knows the location of \\printer01.inlanefreight.local.
  - The attacker (us with Responder running) responds to the host stating that it is the \\printer01.inlanefreight.local that the host is looking for.
  - The host believes this reply and sends an authentication request to the attacker with a username and NTLMv2 password hash.

- Responder-:
```bash
sudo responder -I ens224 
```
![image](https://github.com/user-attachments/assets/30273a69-842a-4b87-bb89-aca45e1d1aef)

- Cracking NTLMv2 hash with hashcat-:

```bash
hashcat -m 5600 forend_ntlmv2 /usr/share/wordlists/rockyou.txt
```
- Use John the Ripper-:

```bash
john --wordlist=[] hash.txt
```

![image](https://github.com/user-attachments/assets/a0c99524-85aa-45d9-958c-c0e4610a4d03)

- 
