----------

### Enumeratimg IAM
### Vulnerable Lab( Cloudgoat)

----------

- Command

```bash
cloudgoat create iam_enum_basics
```
<img width="905" height="201" alt="image" src="https://github.com/user-attachments/assets/a0e9e55d-764c-4581-b84c-bfaac80aec1e" />

- Configure bob creds as provided-:

<img width="880" height="137" alt="image" src="https://github.com/user-attachments/assets/d2108fbe-a5fa-4aca-b002-3f0877856277" />

- Enumerate attached managed policies and read their metadata-:

- User-:

```
aws iam list-users --profile bob | jq
```
<img width="858" height="337" alt="image" src="https://github.com/user-attachments/assets/c25c5a85-0e8e-435d-883e-bc8828c69606" />

- Group-:

```bash
aws iam list-groups --profile bob | jq
```

<img width="1246" height="264" alt="image" src="https://github.com/user-attachments/assets/8bdef635-dec9-42ff-b68b-1fe7eae5e187" />

- Roles-:

```bash
aws iam list-roles --profile bob | jq
```

<img width="914" height="401" alt="image" src="https://github.com/user-attachments/assets/cce2f78e-135d-408c-b535-bddf48b0eb2b" />

- Enumerating groups that a specific user belongs to-:

```bash
aws iam list-groups-for-user --user-name <u> --profile <p>
```

<img width="1203" height="257" alt="image" src="https://github.com/user-attachments/assets/a26bfe3f-1525-42a3-92c3-e731e63efeef" />

- Using query -:

```bash
aws iam list-roles --profile <u> --query "Roles[*].[RoleName,Path]" --output table
```
<img width="1132" height="179" alt="image" src="https://github.com/user-attachments/assets/1622afa8-7379-475e-9122-d2987026cdae" />

> Roles explanation-: Resource Explorer (Resource discovery and indexing)
> AWS SUPPORT: (Enabling Support Related Diagnostics and Indexing)
> Trusted Advisor (Allowing automated health and best practice checks)



