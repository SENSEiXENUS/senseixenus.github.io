----------------

### CTF; IRISCTF 2025

----------------

![image](https://github.com/user-attachments/assets/346755b1-758e-4e39-9594-852a137ceae5)

----------------

### CHALLENGES-:

- WEB
  - Password Manager

----------------

### WEB

----------------

### PASSWORD MANAGER

-----------------

![image](https://github.com/user-attachments/assets/46f3199e-06e7-404b-9acd-5f883da93c10)

-----------------

### Important Code Snippets

- Json struct is `{"usr":"<username>","pwd":"<password>"}`

```golang
type Auth struct {
	User     string `json:"usr"`
	Password string `json:"pwd"`
}
```

- Login funtion for route `/login` is seen below.The function validates the login with the `validateLogin` function and creates a cookie if the credentials are correct.

```golang
func login(w http.ResponseWriter, r *http.Request) {
	var auth Auth

	if err := json.NewDecoder(r.Body).Decode(&auth); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte("Invalid request!"))
		return
	}

	if !validateLogin(auth.User, auth.Password) {
		w.WriteHeader(http.StatusUnauthorized)
		w.Write([]byte("Invalid password!"))
		return
	}

	authJson, err := json.Marshal(auth)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		w.Write([]byte("Error occurred! (this should not happen, please open a ticket!)"))
		return
	}

	http.SetCookie(w, &http.Cookie{
		Name:  "auth",
		Value: base64.RawStdEncoding.EncodeToString(authJson),
	})
	w.Write([]byte("{}"))
}
```
- Another important part of the code to note is that all users are stacked in the `users.json` file as seen below.

```golang
// Initialize users var
	file, err := os.Open("./users.json")
	if err != nil {
		fmt.Printf("Error reading users.json: %v\n", err)
		return
	}

	if err := json.NewDecoder(file).Decode(&users); err != nil {
		fmt.Printf("Error reading users.json: %v\n", err)
		return
	}
```

- Lastly, the main sink is seen is this code.

```golang
func pages(w http.ResponseWriter, r *http.Request) {
	// You. Shall. Not. Path traverse!
	path := PathReplacer.Replace(r.URL.Path)

	if path == "/" {
		homepage(w, r)
		return
	}

	if path == "/login" {
		login(w, r)
		return
	}

	if path == "/getpasswords" {
		getpasswords(w, r)
		return
	}

	fullPath := "./pages" + path

	if _, err := os.Stat(fullPath); os.IsNotExist(err) {
		notfound(w, r)
		return
	}

	http.ServeFile(w, r, fullPath)
}
```
