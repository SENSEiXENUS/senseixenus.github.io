-----------------

### Reverse

-----------------

- Reverse engineering, also called backwards engineering or back engineering, is the process by which an artificial object is deconstructed to reveal its designs, architecture, code, or to extract knowledge from the object.

-------------------

### x86 architecture

-------------------

- The aim of reverse engineering is to understand modern  malware analysis.
- Techniques of Malware analysis-:
  - Static analysis
  - Dynamic analysis

- Static analysis uses software tools to examine ececutables without running the decompiled instructions in Assembly.
- Dynamic analysis uses disassemblers and debuggers to disassemble code without actually running them.The most popular tool in the market today is called IDA which is a multi-platform, multi-processor disassembler and debugger. There are other disassembler/debugger tools as well on the market today such as Hopper Disassembler, OllyDbg and many more.

-------------------

### Types of Malware

--------------------

- Categories of Malware-:
 - Backdoor-: It is a malicious code embedded in a computer to allow remote access with little or no power to execute commands on a computer.
 - A botnet allows an attacker access to a system however receive instructions not from one remote attacker but from a command-and-control server to which can control an unlimited amount of computers at the same time.
 - A downloader is nothing more than malicious code that has only one purpose which is to install other malicious software. Downloaders are frequently installed when a hacker gains access to a system initially. The downloader then installs additional software to control the system.

 -------------------

 ### X86 Assembly intro

 --------------------

- What is X86 Assembly Language? It is a family of backward-compatible Assembly language that provide backward compatibility to the Intel 8000 series of microprocessors.
- It is used to provide object code to the processors above.
- X86 Assembly Language has the two choices of syntax.The AT&T syntax was dominant in the Unix world since the OS was developed at AT&T Bell Labs. In contrast, the Intel syntax was originally used for the documentation of the x86 platform and was dominant in the MS-DOS and Windows environments.
For our purposes, when we are ultimately disassembling or debugging software, whether it be in a Linux or Windows environment, we will see the Intel syntax in large measure. This is essential whether we are examining a Windows binary in PE format or a Linux binary in ELF format. More on that later in this tutorial.
- We will also focus on a 32-bit architecture as ultimately most malware will be written for such in order to infect as many systems as possible. 32-bit applications/malware will work on 64-bit systems so we want to understand the basics of the 32-bit world.

------------------

### Learning the Binary System

------------------

- Binary numbers are what define the core of a computer. A bit within a computer is either on or off. A bit has either electricity turned on to it or it is absent of such.
- Understanding the numbering system
- In binary,each number is a bit,if we combine 8 bits,it is a byte.A byte can be divided into 4 top bits and 4 lower bits.4 bits is a nibble,Since 4 bits gives you the possible range from 0 - 15 a base 16 number system is easier to work with. Keep in mind when we say base 16 we start with 0 and therefore 0 - 15 is 16 different numbers.This exciting number system is called hexadecimal. The reason why we use this number system is that in x86 Assembly it is much easier to express binary number representations in hexadecimal than it is in any other numbering system.

- Hex chart-:

