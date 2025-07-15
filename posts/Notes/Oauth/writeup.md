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
  - Authorization Request-: The client application makes a request to the OAuth Service Provider's `/authorization` route specifying the specific user's data it wants to access.It can also be identified based on the parameters used.Example-:

```
GET /authorization?client_id=12345&redirect_uri=https://client-app.com/callback&response_type=code&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1
Host: oauth-authorization-server.com
```

  - client_id-: Mandatory parameter containing the unique identifier of the client application. This value is generated when the client application registers with the OAuth service.
  - redirect_uri: The URI to which the user's browser should be redirected when sending the authorization code to the client application. This is also known as the "callback URI" or "callback endpoint". Many OAuth attacks are based on exploiting flaws in the validation of this parameter.
  - response_type:Determines which kind of response the client application is expecting and, therefore, which flow it wants to initiate. For the authorization code grant type, the value should be `code`.
  - scope-: Used to specify which subset of the user's data the client application wants to access.
  - state-:Stores a unique, unguessable value that is tied to the current session on the client application. The OAuth service should return this exact value in the response, along with the authorization code. This parameter serves as a form of CSRF token for the client application by making sure that the request to its /callback endpoint is from the same person who initiated the OAuth flow.
- User Login and Consent-: After receiving thhe authorization request, the user receives a login page from the OAuth server to login their account.They will then be presented with a list of data that the client application wants to access. This is based on the scopes defined in the authorization request. The user can choose whether or not to consent to this access. The first time the user selects "Log in with social media", they will need to manually log in and give their consent, but if they revisit the client application later, they will often be able to log back in with a single click.
- Authorization Code Grant-: If the user consents to the requested access, their browser will be redirected to the /callback endpoint that was specified in the redirect_uri parameter of the authorization request. The resulting GET request will contain the authorization code as a query parameter. Depending on the configuration, it may also send the state parameter with the same value as in the authorization request.

```
GET /callback?code=a1b2c3d4e5f6g7h8&state=ae13d489bd00e3c24 HTTP/1.1
Host: client-app.com
```

- Access Code Request-:Once the client application receives the authorization code, it needs to exchange it for an access token. To do this, it sends a server-to-server POST request to the OAuth service's /token endpoint. All communication from this point on takes place in a secure back-channel and, therefore, cannot usually be observed or controlled by an attacker.

```
POST /token HTTP/1.1
Host: oauth-authorization-server.com
…
client_id=12345&client_secret=SECRET&redirect_uri=https://client-app.com/callback&grant_type=authorization_code&code=a1b2c3d4e5f6g7h8
```
 - client_secret-: The client application must authenticate itself by including the secret key that it was assigned when registering with the OAuth service.
 - grant_type-: Used to make sure the new endpoint knows which grant type the client application wants to use. In this case, this should be set to `authorization_code`.

- Access code grant after validating the request
- API Call-: Now the client application has the access code, it can finally fetch the user's data from the resource server. To do this, it makes an API call to the OAuth service's `/userinfo` endpoint. The access token is submitted in the Authorization: Bearer header to prove that the client application has permission to access this data.
- Resource grant-:The resource server should verify that the token is valid and that it belongs to the current client application. If so, it will respond by sending the requested resource i.e. the user's data based on the scope of the access token.The client application can finally use this data for its intended purpose. In the case of OAuth authentication, it will typically be used as an ID to grant the user an authenticated session, effectively logging them in.

---------------

### Implicit Grant Type

--------------

- Implicit grant type is much simpler and faster.Instead of the authorization code sequence,the Oauth service provider sends the the access code after the user login and consents to the scope.
- This method is not widely used because it is done through browser redirects and not server side back channel communication.This means the client_secret and sensitive access_token is shared.The implicit grant type is more suited to single-page applications and native desktop applications, which cannot easily store the client_secret on the back-end, and therefore, don't benefit as much from using the authorization code grant type.

-------------

### Stages

-------------

- Authorization request-: The implicit flow starts in much the same way as the authorization code flow. The only major difference is that the `response_type` parameter must be set to token.

```
GET /authorization?client_id=12345&redirect_uri=https://client-app.com/callback&response_type=token&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1
Host: oauth-authorization-server.com
```

- User login and consent-: The user logs in and decides whether to consent to the requested permissions or not. This process is exactly the same as for the authorization code flow.
- Access Token Grant-: If the user gives their consent to the requested access, this is where things start to differ. The OAuth service will redirect the user's browser to the redirect_uri specified in the authorization request. However, instead of sending a query parameter containing an authorization code, it will send the access token and other token-specific data as a URL fragment.As the access token is sent in a URL fragment, it is never sent directly to the client application. Instead, the client application must use a suitable script to extract the fragment and store it.

```
GET /callback#access_token=z0y9x8w7v6u5&token_type=Bearer&expires_in=5000&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1
Host: client-app.com
```
- API Call-: Once the client application has successfully extracted the access token from the URL fragment, it can use it to make API calls to the OAuth service's /userinfo endpoint. Unlike in the authorization code flow, this also happens via the browser.

```
GET /userinfo HTTP/1.1
Host: oauth-resource-server.com
Authorization: Bearer z0y9x8w7v6u5
```
- Resoure grant-: The resource server should verify that the token is valid and that it belongs to the current client application. If so, it will respond by sending the requested resource i.e. the user's data based on the scope associated with the access token.





