--------------

### Enumerating Beanstalk

--------------

- Using [PACU](https://github.com/rhinosecuritylabs/pacu)

```bash
#kali
# Kali doesn't have the new updates
pipx install git+https://github.com/RhinoSecurityLabs/pacu.git
```

- Setting up Pacu and set profile-:
  
```bash
#run
pacu
```

<img width="931" height="661" alt="image" src="https://github.com/user-attachments/assets/f43c2c92-9af2-4526-a719-9fb56eb75531" />

- Import keys with `import_keys`-:

```bash
#import keys with import_keys
import_keys profile
```
<img width="621" height="122" alt="image" src="https://github.com/user-attachments/assets/3fb1f79d-012d-4eb4-9ba6-b06dde07d461" />

- Use `search` to search through modules-:

```pacu
search
```

- Using Pacu's `elasticbeanstalk__enum` module-:

```bash
elasticbeanstalk__enum --region us-east-1
```

<img width="1893" height="411" alt="image" src="https://github.com/user-attachments/assets/d10acf20-4d89-48b4-b1cc-a3ae095d3778" />

- Bruteforce for iam permissions with Pacu-:

```
run iam__bruteforce_permissions
```



--------------
