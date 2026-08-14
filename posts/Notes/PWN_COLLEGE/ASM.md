-------------

### ASSEMBLY

--------------

- Common verbs-:

```asm
add (some data together)
sub (subtract)
mul (multiply)
div divide some data
mov move some data into or out of storage
comp (compare two pieces of data together)
test some other properties of data
```

- Registers
 -  CPUs need to ne fast, CPUs need a place to access data
 -  Registers are fast, temporary places to store data
 -  You get several "general purpose" register
   ```asm
    x86: eax,ecx,edx,ebx,esp,ebp,esi,edi
arm: r0 -r14
```
-  The address of the next instruction is in a register-:
```asm
eio(x86), rip(amd64),r15(arm)
```
- Load registers into assembly with `mov`

```
mov rax, 0x539
mov rbx, 1337
```

- 32-bit caveat ( if you write to a 32-bit partial e.g eax, the CPU will zero out the rest from the register.

```asm
mov rax to 0xfffffffffffffffffff
mov eax, 0x539
```

---------------
