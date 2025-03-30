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

- Google Dorking-: It is useful if you are getting too many irrelevant results on Google

Queries-:

- `inurl:"/wp-json/wp/v2/users"`<->`Finds all publicly available WordPress API user directories.`
- `intitle:"index.of" intext:"api.txt"` <-> `Finds publicly available API key files`
- `inurl:"/api/v1" intext:"index of /"` <-> `Finds potentially interesting API directories.`
- `ext:php inurl:"api.php?action="` <-> `	Finds all sites with a XenAPI SQL injection vulnerability. (This query was posted in 2016; four years later, there are currently 141,000 results.)`
- `intitle:"index of" api_key OR "api key" OR apiKey -pool` <-> `find exposed api keys`

- Git Dorking-: Regardless of whether your target performs its own development, it’s worth checking GitHub (www.github.com) for sensitive information disclosure. Developers use GitHub to collaborate on software projects. Searching GitHub for OSINT could reveal your target’s API capabilities, documentation, and secrets, such as API keys, passwords, and tokens, which could prove useful during an attack.
- Examples of GitDorking query-: `filename:swagger.json extension:.json`
- Or search for sensitive string

```
api key
apikeys
api key
authorization: Bearer
access_token
secret
token
API Key exposed
```

- Trufflehog-: TruffleHog is a great tool for automatically discovering exposed secrets. You can simply use the following Docker run to initiate a TruffleHog scan of your target's Github.

Syntax-:` trufflehog git <repo> --results=verified,unknown`

- Shodan-: Shodan is the go-to search engine for devices accessible from the internet. Shodan regularly scans the entire IPv4 address space for systems with open ports and makes their collected information public on https://shodan.io. You can use Shodan to discover external-facing APIs and get information about your target’s open ports, making it useful if you have only an IP address or organization’s name to work from. Like with Google dorks, you can search Shodan casually by entering your target’s domain name or IP addresses; alternatively, you can use search parameters like you would when writing Google queries. The following table shows some useful Shodan queries.

- Queries-:

```
hostname:sensei.com 
"content-type: application/json" <-> filter responses with json body
"content-type: application/xml"  <-> filter responses with xml body
"200 OK"  <-> successful requests
"wp-json"  <-> This will search for web applications using the WordPress API.
```

- The Wayback Machine-: It can be used to find zombie apis[active but retired endpoints that remain unknown to the devs]. Zombie APIs fall under the Improper Assets Management vulnerability on the OWASP API Security Top 10 list. Finding and comparing historical snapshots of API documentation can simplify testing for Improper Assets Management.

----------------

### Active Reconnaissance

----------------

- This form of reconnaissance involves interacting with the actual target.During this process you will be scanning systems, enumerating open ports, and finding ports that have services using HTTP. Once you have found systems hosting HTTP, you can open a web browser and investigate the web application. You could find an API being advertised to end users or you may have to dig deeper. Finally, you can scan the web app for API-related directories.

- Amass-:OWASP Amass is a command-line tool that can map a target’s external network by collecting OSINT from over 55 different sources. You can set it to perform passive or active scans. If you choose the active option, Amass will collect information directly from the target by requesting its certificate information. Otherwise, it collects data from search engines (such as Google, Bing, and HackerOne), SSL certificate sources (such as GoogleCT, Censys, and FacebookCT), search APIs (such as Shodan, AlienVault, Cloudflare, and GitHub), and the web archive Wayback.

- List data sources with `amass enum -list`

![image](https://github.com/user-attachments/assets/850ed4fe-c704-4d99-8784-525a2818faae)

- Create a `config.ini` file

```
curl https://raw.githubusercontent.com/OWASP/Amass/master/examples/config.ini >~/.config/amass/config.ini
```

- API active reconnaissance-:

`amass enum -active -d <target> |grep api`

- Directory busting with `ffuf`

------------------

### Endpoint Analysis

------------------

### Reverse engineering an api with postman and mitmweb

------------------

- Installing `mitmweb`-:

```pwsh
 pip3 install mitmproxy2swagger
 pip3 install mitmweb
```

- It uses the default burp port `8080`.To use mitmweb,close burp suite to use it.
- While connected to the proxy, run `mitm.it` to get the certificate and install it.

![image](https://github.com/user-attachments/assets/e9118525-8157-43e0-b696-a1463bade257)

- Now the requests are getting logged.

![image](https://github.com/user-attachments/assets/c3c461c3-fece-4dee-a7f0-6c07022952be)

- Installing postman-:

------------------


