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

- 
- 
