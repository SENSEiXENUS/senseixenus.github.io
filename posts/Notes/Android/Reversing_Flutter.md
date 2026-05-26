-----------

### Reversing Flutter like a noob

-----------

- Dealing with libapp.so
- Dart code runs in an “isolate”, which is a structure which contains a heap, references to objects etc. Isolates are isolated 😏 and can’t access each other, except one special isolate, the “VM” isolate that everybody can access.

- The code is basically in-:

```
_kDartIsolateSnapshotInstruction
```
- Use blutter-termux-:
```
https://github.com/dedshit/blutter-termux/blob/main/README.md
```
