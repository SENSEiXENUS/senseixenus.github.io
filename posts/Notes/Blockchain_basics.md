----------

### Blockchain basics

----------

- What is bitcoin and blockchain? Bitcoin utilizes the blockchain technology.The bitcoin paper authored by `Satoshi Nakamoto` described that Bitcoin will be facilitated by peer to peer transactions over a decentralized networked with cryptography.
- A few years later, Ethereum was created by Vitalik Buterin and others which builds over Blockchain basics with additional capabilities.With Ethereum, you can create decentralized transactions, organizations and agreement without a centralized intermediary and was achieved with smart contracts.`Smart contracts` are a set of instructions executed in a decentralized way without the need for a centralized or third party intermediary.
- Smart contracts functionality is the difference between  `Ethereum` and `Bitcoin`.Technically Bitcoin does have smart contracts but they're intentionally turing incomplete.

----------

### The Smart COntract Problem

----------

- Smart contract face a simillar issue, they cannot interact with data from the real world which is known as the `Oracle Problem`.Blockchain works on data within their ecosystem and to make the compute real world data, real world data are required.
- Oracles serve this purpose. They are devices or services that provide data to blockchains or run external computation. To maintain decentralization, it's necessary to use a decentralized Oracle network rather than relying on a single source. This combination of on-chain logic with off-chain data leads to hybrid smart contracts.

-------------

### Examples of Oracle

-------------

- Chainlink-: is a decentralized Oracle network that allows smart contracts access external data.

-------------

### Layer 2 Solutions

------------

- Layer 2 solutions were created to address issues in blockchain tech.It involves other blockchain hooking into the main blockchain.2 types of L2 Solutions-:
  - Optimistic Rollups-: Optimism, Arbitrum
  - Zero Knowledge ROllups-: Zksync Polygon ZK Evm

------------

### Common Terms

------------

- Blockchain-: Blockchain is a digital ledger that records transaction in decentralized manner across different computers.Each block records all transactions and every new chain is linked to the old chain making it tamper resistant.
- Oracle-: It grants smart contracts access to external data.They act as bridges between the blockchain and the outside world allowing them compute real-world data.
- Layer 2-:These solutions ensures that transactions are done off the main chain and final state is done on the main chain.
- Dapp(Decentralized Application)-: It is an application that runs on a decentralized network e.g the blockchain. It is powered by a smart contract on a decentralized network.Dapps can serve various purposes e.g finance to gaming.A good example is `Uniswap`.
- Smart Contracts-: It is a self-executing agreement with the agreement within the code which is executed as soon as the pre determinined conditions are met, without the need for intermidiaries.
- Hybrid Smart Contracts-: They comine on-chain data and data provided by Oracles.It allows smart contract to interact with data off their chain.e.g A smart contract for insurance data
- Ethereum/EVM  (Ethereum Virtual Machine)-: Ethereum is a blockchain platform known for its smart contract functionality. The Ethereum Virtual Machine (EVM) is its computation engine that executes smart contracts. Ethereum allows developers to build decentralized applications and is the basis for many web3 projects.

------------

### Web3 

-------------

- It is the internet powered by blockchain and smart contracts.nlike the previous versions of the web, web3 is permissionless and relies on decentralized networks rather than centralized servers. This ushers in an era of censorship-resistant and transparent agreements and transactions, often called an ownership economy.

-------------

### The purpose of Smart Contracts

-----------

- Our entire interactions rely solely on contracts which means an agreement between individuals.Normal contracts required trust which can be set aside but not in the case of smart contracts.They are deployed on a decentralized network with visible terms for everyone to see and executed when predetermined terms are set.
- They do this by representing 'promises' as code on the blockchain. This code is executed by a decentralized collective, such that no single entity can alter the agreemeent in any way! The agreement and its terms are public knowledge and will automatically execute without human intervention.
- Although not all platforms are decentralized as claimed, A good example is the `SBF FIX company` which presented itself as a WEB3 company but a web2 one under the hood which used cryptocurrency without smart contracts.


------------

### Features of Smart Contracts

------------

- It contains certain features that distinguishes it from traditonal contracts.Features-:
 - Decentralization-: They do not rely on a central intermediary.Instead, they run on a blockchain managed on thousand of individuals known as node operators which makes it decentralized.
 - Transperency and Flexibility-: It is inherent in blockchain network since node operators can see everything going on.There is no room for unfair or hidden deals. This transparency ensures that everyone has access to the same information and plays by the same rules.Also, transactions are not tied toy our real identity.
 - Security and Immutability-: Once a smart contract is deployed, it cannot be altered or tampered with. This immutability ensures that the terms of the contract are set in stone. This is a stark contrast to centralized systems where a server or database can be hacked, and data can be altered. The decentralized nature of blockchain makes hacking nearly impossible since an attacker would have to take control of more than half the nodes, which is significantly more challenging than compromising a single centralized server.Additionally, the data on a blockchain is resilient. In a traditional system, if your computer and backups fail, you lose all your data. In contrast, in a blockchain, your data is replicated across thousands of nodes. Even if several nodes were to go down, your data would remain secure as long as there is at least one copy of the blockchain.
 - Elimination of Counterparty Risk-: It eliminates the risk of trust in transactions.Once a smart contract is deployed, it cannot be tweaked.None of the parties can tweak it based on greed to ensure it is enforced as intended.

------------

### Application of Smart Contracts

------------