![image](https://github.com/user-attachments/assets/f529ed1e-a54f-42c6-97e7-1f496fbc1556)

---------------

### Examining 42 in decimal

- 42
```python3
>>> 2*10**0 + 4*10**1
42
```
- In hexadecimal, everything will be treated with `base 16`.Converting "2a" based on the number charts, 10 is `a` in hexadecimal while `2` is `2` in hexadecimal.Number has to be converted first in decimal.

```python3
>>> 10*16**0 + 2*16**1
42
```
- "F5" in hexadecimal to decimal-:

```python3
>>> 5*16**0+15*16**1
245
>>>
```
- `F1CD` to decimal-:

```python3
>>> 13*16**0 + 12*16**1 + 1*16**2 + 15*16**3
61901
>>>
```

- 

----------------

### Transistors and Memory

-----------------

- Electronic computers are simply made out of transistor switches. Transistors are microscopic crystals of silicon that use electrical properties of silicon to act as switches. Modern computers have what are referred to as field-effect transistors.

- The presence of voltage indicates a binary 1 and the absence of voltage indicates a binary 0 therefore the memory cell holds one binary digit or bit which is either 1 or 0 meaning on or off.
- Bytes,Word and Double word-:
- Memory is measured in bytes.A byte is `8 bits`.Two bytes are a called `a word` and two words are called a `double word` which 4 bytes(32 bit).Quad word is `4 words` and equal to `64 bits`.A byte is 8 bits and is 2^8 power which is 256. The number of binary numbers 8 bits in size is one of 256 values starting at 0 and going to 255.4 bits is a nibble.
- A digit in hexadecimal is 4 bits long which is a `nibble`.If we look at `40`,it is 8 bits long which is a byte.If we look at d040, we have two bytes or a word in length. Finally, ffffd040 is a double word or 4 bytes in length which is 32-bits long.he 0x at the beginning of the address just designates that is is a hexadecimal value.
- A computer program is no more than a machine code stored in a memory.A 32-bit CPU grabs a double word(4 bytes) from a memory address.4 bytes is loaded from a memory and loaded into a CPU.As soon as it finishes executing, the CPU fetches the next machine instruction in memory from the instruction pointer.

-------------------

### X86 Architecture

--------------------

- A computer program is a set of instructions stored in memory to which the binary numbers that they are made up are unique to the way the cpu decides them.A basic architecture is made up of CPU,memory and I/O (Input/Output) devices connected by a system bus.

![image](https://github.com/user-attachments/assets/018a8411-a2d1-4081-9635-250df9d993fb)

- CPU consist of 4 parts-:
  - Control-Unit-: Retrieves and decodes instructions from the CPU and then storing and retrieving them to and from memory.
  - Execution Unit - Where the execution of fetching and retrieving instructions occurs.
  - Registers - Internal CPU memory locations used a temporary data storage.
  - Flags - Indicate events when execution occurs.

    ![image](https://github.com/user-attachments/assets/0f1edb9f-5e91-4b8d-8cb7-53ca61796102)



- X86 32-bit CPU fetches a double-word(32-bits)(4 bytes) from a specific address in the memory and loads it into the CPU.At this point the CPU looks at the binary pattern of bits within the double word and begins executing the procedure that the fetched machine instruction directs it to do.Upon execution,the CPU fetches the next instruction in sequence.The CPU has a register called the `EIP` or the instruction pointer tht contains the next instruction to be fetched from the memory and then executed.We can immediately see that if we controlled flow of EIP, we can alter the program to do things it was NOT intended to do. This is a popular technique upon which malware operates.

--------------------

### General Purpose Registers

--------------------

- General purpos registers are used to temporarily store data as it is processed on the computer.The registers have evolved dramatically over time and continue to do so.Each new version of general-purpose registers is created to be backward compatible with previous processors. This means that code utilizing 8-bit registers on the 8080 chips will still function on today's 64-bit chipset.
- 8 purpose register-:
  - EAX->It is used for arithmetic calcaulations and also known as an accumulator, as it holds the results of arithmetic operations and function return values.
  - EBX-> The Base Register,Pointer to the data in th .DS segment.Used to store the base address of the program,
  - ECX-> It contains the counter register.It holds the amount of value that a process is to be repeated.Used for string and loop operations.
  - EDX-> General Purpose Register, additionally used for I/O devices,In addition will extend EAX to 64-bits.
  - ESI-> Source Index register. Pointer to data in the segment pointed to by the DS register. Used as an offset address in string and array operations. It holds the address from where to read data.
  - EDI-> Destination Index Register, Pointer to data (or destination) in the segment pointed to by the ES register. Used as an offset address in string and array operations. It holds the implied write address of all string operations.
  - EBP-> Base Pointer, pointer to the data in the stack frame, it points to the bottom of the current stack frame. It is used to reference local variables.
  - ESP-> Stack pointer, pointer to the data in the top of the stack frame, It is used to reference local variables.

- The above registers are 32-bit in length or 4 bytes in length.Each of the lower 2 bytes of the EAX, EBX, ECX, and EDX registers can be referenced by AX and then subdivided by the names AH, BH, CH and DH for high bytes and AL, BL, CL and DL for the low bytes which are 1 byte each.
- In addition, the ESI, EDI, EBP and ESP can be referenced by their 16-bit equivalent which is SI, DI, BP, SP.
----------------

### Subdividing EAX and other registers

---------------

- EAX would have AX as its 16-bits segment and you can further AX into AL for the low 8-bits and AH for the high 8-bits.The same holds true for EBX, ECX and EDX as well. EBX would have BX as its 16-bit segment and then you can further subdivide BX into BL for the low 8 bits and BH for the high 8 bits. ECX would have CX as its 16-bit segment and then you can further subdivide CX into CL for the low 8 bits and CH for the high 8 bits. EDX would have DX as its 16-bit segment and then you can further subdivide DX into DL for the low 8 bits and DH for the high 8 bits.
- ESI would have SI as its 16-bit segment, EDI would have DI as its 16-bit segment, EBP would have BP as its 16-bit segment and ESP would have SP as its 16-bit segment.

----------------

### Segment Registers

----------------

- They are used to reference memory locations.There are three different methods of accessing system memory of which we will focus on the flat memory model which is relevant for our purposes.
- There are six segment registers which are as follows:
  - CS: Code segment register stores the base location of the code section (.text section) which is used for data access.
  - DS: Data segment register stores the default location for variables (.data section) which is used for data access.
  - ES: Extra segment register which is used during string operations.
  - SS: Stack segment register stores the base location of the stack segment and is used when implicitly using the stack pointer or when explicitly using the base pointer.
  - FS: Extra Segment Register
  - GS: Extra Segment Register

----------------

- Each segment register is 16-bits and contains the pointer to the start of the memory-specific segment. The CS register contains the pointer to the code segment in memory. The code segment is where the instruction codes are stored in memory.
- The processor retrieves instruction codes from memory based on the CS register value and an offset value contained in the instruction pointer (EIP) register. Keep in mind no program can explicitly load or change the CS register. The processor assigns its values as the program is assigned a memory space.
- The DS, ES, FS and GS segment registers are all used to point to data segments. Each of the four separate data segments help the program separate data elements to ensure that they do no overlap. The program loads the data segment registers with the appropriate pointer value for the segments and then reference individual memory locations using an offset value.
- The stack segment register (SS) is used to point to the stack segment. The stack contains data values passed to functions and procedures within the program.
- Segment registers are parts of the operating system that cannot be read or write.When working in the protected mode flat model (x86 architecture which is 32-bit), your program runs and receives a 4GB address space to which any 32-bit register can potentially address any of the four billion memory locations except for those protected areas defined by the operating system.Physical memory may be larger than 4GB however a 32-bit register can only express 4,294,967,296 different locations. If you have more than 4GB of memory in your computer, the OS must arrange a 4GB region within memory and your programs are limited to that new region. This task is completed by the segment registers and the OS keeps close control of this.

----------------

### Instruction Pointer (EIP)

----------------

- The instruction pointer register called the EIP register is simply the most important register you will deal with in any reverse engineering. The EIP keeps track of the next instruction code to execute.EIP pointer points to the next instruction code to execute.If you were to alter that pointer to jump to another area in the code you have complete control over that program.

-------------------

- It is the most important register that we will deal with in reverse engineering and it presents the next instruction code for the processor to execute.For our purposes today, we will see the raw POWER of assembly language and particularly that of the EIP register and what we can do to completely hack program control.
- Code-:

```c
#include <stdio.h>
#include <stdlib.h>

void unreachableFunction(void) {
     printf("flag{hidden_function_12345678}\n");
}

int main(void) {
    printf("Hello World!\n")
    return 0;
}

```
- In this code, we cannot access the `UnreachableFunction` because it cannot be called by the program itself
- Compiling with gcc-:

```bash
```
- You might face this error-:

```
❯ gcc -m32 -o eipexample eipexample.c
In file included from eipexample.c:1:
/usr/include/stdio.h:28:10: fatal error: bits/libc-header-start.h: No such file or directory
   28 | #include <bits/libc-header-start.h>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
```
- Install 32-bit libraries with `sudo apt-get install gcc-multilib`
- Launching gdb without pwndgb,comment out `source /home/<user</pwndbg/gdbinit.py` in the `~/.gdbinit` file.
- Controlling the eip,first of all, run the program with `gdb ./program`, set disasseumble flavor to intel architecture.

```gdb
set disassembly-flavor intel
```
- Set a breakpoint at function `main` with `b main`
![image](https://github.com/user-attachments/assets/aac64a40-aa6d-466d-a56e-a5316e641470)

- Then, run with `r`

![image](https://github.com/user-attachments/assets/23917dc6-c492-4366-8c84-e98db3a66eff)


- Use `disas` to disassemble the code with `gdb`

![image](https://github.com/user-attachments/assets/c9c56bcd-d8c4-4f02-8c20-03e6786eb573)

- The "=>" points to the instruction where the EIP is pointing to that will be executed next.
- If we run it with `r`, we will see where it is pointing to.

![image](https://github.com/user-attachments/assets/7eddfaec-3b95-49bb-b721-786eda262888)

- Let's see where the eip is pointing to with `x/1xw $eip` and `x/1xb $eip`.

![image](https://github.com/user-attachments/assets/ecbf4202-4607-44c6-8219-1e07f7ee4c11)

- Now, let's focus on the unreachable function.Disassemble with `disas` and the highlighted part is the memory address.

![image](https://github.com/user-attachments/assets/e50902ce-efa1-450d-865a-b8627e4fc8e6)

- Now let's set the eip with `set $eip=<addr>` to hijack the flow of the program.`$eip` is `$rip` in  64-bit programs.

![image](https://github.com/user-attachments/assets/6341b4f7-6e62-48df-9bc0-f7716519e98b)

- Then, press `c` to continue-:

![image](https://github.com/user-a5ttachments/assets/69dee587-8fac-41e3-9404-efdca5c2de4a)


- We've successfully hijacked the program flow with the aid of instruction pointer.

--------------------

### Control Register Pointer

---------------------

- There are 5 control registers which are used to determine the operating mode of the CPU and the characteristics of the current executing tasks.
  -  CR0-: System flag that control the operating mode and various states of the processor
  -  CR1-: (Not Currently Implemented)
  -  CR2-: Memory Fault Implementation
  -  CR3: Memory page Directory information
  -  CR4-: Flags that enable processor feathers and indicate feature capabilities of the processor.

- The values in each of the control registers can’t be directly accessed however the data in the control register can be moved to one of the general-purpose registers and once the data is in a GP register, a program can examine the bit flags in the register to determine the operating status of the processor in conjunction with the current running task.
- If a change is required to a control register flag value, the change can be made to the data in the GP register and the register moved to the CR. Low-level System Programmers usually modify the values in control registers. Normal application programs do not usually modify control register entries however they might query flag values to determine the capabilities of the host processor chip on which the program is currently running.

----------------------

### Flags

----------------------

- The topic of flags are one of the most extremely complex and complicated concepts of assembly language and program flow control when reverse engineering. This information below will become much clearer as we enter into the final phase of our training when we reverse engineer C applications into assembly language.Flags are critical to Assembly programs that helps to notice if a program was successfully executed.
- We are dealing with 32-bit assembly to which a single 32-bit register which contains a group of status, control and system flags exist. This register is called the EFLAGS register as it contains 32 bits of information that are mapped to represent specific flags of information.
- There are three kinds of flag-:
 - Status flags
 - Control Flags
 - System flags

- Status flag-:

```
CF: Carry Flag
PF: Parity Flag
AF: Adjust Flag
ZF: Zero Flag
SF: Sign Fla
OF: Overflow Flag
```

- Carry flag is when the a math operation or math inteer carry or borrow from the most signifcant bit.This is an overflow condition for the register involved in the math operation. When this occurs, the remaining data in the register is not the correct answer to the math operation.
- Parity flag-: The parity flag is used to indicate corrupt data as a result of a math operation in a register. When checked, the parity flag is set if the total number of 1 bits in the result is even and is cleared if the total number of 1 bits in the result is odd. When the parity flag is checked, an application can determine whether the register has been corrupted since the operation.
- Adjust flag-: The adjust flag is used in Binary Coded Decimal math operations and is set if a carry or borrow operation occurs from bit 3 of the register used for the calculation.
- Zero Flag-:The zero flag is set if the result of an operation is zero.
- Overflow Flag-: The overflow flag is used in signed integer arithmetic when a positive value is too big or a negative value is too small to be represented in the register.
- Sign flag-:The sign flag is set to the most significant bit of the result which is the sign bit and indicates whether the result is positive or negative.

- Control flag-:They are used to control the specific behaviour in the processor.The DF flag which is the direction flag is used to control the way strings are handled by the processor. When set, string instructions automatically decrement memory addresses to get the next byte in the string. When cleared, string instructions automatically increment memory addresses to get the next byte in the string.



