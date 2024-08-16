-------------------

### Learning Windows

-------------------

### Javac 

- `javac <file.java>` to compile a java file
- `java <file.java>` to run the file

### Displaying file contents

Use:
- `more <file name>`
- `type <file name>`

### Exit a terminal with

- `exit`


| **Commands**     |  **syntax**             |    **Actions**        |
|------------------|-------------------------|-----------------------|
|    dir           |    `dir`                |  List a directory     |                
|   cd             |   `cd <directory`       |  Change directory     |
|   cd ..          |   `cd ..`               | Move up a directory   |
|   move           |   `move file file`      | Move a file           |
|   copy           |  `copy file file`       | Copy a file           |
|   del            |   `del <file name>`     |  Delete a file        |  
|   mkdir          | `mkdir <directoryname>` | Make a directory      |

### Redirecting output

- Use `>` and `<`, Linux logic appplies to it,the same with  piping `|`


### Running a cmd shell as admin

- `powershell start cmd  -v runAs`

### Checking list of drivers

- `driverquery`

### Show your PC's details

- `systeminfo`

### Environmental Variables

- `set`

### Prompt

- To change your default text

 ![image](https://github.com/user-attachments/assets/2ee8b3d5-2f3a-47dd-aa3e-0e18548b41d8)

- use `prompt <what you want to do> $G`
- To revert, use `prompt`

### To copy to clipboard

- Just pipe the output of a file to clip e.g `dir | clip`

### Listing files and their extensions

- Use `assoc`

### Changing your cmd title window

- Use `title cmdbaby`

### Comparing 2 files

- Use `fc <file1> <file2>`

### Using `cipher`

- On a PC, deleted files remain accessible to you and other users. So, technically, they are not deleted under the hood.

   `cipher`

### Checking open ports, ip and states

- Use `netstat -an`

### shutdown a system
- Use `shutdown`
- `shutdown /r` will restart a system

### Clear a system shell

- Use `cls`

### Exit cmd

- Use `cmd`

### Rename a file

- use `ren <filename1> <filename2>`

### Creating a file

- use `echo <words> > filename.txt`

### Use `-help` to show a guide on  list

- `powercfg -help`

### To run the Deployment Image Service Management Tool

- Use `dism`

### Show the Serial Number and Label Info of the Current Drive

- Use `vol`

### Pinging an address

- Use `ping <addr>`

### Changing the terminal's color

- Use `color attr` to check a color's index
- use `color <number>` to change color

### Checking a wifi's password

- Use `netsh wlan show profiles` to check wifis previously connected to
- Then,`netsh wlan show profiles name="<wifi's name>" key=clear`

### Using `ipconfig` to check the machine's ip address

- run `ipconfig`
- This command also has extensions such as `ipconfig /release`, `ipconfig /renew`, and `ipconfig /flushdns` which you can use to troubleshoot issues with internet connections

### System file checker `sfc`

- Use `sfc /scannow` to check for corrupt files and repair them
  
### `Powercfg`
  You can use this command with its several extensions to show information about the power state of your PC. 

- `powercfg /energy` to generate a battery health report

### Starting a web address

- use `start <web addr>`

### Showing the tree of the current directory

- Use `tree`

### Os version

- Use `ver`

### Show open programs

- Use `tasklist`

### Killing open programs

- use `taskkill /IM "<program>" /F` to kill a program

### Showing date, time

- Use `date` to show data
- Use `time` to show time

 
------------------------------

### REFERENCES:

- [Freecode camp](https://www.freecodecamp.org/news/command-line-commands-cli-tutorial/)

------------------------------

 
### Understanding Windows

### COnnecting to a remote desktop protocol, use `remmina` on linux 

![image](https://github.com/user-attachments/assets/914044ec-5759-49a0-b26e-7d81e24b40a6)

- Enter ip

![image](https://github.com/user-attachments/assets/a27b0ae2-64e2-4b51-8e7e-a5cd2e56ecca)

- Enter credentials


### Troubleshooting with Msconfig
  
  The System Configuration utility (MSConfig) is for advanced troubleshooting, and its main purpose is to help diagnose startup issues. 

- Use `windowskey + r` ,type `msconfig`

![image](https://github.com/user-attachments/assets/a6c81d7d-cdd4-422e-82e5-7316071f1650)

- Type `taskmgr to run the `task manager` get programs and background processes

![image](https://github.com/user-attachments/assets/83bd7c79-4909-4ce4-bb70-c6648443f897)

### Computer management

The Computer Management (compmgmt) utility has three primary sections: System Tools, Storage, and Services and Applications.

- Type `compmgmt.msc` in the `windowskey + r` dialog box
- The task scheduler is used to enable tasks at startup

![image](https://github.com/user-attachments/assets/0ab80421-0ccf-447d-a983-26205b412b12)

- Event viewer allows us to acccess logs of events hat occurred while using the system

![image](https://github.com/user-attachments/assets/b9a71b7f-e8df-4a18-a720-3bd51621324c)

- Shared folders shows shares or folders that users can have access to

![image](https://github.com/user-attachments/assets/67f17e12-3223-4885-8eb2-418dc68a9eaa)

-







