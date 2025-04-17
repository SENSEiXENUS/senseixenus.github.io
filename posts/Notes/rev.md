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
- A digit in hexadecimal is 4 bits long which is a `nibble`.If we look at `40`,it is 8 bits long which is a byte.If we look at d040, we have two bytes or a word in length. Finally, ffffd040 is a double word or 4 bytes in length which is 32-bits long.
