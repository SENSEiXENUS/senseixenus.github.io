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

![image](https://github.com/user-attachments/assets/caa7ddbe-8696-4547-8d1e-6be5c31ff80a)

- Responder logs are stored in `/usr/share/responder/logs`-:

![image](https://github.com/user-attachments/assets/e0045ce3-c707-44b1-90c0-156ca1e9b165)

--------------

### Exploitng LLMNR/NBT-NS attacks with Inveigh.exe on windows

-------------

- [Inveigh](https://github.com/Kevin-Robertson/Inveigh)-: If we end up with a Windows host as our attack box, our client provides us with a Windows box to test from, or we land on a Windows host as a local admin via another attack method and would like to look to further our access, the tool Inveigh works similar to Responder, but is written in PowerShell and C#. Inveigh can listen to IPv4 and IPv6 and several other protocols, including LLMNR, DNS, mDNS, NBNS, DHCPv6, ICMPv6, HTTP, HTTPS, SMB, LDAP, WebDAV, and Proxy Auth.
- Let's start Inveigh with LLMNR and NBNS spoofing, and output to the console and write to a file.Don't forget to run as adminstrator `powershell start powershell -v runAs`.Using Inveigh-:

```powershell
Invoke-Module .\Inveigh.ps1
Invoke-Inveigh Y -NBNS Y -ConsoleOutput Y -FileOutput Y
```
![image](https://github.com/user-attachments/assets/56b17304-f7db-49e0-93a7-ba3c29d4996e)
- Captured Hashes-:

![image](https://github.com/user-attachments/assets/211c8faf-8c75-4c48-8d5c-1b475598d6e1)


- C# Inveigh Zero-:
- Usage-:
```powershell
.\Inveigh.exe
```
- We can hit the esc key to enter the console while Inveigh is running.

![image](https://github.com/user-attachments/assets/5274c331-3afc-4f79-a58a-26e952918efa)

- Hit "help" for several options-:

![image](https://github.com/user-attachments/assets/c119c284-9260-4473-a2a7-ee28272352a8)

- We can quickly view unique captured hashes by typing `GET NTLMV2UNIQUE`.

![image](https://github.com/user-attachments/assets/52644780-7bab-4de7-8936-bad04d34d94b)![image](https://github.com/user-attachments/assets/3d593408-ec58-423d-a39f-1fd1063b8261)

- We can type in `GET NTLMV2USERNAMES` and see which usernames we have collected.

---------------

### Using ldap-search

----------------

- To filter objects, use -W "objectClass="

```bash
ldapsearch -x -H ldap://[ip] -b 'dc=support,dc=htb' -D "support\ldap" -W 'objectClass=user'
```

- All objects, use -W "objectClass=*"

![image](https://github.com/user-attachments/assets/4ad995ae-a820-4520-a17d-8c5c68fe8abe)

- Users in the directory -: `objectClass=user`

```bash
ldapsearch -x -H ldap://[ip] -b 'dc=support,dc=htb' -D "support\ldap" -W 'objectClass=user'
```

- Using ldapsearch with password stored in a file.I used `-n` to prevent newline in text file.Use `-y` to specify passwd file.

```bash
ldapsearch -x -H ldap://support.htb -b 'dc=support,dc=htb' -D "support\ldap" -W 'objectClass=user' -y passwd
```

```
echo -n "password" > passwd
chmod 600 passwd
```

![image](https://github.com/user-attachments/assets/966f7ace-f31a-49d7-bbdc-b9f715219953)

- Finding the user without -W "filter" -:

```bash
ldapsearch -x -H ldap://support.htb -b 'cn=support,cn=users,dc=support,dc=htb' -D "support\ldap" '(objectClass=user)' -y passwd
```
![image](https://github.com/user-attachments/assets/9472fa1e-9422-4dde-b5fe-ba2d4e2d46f0)

- Groups-:

```bash
ldapsearch -x -H ldap://support.htb -b 'dc=support,dc=htb' -D "support\ldap" '(objectClass=group)'
```

- Computer Accounts-:

```bash
ldapsearch -x -H ldap://support.htb -b 'dc=support,dc=htb' -D "support\ldap" '(objectClass=computer)' -y passwd
```

- Users of a group-:

```bash
ldapsearch -x -H ldap://support.htb -b 'dc=support,dc=htb' -D "support\ldap" '(sAMAccountName=*)' -y passwd
```

--------------

### Using Bloodhound-ce

---------------

- [Installation](https://github.com/dirkjanm/BloodHound.py)-:

```bash
pip install bloodhound-ce #community edition
pip install bloodhound #legaacy version
#same syntax tho
```
- Usage`[-c -> 'all']`-:

```
bloodhound-ce-python -u [user@domain] -p '[password]' -ns [nameserver / IP] -d [domain] -c [collection method]
```

![image](https://github.com/user-attachments/assets/902b2934-ae9d-4012-8876-e255d3a38626)

- Collector for [Bloodhound 4.3.1](https://github.com/SpecterOps/BloodHound-Legacy/blob/master/Collectors/SharpHound.exe)

![image](https://github.com/user-attachments/assets/b78f5f72-6f3a-4e63-9d1b-23630909ff07)

- 




