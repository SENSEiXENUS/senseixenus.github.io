---------------

### API RECONNAISSANCE

----------------

### Techniques

----------------

-  Private apis
-  Public apis
-  Partner apis

---------------

- Public apis are easily found and used by end-users.It can be entirely public and meant for authenticated users.Authentication depends on the data offered to end-users.In order to facilitate this, API providers share documentation that serves as an instruction manual for a given API. This documentation should be end-user friendly and relatively straightforward to find.
- Partner apis are created exclusively by the partner of the provider. These might be harder to find if you are not a partner. Partner APIs may be documented, but documentation is often limited to the partner.
- Private apis are limited to the organization.These APIs are often documented less than partner APIS, if at all, and if any documentation exists it is even harder to find.
- API's obvious naming schemes-:

```
/api
/v1
/v2
/v3
/rest
/swagger
/swagger.json
/docs
/doc
/graphql
/graphiql
/altair
/playground
```

- Subdomains are not left out

```
api.target-name.com
uat.target-name.com
dev.target-name.com
developer.target-name.com
test.target-name.com
```

- The use of `Content-Type` headers like `application/xml` and `application/json` can be a good indicator that you've discovered an api
- Or errors in HTTP response headers

```
{"message": "Missing Authorization token"}
```

- Information gathering via third party sources and api directories

[Github](github.com)
[Postman Explore](https://www.postman.com/explore/apis)
[APIS guru](https://apis.guru/)
[Public Apis Github Project](https://github.com/public-apis/public-apis)
[Rapid API Hub](https://rapidapi.com/search/)

----------------

### PASSIVE RECONNAISSANCE

----------------

- Google Dorking-: It is useful if you are getting too many irrelevant result

Queries-:

- `inurl:"/wp-json/wp/v2/users"`<->`Finds all publicly available WordPress API user directories.`
- `intitle:"index.of" intext:"api.txt"` <-> `Finds publicly available API key files`
- `inurl:"/api/v1" intext:"index of /"` <-> `Finds potentially interesting API directories.`
- `ext:php inurl:"api.php?action="` <-> `	Finds all sites with a XenAPI SQL injection vulnerability. (This query was posted in 2016; four years later, there are currently 141,000 results.)`
- `intitle:"index of" api_key OR "api key" OR apiKey -pool` <-> `find exposed api keys`
- 



