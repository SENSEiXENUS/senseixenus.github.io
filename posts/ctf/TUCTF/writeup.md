------------

### CTF: TUCTF

------------

![image](https://github.com/user-attachments/assets/0103e628-3780-459b-9e5f-7ed118289138)

------------

### CHALLENGES-:

------------

- Web-:
  - Med Graph

--------------

### Med Graph

------------

![image](https://github.com/user-attachments/assets/74c149e9-855a-4a37-9682-9d271c00af13)

-------------

- After entering the provided creds, I noticed this graphql endpoint in the intercept tab.

![image](https://github.com/user-attachments/assets/cf8e3ed0-28a4-4b84-a15e-b1f75b3ec90f)

- I sent it to repeater and copied an introspection query to the graphql tab to discover the graphql schema of the webpage.

![image](https://github.com/user-attachments/assets/ac24323f-0fd0-4aea-9304-de1d853a32ce)

- Introspection query

```graphql
query IntrospectionQuery {
        __schema {
            queryType {
                name
            }
            mutationType {
                name
            }
            subscriptionType {
                name
            }
            types {
             ...FullType
            }
            directives {
                name
                description
                args {
                    ...InputValue
            }
            }
        }
    }

    fragment FullType on __Type {
        kind
        name
        description
        fields(includeDeprecated: true) {
            name
            description
            args {
                ...InputValue
            }
            type {
                ...TypeRef
            }
            isDeprecated
            deprecationReason
        }
        inputFields {
            ...InputValue
        }
        interfaces {
            ...TypeRef
        }
        enumValues(includeDeprecated: true) {
            name
            description
            isDeprecated
            deprecationReason
        }
        possibleTypes {
            ...TypeRef
        }
    }

    fragment InputValue on __InputValue {
        name
        description
        type {
            ...TypeRef
        }
        defaultValue
    }

    fragment TypeRef on __Type {
        kind
        name
        ofType {
            kind
            name
            ofType {
                kind
                name
                ofType {
                    kind
                    name
                }
            }
        }
    }
```





