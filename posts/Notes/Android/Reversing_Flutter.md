-----------

### Reversing Flutter like a noob

-----------

- Dealing with libapp.so
- Dart code runs in an “isolate”, which is a structure which contains a heap, references to objects etc. Isolates are isolated 😏 and can’t access each other, except one special isolate, the “VM” isolate that everybody can access.

- The code is basically in-:

```
_kDartIsolateSnapshotInstruction
```
- Code in `\misc-code\flutter`:

```
https://github.com/cryptax/misc-code.git
```

- Usage-:

```
python3 flutter-header.py -i libapp.so
```

<img width="806" height="175" alt="image" src="https://github.com/user-attachments/assets/cdc978ac-4a60-4c60-8b41-c7dc38c26644" />

- Use blutter-termux-:
```
https://github.com/dedshit/blutter-termux/blob/main/README.md
```
