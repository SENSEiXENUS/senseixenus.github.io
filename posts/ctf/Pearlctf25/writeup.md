------------

### CTF-: Pearl Ctf 2025

-------------

-------------

- Web
  - Tic-tact-toe

---------------

### TIC-TAC-TOE

---------------

![image](https://github.com/user-attachments/assets/3a66e18d-5a07-4e01-8d46-082ac5df5d33)

----------------

- Vulnerability-: SSRF-to-Docker-RCE chain

-----------------

### Source Code-> Analysis for SSRF

-----------------

- app.py-:

```python3
from flask import Flask, render_template, request, jsonify
import requests, json
import url
import subprocess
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def wrap_response(resp):
    try:
        parsed = json.loads(resp)
    except json.JSONDecodeError:
        parsed = resp

    return {"body": parsed}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/deploy")
def deploy():
    container_inspect = subprocess.run(["docker", "inspect", "game"], stdout=subprocess.PIPE)
    resp = json.loads(container_inspect.stdout)
    
    if len(resp) > 0:
        return jsonify({"status": 1})
    
    docker_cmd = ["docker", "run", "--rm", "-d", "-p", "8000:8000", "--name", "game", "b3gul4/tic-tac-toe"]
    subprocess.run(docker_cmd)
    
    return jsonify({"status": 0})

@app.route("/")
def game():
    return render_template("index.html")

@app.post("/")
def play():
    game = url.get_game_url(request.json)
    
    if game["error"]:
        return jsonify({"body": {"error": game["error"]}})
    
    try:
        if game["action"] == "post":
            resp = requests.post(game["url"], json=request.json)
            if resp.status_code < 200 or resp.status_code >= 300:
                logger.debug(resp.text)
                return jsonify({"body": {"error": "there was some error in game server"}})
        else:
            resp = requests.get(game["url"])
            if resp.status_code < 200 or resp.status_code >= 300:
                logger.debug(resp.text)
                return jsonify({"body": {"error": "there was some error in game server"}})
            
    except Exception as e:
        return jsonify({"body": {"error": "game server down"}})
        
    return jsonify(wrap_response(resp.text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```

- `Url.py`-:

```python3
import os

URL = "http://<domain>:<port>/<game_action>"

def is_valid_state(state):
    if len(state) != 9:
        return False
    
    for s in state:
        if s not in ["X", "O", "_"]:
            return False
    
    return True

def get_game_url(req_json):
    try:
        api = req_json["api"]
        keys = list(api.keys())
        
        url = URL.replace("<domain>", os.getenv("GAME_API_DOMAIN"))
        url = url.replace("<port>", os.getenv("GAME_API_PORT"))
        # The game api is going to have many more endpoints in future, I do not want to hardcode the action
        url = url.replace(keys[0], api[keys[0]])
        
        if not is_valid_state(req_json["state"]):
            return {"url": None, "action": None, "error": "Invalid state"}
        
        return {"url": url, "action": req_json["action"], "error": None}
    
    except Exception as e:
        print(e)
        return {"url": None, "action": None, "error": "Internal server error"}
```

- The index route calls function `get_game_url` and pass the json body to create a url.We just need to focus on `get_game_url()` to understand how the url is being created and triggr an ssrf.
The function picks key `api` from the dict and picks the keys from the dict with `keys()` object.Later, the url is replaced with environmental variables which will make the url look like this `http://localhost:8000/<game_action>`.The `<game_action>` will be replaced with the value of the first key.The `json` body must also contain an `action` key which will determine whether the request should `get` or `post` and a state to mimic the `tic-tac-toe` object.The `state` must be a list containing 9 characts[string] and must consist of `X','_' and '0'`.

```python3
import os

URL = "http://<domain>:<port>/<game_action>"

def is_valid_state(state):
    if len(state) != 9:
        return False
    
    for s in state:
        if s not in ["X", "O", "_"]:
            return False
    
    return True

def get_game_url(req_json):
    try:
        api = req_json["api"]
        keys = list(api.keys())
        
        url = URL.replace("<domain>", os.getenv("GAME_API_DOMAIN"))
        url = url.replace("<port>", os.getenv("GAME_API_PORT"))
        # The game api is going to have many more endpoints in future, I do not want to hardcode the action
        url = url.replace(keys[0], api[keys[0]])
        
        if not is_valid_state(req_json["state"]):
            return {"url": None, "action": None, "error": "Invalid state"}
        
        return {"url": url, "action": req_json["action"], "error": None}
    
    except Exception as e:
        print(e)
        return {"url": None, "action": None, "error": "Internal server error"}
```

- I triggered an ssrf by creating an object in this manner because we want the entire url to be replaced with our own url.The url will obviously end be like this `http://localhost:8000/<game_action>` which will be the first key of the api `dict` and it will house our malicious url value.

```json
{"api":{"http://localhost:8000/<game_action>":"http://localhost:2375/container/json"},"state":["X","X","X","X","X","X","X","X","X"],"action":"get"}
```

- Results will only be shown if the status code is between range `200` to `300`.

```python3
try:
        if game["action"] == "post":
            resp = requests.post(game["url"], json=request.json)
            if resp.status_code < 200 or resp.status_code >= 300:
                logger.debug(resp.text)
                return jsonify({"body": {"error": "there was some error in game server"}})
        else:
            resp = requests.get(game["url"])
            if resp.status_code < 200 or resp.status_code >= 300:
                logger.debug(resp.text)
                return jsonify({"body": {"error": "there was some error in game server"}})
            
    except Exception as e:
        return jsonify({"body": {"error": "game server down"}})
        
    return jsonify(wrap_response(resp.text))
```

-------------------------

### Dockerfile Analysis for RCE

-------------------------

- According to the docker file,

