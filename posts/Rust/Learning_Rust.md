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

### Using `println!()` to insert values with placeholders

    let x  = 9;
    let y = 10;
    println!("The x is {} and y is {}",x,y);

### To update a crate, use

    cargo update

### To import a crate, use the keyword `extern crate` 

    extern crate rand
    use std::cmp::Ordering

### Comparing a number with `std::cmp::Ordering`

    match guess.cmp(&secret_number){
          Ordering::Less => println!(""),
          Ordering::Greater => println!(""),
          Ordering::Equal => println!(""),
    }

### Some functions
-  .trim() eliminates any whitespace in a a string

        let guess  =  "1";
        let mut guess =  guess.trim();

-  A variable can be reused in Rust with the .parse() function

       let guess = String::new();
       let mut guess: i32 = guess.trim().parse();
    
- Use `loop{}` to create a loop in rust and break it with `break` 

        extern crate rand;
        use rand::Rng;
        fn main() {
            let _secret_number = rand::thread_rng().gen_range(1,101);
            loop {
                let guess: u32  =  10;
                if guess ==  10 {
                   println!("Success");
                   break;
                }
            }
        }
    
### Guessing game final code

    extern crate rand;
    use std::io;
    use rand::Rng;
    use std::cmp::Ordering;
    fn main() {
       println!("Guessing game.....");
       let secret_number: u32  =  rand::thread_rng().gen_range(1,101);
       println!("The secret number is {}",secret_number);
       loop {
          let mut guess =  String::new();
          io::stdin().read_line(&mut guess)
             .expect("Enter a number.....!!!!");
          let guess: u32 = match guess.trim().parse() {
              Ok(num) => num,
              Err(_) => continue,
          };
          match guess.cmp(&secret_number) {
            Ordering::Less => println!("Lesser than the number"),
            Ordering::Equal => {
                println!("Equal to the number");
                break;
                },
            Ordering::Greater => println!("Greater than the number"),    
          }
       }    
    }

### Common Programming Concepts
This chapter explains the concepts like variables,functions, control flow, basic types and comments

### Variables

- A variable might be mutable or immutable, A variable is mutable if its value can be changed and immutable if its value cannot be changed.The `mut` keyword makes a variable mutable.

   A code without the `mut` keyword
  
         fn main () {
         let x = 6; 
         println!("X is {}",x);
         x = 9;
         println!("X is {}",x);
      }

   A code with the `mut` keyword

         fn main () {
         let mut  x = 6; 
         println!("X is {}",x);
         x = 9;
         println!("X is {}",x);
      }
