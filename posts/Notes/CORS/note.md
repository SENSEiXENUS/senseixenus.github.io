-------------

### Understanding Cross Origin Sharing

-------------

- It is a browser mechanism that grants permission control to a resource outside of a domain.It grants flexibility as against Same-Origin Policy(SOP).It provides potential for cross domain attacks if poorly configured.
- CORS is not a protection against cross-origin attacks such as cross-site request forgery (CSRF).
- Same-Origin policy limits the way a website interact with resources outside its domain.The same-origin policy was defined many years ago in response to potentially malicious cross-domain interactions, such as one website stealing private data from another. It generally allows a domain to issue requests to other domains, but not to access the responses.
- A controlled relaxation of the same-origin policy is possible using cross-origin resource sharing (CORS).The cross-origin resource sharing protocol uses a suite of HTTP headers that define trusted web origins and associated properties such as whether authenticated access is permitted. These are combined in a header exchange between a browser and the cross-origin web site that it is trying to access.

------------

### CORS and Access-Control-Allow-Origin headers

------------

- Access-Control-Allow-Origin response header is included in the response from a website to a requesting website and identifies the permitting origin of the website.

------------

### Implementing simple cross-origin resource sharing

------------

- The cross-origin resource sharing (CORS) specification prescribes header content exchanged between web servers and browsers that restricts origins for web resource requests outside of the origin domain.
- For example, suppose a website with origin normal-website.com causes the following cross-domain request:
```http
GET /data HTTP/1.1
Host: robust-website.com
Origin : https://normal-website.com
```
-  The server on `robust-website.com` will return this response

```http
HTTP/1.1 200 OK
...
Access-Control-Allow-Origin: https://normal-website.com
```

- The browser will allow access to the resource because the `Origin` header matches the `Access-Control-Allow-Origin` specified in the response.The specification of Access-Control-Allow-Origin allows for multiple origins, or the value null, or the wildcard *. However, no browser supports multiple origins and there are restrictions on the use of the wildcard *.Values allowed-:

```
null
*
```

---------------

### Handling Cross Origin request with credentials

--------------

- The default behavior of cross-origin resource requests is for requests to be passed without credentials like cookies and the Authorization header. However, the cross-domain server can permit reading of the response when credentials are passed to it by setting the CORS Access-Control-Allow-Credentials header to true. Now if the requesting website uses JavaScript to declare that it is sending cookies with the request.
- If the website uses javascript to send cookies

```http
GET /data HTTP/1.1
Host: robust-website.com
...
Origin: https://normal-website.com
Cookie: JSESSIONID=<value>
```

- And the response to the request is-:

```http
HTTP/1.1 200 OK
...
Access-Control-Allow-Origin: https://normal-website.com
Access-Control-Allow-Credentials: true
```

- The browser will allow the requesting website to read the response because `Access-Control-Allow-Credentials` is set to `true`.Otherwise, it will not allow the response.


--------------

### Relaxation of CORS with wildcards

-------------

- The `Access-Control-Allow-Origin` allows wildcards `*`.

```http
Access-Control-Allow-Credentials: true
```
- 

-------------
