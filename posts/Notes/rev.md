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
- 
