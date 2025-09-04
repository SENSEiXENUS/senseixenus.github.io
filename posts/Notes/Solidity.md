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

- Pure and view functions-:

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

- 

-----------------

