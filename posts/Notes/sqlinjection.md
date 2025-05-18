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

- The count() function in sql is used to count the amount of tables in a database. Digit will be placed after equals to `=`.

```sql
(SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) = {number}
```

-
