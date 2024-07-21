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
- `Const` variables are hardcoded and should be in uppercase

         const MAX_SCORES: u32 = 100000;

### Scalar Types

A Scalar type means a single point character. It can be an `integer,floating-point number,Boolean and character`

### Integer types
An integer can be signed or unsigned. A signed integer can contain both negative and positive integers while unsigned ones can only contain non-negative integers.

| **length** | **signed** | **unsigned** |
|------------|------------|--------------|
| 8-bit      |   i8       |    u8        |
| 16-bit     |   i16      |    i16       |
| 32-bit     |   i32      |    u32       |
| 64-bit     |   i64      |    u64       |
| Arch       |   isize    |    usize     |

### Calculating the numbers that each length can store

- Signed integer 

      (2n − 1) N refers to the amount of bit e.g (2 raise to 8-1) which is 2 raise to 7-1 

- Unsigned integer

      (2n − 1) which is 2 raise to power the bit,then the result -1

- If use are unsure of the type of integer, you should use default `i32`.`isize and usize` are used when indexing collections.
  
      
### Boolean 

- It is denoted by `bool` in Rust.It can either be `true` or `false`

      let x: bool = true;
      let y: bool = false;

### Character

- It is denoted by `char`.It represents unicode characters e.g emojis

      let x: char  =  '[emoji]';

    
### Compound Types

### Tuple
- Tuple is a way of storing variables

      fn main () {
         let tup: (i32,i32,&str) = (100,100,"str");
     }

- Use destructuring to break down the values

      let (x,y,z) = tup;

- To also destructure, you can use x followed by . and the value you want to pick

      let hundred  =  x.2;
      println!(hundred);
     

### Array

- An array contains values and they must be of the same type. It is denoted by `[]`.

      let x = [1,2,3,4];

- To pick a value, use `x[index of the number]`

      println!("X is {}",x);

### Functions

- A function name should be separated with underscore and should not be in camel case
  e.g

      fn main() {
       println!("{}",printing_five());
    }
    fn printing_five() -> i32 {
       return 5;
    
    }

- Passing an argument or parameter into a function

      fn main () {
         multiply_by_five(100);
      }
      
      fn multiply_by_five(x: i32) {
          let result: i32 =  x * 5;
          println!("The result is {}",result);
      }

  
    

