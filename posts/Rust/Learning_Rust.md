### Learning Rust

### Installing Rust on LINUX CLI
  
    curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh

### Printing Hello World!!!

    fn main () {
       println!("Hello World!!!");
    }

### Compiling rust code with rustc

    rustc -o <binary's name> <rust script's name>.rs

### Or you can use

    rustc try.rs

### Cargo
 Cargo is a package manager for Rust and it is used to install dependencies that your code requires.

 ### Checking Cargo's version

     cargo --version

 ### Creating a directory to manage project with cargo containing directory for us: a Cargo.toml file and a srcdirectory with a main.rs file inside. It has also initialized a new Git repository along with a .gitignore file.

     cargo new <binary> --bin
  
 ### To compile Rust with cargo, from the directory, run with the command below and spot the binary in `target/debug`

     cargo build

 ### To build and run, use

     cargo run

### To run and check for errors without creating a binary, use

     cargo check

### To run and compile a rust code from github, use

    $ git clone someurl.com/someproject
    $ cd someproject
    $ cargo build


### Chapter 2: Building a Guessing game 

 Learning `let,match and other methods`

### To import a library, use the keyword `use` and to use the specific library, use `::`

    use std::io;

### To create a mutable variable, use `mut` and `let` to define a variable

    let  mut foo = "bar";
### Creating a variable to store string

    let mut foo = String::new();

### Using io to read lines and triggering a statement if the functions fails to read the line with `.expect`

'&' means reference in rust and it allows rust read data once without making it read multiple times.`&mut guess` is used instead of `&guess` to make it mutable.

    io::stdin().read_line(&mut guess).expect("Failed to read lines");
