-----------

### Introduction to AD

------------

- Active Directory (AD) is a directory service for Windows network environments. It is a distributed, hierarchical structure that allows for centralized management of an organization's resources, including users, computers, groups, network devices, file shares, group policies, devices, and trusts.AD provides authentication and authorization functions within a Windows domain environment.
- AD is essentially a sizeable read-only database accessible to all users within the domain, regardless of their privilege level. A basic AD user account with no added privileges can enumerate most objects within AD. This fact makes it extremely important to properly secure an AD implementation because ANY user account, regardless of their privilege level, can be used to enumerate the domain and hunt for misconfigurations and flaws thoroughly. Also, multiple attacks can be performed with only a standard domain user account, showing the importance of a defense-in-depth strategy and careful planning focusing on security and hardening AD, network segmentation, and least privilege.
- A directory service such as Active Directory Domain Services(AD DS) gives an organization ways to store directory data and make it available to both standard users and administrators on the same network.AD DS stores information such as usernames and passwords and manages the rights needed for authorized users to access this information. It was first shipped with Windows Server 2000; it has come under increasing attack in recent years. It is designed to be backward-compatible, and many features are arguably not "secure by default." It is difficult to manage properly, especially in large environments where it can be easily misconfigured.
- Active Directory flaws and misconfigurations can often be used to obtain a foothold (internal access), move laterally and vertically within a network, and gain unauthorized access to protected resources such as databases, file shares, source code, and more.
- AD is arranged in hierarchical structure with the `forest` at the top with a number of `domains` which in turn can contain `nested subdomains`.A domain is a structure within which objects( users,computers and groups) are accessible.It has many built-in Organizational Units (OUs), such as Domain Controllers, Users, Computers, and new OUs can be created as required. OUs may contain objects and sub-OUs, allowing for the assignment of different group policies.
- Example-:

```
INLANEFREIGHT.LOCAL/
├── ADMIN.INLANEFREIGHT.LOCAL
│   ├── GPOs
│   └── OU
│       └── EMPLOYEES
│           ├── COMPUTERS
│           │   └── FILE01
│           ├── GROUPS
│           │   └── HQ Staff
│           └── USERS
│               └── barbara.jones
├── CORP.INLANEFREIGHT.LOCAL
└── DEV.INLANEFREIGHT.LOCAL
```

- Here we could say that INLANEFREIGHT.LOCAL is the root domain and contains the subdomains (either child or tree root domains) ADMIN.INLANEFREIGHT.LOCAL, CORP.INLANEFREIGHT.LOCAL, and DEV.INLANEFREIGHT.LOCAL as well as the other objects that make up a domain such as users, groups, computers, and more as we will see in detail below. It is common to see multiple domains (or forests) linked together via trust relationships in organizations that perform a lot of acquisitions. It is often quicker and easier to create a trust relationship with another domain/forest than recreate all new users in the current domain.
- 
