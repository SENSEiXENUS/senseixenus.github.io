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

- Inheritance way of life in Javascript-:
