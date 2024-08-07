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

- Testing our little fact by executing \{\{7*7\}\}```,the server returned the value `49`
