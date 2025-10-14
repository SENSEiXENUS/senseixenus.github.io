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

