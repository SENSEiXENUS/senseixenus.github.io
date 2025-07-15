------------

### Feeling funky and decided to learn Insecure Deserialization

------------

- Unserialize under the hood-:
 - Understand with php magic methods-: They are methods with magical properties.The magic methods that are relevant for us now are __wakeup() and __destruct(). If the class of the serialized object implements any method named __wakeup() and __destruct(), these methods will be executed automatically when unserialize() is called on an object.
 - function. __wakeup() reconstructs any resources that the object may have. It is used to reestablish any database connections that have been lost during serialization and perform other reinitialization tasks.
 - The program operates on the object and uses it to perform other actions.
 - Finally, when no reference to the deserialized object instance exists, __destruct() is called to clean up the object.
 - To exploit insecure deserialization, you need to control the application flow by controlling the values passed into automatically executed methods like `__wakeup()` and `__destruct()`.

- Accessing Private Classes-:
  - Vuln code-:

```php
class Example2
{
  private $hook;
  function __construct(){
      // some PHP code...
  }
  function __wakeup(){\
      if (isset($this->hook)) eval($this->hook);
  }
}
// some PHP code...
$user_data = unserialize($_COOKIE['data']);
// some PHP code...
```

- Accessing private fields in php-:

```php
<?php
class Example2
{
  private $hook;
  function __construct(){
      // some PHP code...
  }
  function __wakeup(){
      if (isset($this->hook)) echo eval($this->hook);
  }
}
$example2 = new ReflectionClass('Example2');
$obj = $example2->newInstanceWithoutConstructor();
$prop= $example2->getProperty('hook');
$prop->setAccessible(true);
$prop->setValue($obj,'');
echo base64_encode(serialize($obj));
?>
```

-------------

### PHP POP Chains

--------------

- In a nutshell, when an attacker controls a serialized object that is passed into unserialize(), she can control the properties of the created object. This will then allow her the opportunity to hijack the flow of the application, by controlling the values passed into magic methods like __wakeup().
- Unfortunately, even if the magic methods themselves are not exploitable, an attacker could still wreak havoc using something called POP chains. POP stands for Property Oriented Programming, and the name comes from the fact that the attacker can control all of the properties of the deserialized object. Similar to ROP attacks (Return Oriented Programming), POP chains work by chaining code “gadgets” together to achieve the attacker’s ultimate goal. These “gadgets” are code snippets borrowed from the codebase that the attacker uses to further her goals.

- Pop Chain-:

```php
<?
// some PHP code...
class CodeSnippet{
	private $code = "phpinfo();";
}
class Example {
	private $obj;

	function __construct() {
		$this->obj = new CodeSnippet();
	}
}

echo urlencode(serialize(new Example));
?>
```
--------------

### Core Concepts-:

---------------

- Concept-:

```php
private variables are serialized as \x00ClassName\x00VariableName
protected variables are serialized as \x00*\x00VariableName
public variables are serialized as: VariableName
Classes in PHP are case-insensitive

__sleep() //Triggered before an object is serialized.  
__wakeup()   //Called immediately after an object is deserialized.
From PHP 7.4 onward, if both __unserialize() and __wakeup() exist, only __unserialize() is executed. __wakeup() is ignored.。
__construct() //when an object is created
__destruct() //when an object is destroyed
__toString()： //Runs when an object is used as a string (e.g., echo $object).
__call() //Triggered when calling a non-accessible method in an object context.
__callStatic() //Triggered when calling a non-accessible static method.
__get() //Used to read data from inaccessible properties (either private or non-existent).
__set() //Used to write data to inaccessible properties.
__isset() //Called when isset() or empty() is used on an inaccessible property.
__unset() //Called when unset() is used on an inaccessible property.
__invoke() //Activated when an object is called as a function (e.g., $object()).
```


---------------

### Sauce

--------------

- [Og Vickie li](https://vickieli.dev/insecure%20deserialization/pop-chains/)
- [Chenxi(someOG Chinese Dude)](https://chenxi9981.github.io/php%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/)

-------------
