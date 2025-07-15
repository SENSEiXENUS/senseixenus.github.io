--------------

### Exploiting Oauth 

--------------

### Portswigger Oauth

--------------

-  Oauth is an authorization framework that allows web applications and framework to gain limited access to a user's account on another application.Crucially,OAuth allows access to an account without login credentials.It means that users can finetune what data they can send instead of granting full control to the account.
-  Oauth2.0 was developed as a way for sharing information among applications.It works through a series of interactions between 3 providers i.e client application, resource owner and Oauth service provider.
  -  Client Application-: The application that wants to access user's data
  -  Resource Owner-: The owner which data wants to be accessed.
  -  Oauth Service Provider-: The website or application that control user's data or access to it.They support OAuth by providing an API for interacting with both an authorization server and a resource server.

- Ways that OAuth process can be implemented,They are known as OAuth "flows" and "grant types". In this topic, we'll focus on the "authorization code" and "implicit" grant types as these are by far the most common. Broadly speaking, both of these grant types involve the following stages:
  -  The client application requests access to a subset of the user's data, specifying which grant type they want to use and what kind of access they want.
  -  The user is prompted to log in to the OAuth service and explicitly give their consent for the requested access.
  -  The client application receives a unique access token that proves they have permission from the user to access the requested data. Exactly how this happens varies significantly depending on the grant type.
  -  The client application uses this access token to make API calls fetching the relevant data from the resource server.

--------------

### OAUTH Grant Types

--------------

- It determines the type of sequence taken in OAuth process.They are also known as "OAuth flows".
- The Oauth service must be configured to support a grant type before it can initiate the process.

--------------

### Oauth Scope

-------------

- For any OAuth grant type, the client application has to specify which data it wants to access and what kind of operations it wants to perform. It does this using the `scope` parameter of the authorization request it sends to the OAuth service.
- For basic OAuth, the scopes for which a client application can request access are unique to each OAuth service. As the name of the scope is just an arbitrary text string, the format can vary dramatically between providers. Some even use a full URI as the scope name, similar to a REST API endpoint. For example, when requesting read access to a user's contact list, the scope name might take any of the following forms depending on the OAuth service being used:

```
scope=contacts
scope=contacts.read
scope=contact-list-r
scope=https://oauth-authorization-server.com/auth/scopes/user/contacts.readonly
```
- When Oauth is used for authentication,however, the standardized OpenID Connect scope are often used.For example, the scope `openid profile` will grant the client application read access to a predefined set of basic information about the user, such as their email address, username, and so on.

---------------

### Authorization Code Grant

---------------

- In short, the client application and OAuth service first use redirects to exchange a series of browser-based HTTP requests that initiate the flow. The user is asked whether they consent to the requested access. If they accept, the client application is granted an "authorization code". The client application then exchanges this code with the OAuth service to receive an "access token", which they can use to make API calls to fetch the relevant user data.
- All communication that takes place from the code/token exchange onward is sent server-to-server over a secure, preconfigured back-channel and is, therefore, invisible to the end user. This secure channel is established when the client application first registers with the OAuth service. At this time, a client_secret is also generated, which the client application must use to authenticate itself when sending these server-to-server requests.
- As the most sensitive data (the access token and user data) is not sent via the browser, this grant type is arguably the most secure
  - Authorization Request-: The client application makes a request to the OAuth Service Provider's `/authorization` route specifying the resource it wants to access.It can also be identified based on the parameters used.Example-:

```
GET /authorization?client_id=12345&redirect_uri=https://client-app.com/callback&response_type=code&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1
Host: oauth-authorization-server.com
```

  -


