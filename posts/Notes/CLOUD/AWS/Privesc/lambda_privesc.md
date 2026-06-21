----------------

### Lambda Privesc

-----------------

- AWS Lambda is a compute service that runs code without the need to manage servers.
- Enumerating roles-:

```bash
aws iam list-role --profile <iq> | jq
```
<img width="1054" height="900" alt="image" src="https://github.com/user-attachments/assets/cb434025-8a59-4e9a-9077-662da0edc215" />

- Enumerating `LambdaManager` shows that the role has full access over lamda:

```bash
aws iam get-policy-version --policy-arn arn:aws:iam::865614241237:policy/cg-lambdaManager-policy-cgid1n6f5si8o5  --version-id v1 --profile lambda_secrets | jq 
```
<img width="1771" height="471" alt="image" src="https://github.com/user-attachments/assets/940a503a-61f1-48dd-91a7-0c96a6c8c129" />

- Enumerating `debug role` shows we have admin access-:

<img width="1527" height="391" alt="image" src="https://github.com/user-attachments/assets/a0d57505-b996-4be4-8955-8dc4ebaeaa6e" />

- Only `LambdaManager` can be assumed-:

<img width="1908" height="390" alt="image" src="https://github.com/user-attachments/assets/6fa87e8e-ebf0-4671-ae50-e80bf22881d9" />




------------------
