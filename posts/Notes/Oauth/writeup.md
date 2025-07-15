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

- 
--------------
