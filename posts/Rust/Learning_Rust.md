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
