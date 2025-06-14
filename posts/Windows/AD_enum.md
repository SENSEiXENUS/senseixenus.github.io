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

----------------


