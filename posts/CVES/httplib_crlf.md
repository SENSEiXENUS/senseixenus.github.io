-------------

### Python's cython httplib `set_tunnel` CRLF issue

--------------

- Affected code in http.client._tunnel()-:

```python3
#Line 984
 for header, value in self._tunnel_headers.items():
            headers.append(f"{header}: {value}\r\n".encode("latin-1"))
        headers.append(b"\r\n")
```
- It directly passes headers values without filtering input for \r\n leading to injection of new headers through a header's value.
- Proof-of-concept-:
<img width="1102" height="153" alt="image" src="https://github.com/user-attachments/assets/2fa77f5b-1820-4735-b31f-c052093b8f9b" />

Result-:

