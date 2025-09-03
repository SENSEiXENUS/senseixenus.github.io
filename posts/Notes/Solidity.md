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

--------------

