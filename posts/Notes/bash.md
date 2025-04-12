-------------

### Bash Scripting
### Bash

--------------

### Bash manual

---------------

### What is a shell?

----------------

- A shell is a macro processor that executes commands.The term macro processor means functionality where text and symbols are expanded to create larger expressions.A Unix shell is both a command interpreter and a programming language. As a command interpreter, the shell provides the user interface to the rich set of GNU utilities. The programming language features allow these utilities to be combined. Files containing commands can be created, and become commands themselves. These new commands have the same status as system commands in directories such as /bin, allowing users or groups to establish custom environments to automate their common tasks.Shells may be used interactively or non-interactively. In interactive mode, they accept input typed from the keyboard. When executing non-interactively, shells execute commands read from a file.

---------------------

### SHELL SYNTAX

---------------------

- When the shell reads input, it proceeds through a sequence of operations. If the input indicates the beginning of a comment, the shell ignores the comment symbol (‘#’), and the rest of that line.

```bash
#script
```

- Shell mode of operation-:

```
- Reads it from a file or if it is passed as an argument with `-c`  or from the user terminal
- Breaks the input into words and operators, obeying the quoting rules described in Quoting. These tokens are separated by metacharacters.
- Parses the tokens into simple and compound commands
- Performs the various shell expansions (see Shell Expansions), breaking the expanded tokens into lists of filenames
- Performs any necessary redirections
- Optionally waits for the command to complete and collects its exit status
```

- Quoting is used to remove the special meaning of certain characters or words to the shell. Quoting can be used to disable special treatment for special characters, to prevent reserved words from being recognized as such, and to prevent parameter expansion.
- Each of the shell metacharacters (see Definitions) has special meaning to the shell and must be quoted if it is to represent itself. When the command history expansion facilities are being used (see History Expansion), the history expansion character, usually ‘!’, must be quoted to prevent history expansion.e.g

![image](https://github.com/user-attachments/assets/36f11f92-d194-48e6-9558-05920acd6711)

- Quoting Mechanisms-:

```
- Escape Character
- Single Quotes
- Double quotes
- Ansi-c Quoting
- Locale-Specific Translation
```

- Escape character `\` is the Bash escape character.It preserves the literal value of the next character that follows, with the exception of newline. If a \newline pair appears, and the backslash itself is not quoted, the \newline is treated as a line continuation (that is, it is removed from the input stream and effectively ignored).
- Enclosing characters in single quotes (‘'’) preserves the literal value of each character within the quotes. A single quote may not occur between single quotes, even when preceded by a backslash.
- Double quotes-: Enclosing characters in double quotes (‘"’) preserves the literal value of all characters within the quotes, with the exception of ‘$’, ‘\`’, ‘\’, and, when history expansion is enabled, ‘!’.The characters ‘$’ and ‘`’ retain their special meaning within double quotes.A double quote may be quoted within double quotes by preceding it with a backslash. If enabled, history expansion will be performed unless an ‘!’ appearing in double quotes is escaped using a backslash. Backslahing with non-special characters within double quotes won't affect the characters e.g `backslash before a double quotes within 2 double quotes `.The backslash preceding the ‘!’ is not removed.The special parameters ‘*’ and ‘@’ have special meaning when in double quotes.
- ANSI-C Quoting-: Character sequences of the form $’string’ are treated as a special kind of single quotes. The sequence expands to string, with backslash-escaped characters in string replaced as specified by the ANSI C standard.


