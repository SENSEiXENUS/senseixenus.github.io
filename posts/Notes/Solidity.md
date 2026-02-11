-------------

### Solidity Basics

-------------

- Installing solcjs

```bash
sudo npm install --global solc
```

- Specifying the version

```sol
//version
pragma solidity 0.8.30; //use only 0.8.30
//use versions between 0.8.19 and 0.9.0 (excluded)
pragma solidity ^0.8.19;
pragma solidity >=0.8.19 <0.9.0;
```
- SPDX License Identifier, use
```sol
//SPDX-License-Identifier: MIT
//solidity version
pragma solidity ^0.8.30;
```

- Running with `solcjs`-:

```bash
solcjs --bin main.sol
```
![image](https://github.com/user-attachments/assets/d14f8c95-e6a8-442d-94ec-f2d99164bdbc)

- Code-:

```sol
//SPDX-License-Identifier: MIT
//solidity version
pragma solidity ^0.8.30;

contract simpleStorage {
    //code goes thus
}
```
- Bool-:

```sol
bool hasFavoriteNumber = true; //true or false
```
- Basic types-:

```sol
   bool hasFavoriteNumber = true;
    uint256 favoriteNumber = 88;
    string favoriteNumberInText = "eighty-eight";
    int256 favoriteInt = -88;
    address myAddress = 0xAB1b7206aa6840C795aB7A6AE8b15417B7E63A8D;
    bytes32 favoriteBytes32 = "cat";
```

- create a function with `function`-:

```sol
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.1;

contract Storage{
    uint256 digit = 100;
    function store(uint256 _digit) public {
        digit = _digit;
    }
}
```

-  Appending the public keyword next to a variable will automatically change its visibility and it will generate a getter function (a function that gets the variable's value when called).

```sol
uint256 public digit = 1000;
```

- Visibility for variables and function-:

```
public
private
internal
external
```

- Pure and view functions,-:

```sol
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.1;

contract Storage{
    uint256 digit = 100;
    function store(uint256 _digit) public {
        digit = _digit;
    }
    //view
    function retrieve() public view returns {
        return digit;
    }
    //pure
    function retrieve() public pure returns {
        return 7;
    }
}
```
- To store function in memory, use `memory` -:

```solidity
function createZombie(string memory _name,uint _dna) public {

}
```
- Return a value in a function with `return`, specify like this

```solidity
string greeting = "What's up dog";

function sayHello() public returns (string memory) {
  return greeting;
}
```

- Function modifiers
- The below function doesn't actually change state in solidity e.g it doesn't chnage values or write anything.It is set with `view`

```solidity
function sayHello() public view returns (string memory){
}
```
- Solidity also contains pure functions meaning you are not accessing any data fron the app e.g

```solidity
function _multiplyNumbers(uint a, uint b) private pure returns (uint memory) {
  return a * b;
}
```
- 
 
--------------

### Arrays and Structs

--------------

- Creating a list of `uint256` numbers-:

```
uint256[] digits = [0,10,90];
```

- The issue with this data structure above is that we cannot link the owner with its favorite value. One solution is to establish a new type using the struct keyword, named Person, which is made of two attributes: a favorite number and a name.

```sol
struct Person {
   string name;
   uint256 age;
}
```
- Using it-:

 ```sol
Person public ade = Person("Ade",100);
```
- Array of struct-: Creating individual variables that represent several people might become a tedious task, due to the repetitive steps of the process. Instead of manually instantiating a variable for each person, we can combine the two concepts we just learned about: arrays and structs.

```sol
Person[] public people;
Person[3] public three_people;
```

- Pushing new values to an `array of structs` with a function.

```sol
//function push to three_people array
    function push_value(uint256 _negativeNumber, string memory _name) public{
        people.push(Person(_negativeNumber,_name));
  }
```

-------------

### Memory Storage

---------------

- How does solidity handle data storage? It uses locations like this-:

```
Calldata
Memory
Storage
Stack
Code
Logs
```

- `Calldata` and `memory` are temporary storage locations during function execution.calldata is read-only, used for function inputs that can't be modified. In contrast, memory allows for read-write access, letting variables be changed within the function. To modify calldata variables, they must first be loaded into memory.
- Memory-:

```sol
string memory name = "Ade";
```
-----------------

### Keccak256 and Typecasting

-----------------

- Ethereum's `keccak256` is the version of `SHA3`.It maps an input into a 256-bit hexadecimal number.It expects a parameter of type `bytes`.It means we have to pack `string` to `bytes`.

```solidity
keccak256(abi.encodePacked("deadbeef"))
```

-  Typecasting involves converting between data types.For example-:

```solidity

uint a = 6;
uint8 b = 9;

uint8 c = b * uint8(a);
```
-------------------

### Events
--------------------

- Events are a way for your contract to communicate that something happened on the blockchain to your app front-end, which can be 'listening' for certain events and take action when they happen.

```solidity
// declare the event
event IntegersAdded(uint x, uint y, uint result);

function add(uint _x, uint _y) public returns (uint) {
  uint result = _x + _y;
  // fire an event to let the app know the function was called:
  emit IntegersAdded(_x, _y, result);
  return result;
}
```

- Javascript implementation-:

```js
YourContract.IntegersAdded(function(error, result) {
  // do something with the result
})
```
- Status (chapter 15)-:

```solidity
pragma solidity >=0.5.0 <0.6.0;

contract ZombieFactory {

    event NewZombie(uint zombieId,string name,uint dna);
    
    uint dnaDigits = 16;
    uint dnaModulus = 10 ** dnaDigits;

    struct Zombie {
        string name;
        uint dna;
    }

    Zombie[] public zombies;

    function _createZombie(string memory _name, uint _dna) private {
        uint id = zombies.push(Zombie(_name, _dna)) - 1; // 2. Store the result of `zombies.push(...) - 1` in a `uint` called `id`
        emit NewZombie(id, _name, _dna);
    }

    function _generateRandomDna(string memory _str) private view returns (uint) {
        uint rand = uint(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }

    function createRandomZombie(string memory _name) public {
        uint randDna = _generateRandomDna(_name);
        _createZombie(_name, randDna);
    }

}
```

------------------

### Intermediate Solidity

--------------------

- New data types `mapping` and `address`
- Each account has an `address` which you can think of as a bank account which looks like this `0x0cE446255506E92DF41614C46F1d6df9Cc969183`. Mappings are another way of storing data
- A mapping might look like this-:

```solidity
mapping (address => uint) public accountBalance;
mapping (uint => string ) userIdToName;
```

-  It is typically a key-value pair for storing and looking up data.

---------------------

### Msg.sender

---------------------

- There are certain global functions available to all functions. One of them is `msg.sender` which belongs to the address of the person that called a function in a contract.

>Note: In Solidity, function execution always needs to start with an external caller. A contract will just sit on the blockchain doing nothing until someone calls one of its functions. So there will always be a msg.sender.

- Example-:

```solidity
mapping (address => uint ) public contractAddresses;

function setAddressValue(uint memory _number) public {
    contractAddresses[msg.sender] = _number;
}
```

- Increasing counter in solidity-:

```sol
uint number = 0;
number++;
```

- `Require` is used to ensure a line of code throws an error if the condition is not fulfilled.

```solidity
require(abi.encodePacked('a') == abi.encodePacked('b'));
```
-------------

### Inheritance

--------------

- Inheritance prevents a long contract by breaking it into several contracts inheriting attributes from the each other.Example-:

```solidity
contract Doge {
}
//is extends a subclass to base class
contract baseDoge is Doge {

}
```
- Importing a contract from another file, use-:

```solidity

import "./someContract.sol"

contract Doge is someContract {
}
```

-  `Storage v Memory` data location-:
-  `Storage` data are stored on the blockchain while `Memory` values are stored in the `RAM` or the `hard-disk`.
-  Although, you don't need to specify for `storage` because state variables are stored in it by default and permanently written to the blockchain, while variables stored in function are stored in the `memory` and disappears after a function gets called.

```solidity
function feedAndMultiply(uint _zombieId, uint _targetDna) public {
    require(msg.sender == zombieToOwner[_zombieId]);
    Zombie storage myZombie = zombies[_zombieId];
    // start here
  }
```
- Access a struct's data with `struct.key`.e.g

```
myZombie.dna
```
-
---------------
