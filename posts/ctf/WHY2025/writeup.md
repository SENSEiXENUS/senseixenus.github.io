-------------------

### CTF: WHY2025 CTF

-------------------

![image](https://github.com/user-attachments/assets/5d7b39c1-2e1f-48da-a494-f818560ea6d0)

-------------------

### CHALLENGES-:

-------------------

- Web-:
  - Planets
  - Festival

-------------------

### PLANETS

-------------------

![image](https://github.com/user-attachments/assets/f1fb9132-28d3-4135-a6d5-9385277c245d)

------------------

- Source Code as seen with view-source-:

```js
try {
            fetch("/api.php", {
                method: "POST",
                body: "query=SELECT * FROM planets",
                headers: {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"},
            })
            .then(response => response.json())
            .then(response => addPlanets(response))
        } catch (error) {
            console.error(error.message);
        }
```

- The code above is a js ajax request  making a post request to php page `/api.php`.The interesting part is the body which contains sql query sent to the server.We can manipulate the input to read other data from the database.

```js
 body: "query=SELECT * FROM planets"
```

- I made a query to check for other tables with `SHOW TABLES`.We have an interesting rresult `abandoned_planets`.

![image](https://github.com/user-attachments/assets/0153717f-8f47-4652-ad06-918200fe2a6e)

- The next step is to read the columns with `select * from abandoned_planets`.I got the flag with that statement.

![image](https://github.com/user-attachments/assets/17fc2858-fec1-4bf2-a46b-1ac5fe0ef5a1)

- Flag-:`flag{54de9e7dbee502cdc153cec4e0abfb38}`

----------------------

### FESTIVALS

-----------------------

![image](https://github.com/user-attachments/assets/4c2dc171-a7bc-44cb-a0d2-5d9e977649ad)

-----------------------

- This target uses the graphl language but it is vulnerable to XPATH injection which is a vulnerability that affect websites that use `XPATH` to interact with `XML databases`.The exploitation aspect focuses on xpath injection in graphql.
- I spotted the vulnerability with the error `Invalid Predicate` in the result.This StackOverflow [post](https://stackoverflow.com/questions/33830821/python-xpath-syntaxerror-invalid-predicate) associated the error to XPATH.

![image](https://github.com/user-attachments/assets/f9a7a19c-4d5a-491d-b990-bc265e2200b1)

- I followed this [blogpost](https://www.vaadata.com/blog/xpath-injections-exploitations-and-security-tips/) to exploit the vulnerability but I modified the code slightly to exploit the target.
- XPATH is like sql injection and the backend react differently to `TRUE` or `False` statements.In the case of a `TRUE` statement,we get the data related to id `1`.

![image](https://github.com/user-attachments/assets/f60082cd-397d-4787-9006-b73feb7112a5)

- But, in a false statement,we get none.

![image](https://github.com/user-attachments/assets/4a8da922-7e7d-442f-bb98-6e78953612ce)

- This target is vulnerable to `XPATH blind injection`,we'll have to exfiltrate data based on `TRUE` and `FALSE` statemeent.In our case, if the statement is true,we get the data of id `1` but if it is false,we get none.
- In Xpath,we have the root node and other child nodes e.g `/root/` -> `[root node]`,`/root/mead/` ->`[Meager is the child node]`.The firsst step is to find the string-length of the root node with the query below.It is done with the string-length() function.Value 3 should be iterated.

```xpath
string-length(name(/*[1]))=3
```
- I wrote a POC for it.

![image](https://github.com/user-attachments/assets/4cae27fb-b329-432c-a8b7-b1134612e19f)

- The root-node has 4 characters-:

![image](https://github.com/user-attachments/assets/c93f9376-0cda-4a57-9d5d-0282ecfe4ae2)

- The next step is to read the characters with this function `substring()`.The char `d` should be replaced with characters.

```xpath
substring(name(/*[1]), 1, 1)=’d‘
```

- POC-:

![image](https://github.com/user-attachments/assets/8082e0ef-8b91-4111-9139-7b259fe854de)

- Result is `data`-:

![image](https://github.com/user-attachments/assets/11f15086-29fe-4296-9dfb-42160414a1a0)

- The next step is to count the amount of child_nodes with `count()` function.

```xpath
count(/[root node]/*)=2
```
- Count Nodes POC-:

![image](https://github.com/user-attachments/assets/890c0543-d525-4f11-8741-45a69c3ab399)

- 2 child nodes-:

![image](https://github.com/user-attachments/assets/9bf047e6-7d08-4bd7-9eaa-245b5bce01e7)

- After getting the child nodes,the next step requires reading a text node which contains a text string. It can be achieved with the  `substring()` but without the `name()` function because it can only be used to read child and root nodes.This should be the new syntax to get the string length-:

```xpath
string-length(/data/products/product[1])=4
```

- Read chars with-:

```xpath
substring(/data/ctf_s3cr3ts/secret_value_8761[1], 1, position[int])
```

- Flag-: ` flag{f16ceec239b54aec5e74c87c4c302a12}`

![image](https://github.com/user-attachments/assets/524b7689-774c-4e76-a230-5d2071034727)