- Defi(Decentralized Finance)-: It allows users to interact with the financial market without a central authority.With smart contracts, users have transparent access to financial markets and can engage with sophisticated financial products efficiently and securely. We will provide practical examples of how to build and interact with DeFi protocols in upcoming lessons.
- DAOs(Decentralized Autonomous Organizations)-:AOs are governed entirely by smart contracts and operate in a decentralized manner. This structure offers benefits such as transparent governance, efficient engagement, and clear rules. DAOs are an evolution in politics and governance
- Non-Fungible Tokens-: They are known as digital art or digital assets.

-----------

### Setting up Testnet on Tenderly

------------

- Visit [Tenderly](https://tenderly.co/?mtm_campaign=partner&mtm_kwd=cyfrin)
- Create account and click on `Virtual Testnet` on dashboard
- Settings-:

![image](https://github.com/user-attachments/assets/92f54036-5a42-4847-82e2-32cc26b7f150)

![image](https://github.com/user-attachments/assets/d822db39-b5fe-4de9-aef0-bd7cca242822)

-----------

### Working  with Testnets

-----------

- To send a token on a testnet, a `faucet` is required to get free tokens.

![image](https://github.com/user-attachments/assets/815bf05b-010f-4e1a-a0af-0372c55f74ed)

- Recommended [faucet](https://faucets.chain.link)
- Understanding Transaction Details
You can view transaction details on [Sepolia Etherscan](https://sepolia.etherscan.io). Important details include:
- Transaction hash: A unique identifier for the transaction.
- Status: Whether the transaction was successful.
- From: The address that sent the transaction.
- To: The address that received the transaction.
- Value: The amount of ETH sent (in this case, 0.1 Test ETH).
 
-----------

### Transaction and Gas Fees

----------

- The transaction fee is the amount rewarded to the block producer for processing the transaction. It is paid in Ether or GWei. The gas price, also defined in either Ether or GWei, is the cost per unit of gas specified for the transaction. The higher the gas price, the greater the chance of the transaction being included in a block.Gas price is not to be confused with gas. While gas refers to the computational effort required to execute the transaction, gas price is the cost per unit of that effort.

------------

### Role of nodes in Blockchain

------------

- Blockchains are run by a group of different nodes, sometimes referred to as miners or validators, depending on the network. These miners get incentivized for running the blockchain by earning a fraction of the native blockchain currency for processing transactions. For instance, Ethereum miners get paid in Ether, while those in Polygon get rewarded in MATIC, the native token of Polygon. This remuneration encourages people to continue running these nodes.
- A gas is a computational complexity unit.The total transaction fee can be calculated by multiplying the gas used with the gas price in Ether (not GWei). Therefore, `Transaction fee = gasPrice * gasUsed`.


-----------

### Blockchain mode of operation

-----------

- Understanding hash functions-: Hash is a fixed length of string that serves to identify a piece of data. Eth uses its own form of hashing algorithm(keccak 256) which belongs to sha256 family.
- Understanding Block-: The blockchain is a collection of "blocks". A `block` is divided into `block`,`nonce` and `data`.All three are then run through the hash algorithm, producing the hash for that block. As a result, even a minor change in the data leads to an entirely different hash, hence, invalidating the block.In essence, mining involves the computational trial and error process of finding an acceptable value to produce a hash which typically follows a certain pattern, such as starting with four zeros. The value found, which satisfies this criterion, is known as the 'nonce'.

-----------

### Inherent immutability 

-----------

- In a blockchain, which is essentially a sequence of blocks, each block is comprised of the previous elements - a block number, a nonce and data - as well as the hash of the previous block.What this means in practice is that any changes to data, in any block of the chain, will invalidate every proceeding block, until they are recalculated, or re-mined.

<img width="1465" height="646" alt="image" src="https://github.com/user-attachments/assets/6abd1680-07b2-47b1-aadd-6442c1b66e94" />

- The first block is known as the `Genesis Block`.

--------------

### Decentralized Distribution

--------------

- Now, if a single entity were to control the blockchain, they could conceivably change any data they want, and then re-mine, or re-validate subsequent blocks. This is bad.The crux of blockchain's power lies in its decentralization or distributed nature. Under this system, multiple entities or "peers" run the blockchain technology, each holding equal weight and power. In the event of disparity between the blockchains run by different peers (due to tampering or otherwise), the majority hash wins, as the majority of the network agrees on it.
- Interplay of transactions in blockchain-: Until now we've been considering the data passed in a block to be a random string of text, but the reality is - this data can be anything. In the token and coinbase sections of this demo you can see how each block is comprised of a number of transactions that all get hashed together. Any edits to any of these transactions is going to invalidate the chain!


--------------

### Public and Private Keys

-------------

- The private key is then passed through an algorithm (the Elliptic Curve Digital Signature Algorithm for Ethereum and Bitcoin) to create the corresponding public key. Both the private and public keys are central to the transaction process. However, while the private key must remain secret, the public key needs to be accessible to everyone.

-------------

### How does transaction signing occur?

--------------

- When we sign a transaction on the blockchain, we're digitally signing some data with our private key. The hashing algorithm used makes it impossible for something to derive your private key from a message signature.
- It is like passing a private key to the blockchain-:

![image](https://github.com/user-attachments/assets/13b15622-b549-4cf1-88e6-8e1c7cd4e29a)

- This signing method allows anyone to verify the validity of a transaction by comparing the message signature to a user's public key!

--------------

