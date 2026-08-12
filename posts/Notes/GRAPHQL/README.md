-----------------

### GRAPHQL tricks

-----------------

### Using Curl

------------------

- Syntax-:

```bash
curl https://localhost:5000/api/v1/graphql -H "Content-Type: application/json" -d @introspection.json | jq ".data" | tee schema.json
```

------------------

### Graphql Dorks

-----------------

- FOFA-:

```query
body="GraphQL Server" && title="Graphql"
```

--------------------

### Common list so far

-------------------

- Urls-:

```text
/query
/graphql
```

