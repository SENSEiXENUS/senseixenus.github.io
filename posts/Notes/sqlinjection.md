------------------

### Exploiting sqlite3

------------------

### Blind SQLite3 exfiltration

-----------------

- The method below is `Boolean based` which is `True` or `False` e.g If a statement is true, return this data and if false, do not return this query.
- This approach will be explained with `BYUCTF` `cooking flask` web challenge.The `tag` query is vulnerable-:

![image](https://github.com/user-attachments/assets/0f4fe54e-c1ed-4e87-a3d1-ccdfc717b127)

- Now let's move over to burp suite to understand the logic.


-----------------

### Counting the amount of tables

------------------

- The count() function in sql is used to count the amount of tables in a database. Digit will be placed after equals to `=`.

```sql
(SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) = {number}
```

-
