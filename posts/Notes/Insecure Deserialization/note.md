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
  
