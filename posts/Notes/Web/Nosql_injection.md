----------------

### NOSQL Injection

-----------------

- This form of injection is typical to non sql databases e.g mongodb, cypher and others.This will focus more on mongodb.

----------------

- Types-:
  - Syntax injection-: This occurs when you can break the NoSQL query syntax, enabling you to inject your own payload. The methodology is similar to that used in SQL injection. However the nature of the attack varies significantly, as NoSQL databases use a range of query languages, types of query syntax, and different data structures.
  - Operators injection-:  This occurs when you can use NoSQL query operators to manipulate queries.


----------------  

- Operator injection-: NoSQL databases often use query operators, which provide ways to specify conditions that data must meet to be included in the query result.
- Examples-:

| **Operator** |      **Description**        |
|--------------|---------------------|
|$where | Matches documents that satisfy a JavaScript expression.|
|$ne | Matches all values that are not equal to a specified value|
|$in |Matches all of the values specified in an array. |
|$regex | Selects documents where values match a specified regular expression.|
| $nin  | not in an array |

- 
