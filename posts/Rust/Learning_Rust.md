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


  ### Control Flow

- An example of an `if else` statement

        fn main () {
           let x: bool =  true;
           let y: bool = true;
           println!("{}",compare_boolean(x,y));
        }
        fn compare_boolean(x: bool,y: bool) -> String {
           if x == y {
              return "Same Boolean".to_string()
           } else {
              return "Different boolean".to_string()
           }
        }


- Using `if` in a let statement, it should be noted that the if condition should return the same type e.g `str` should not be replaced with `integer`.
    
       fn main () {
        let condition: bool = true;
        let number: i32  =  if condition {
            5
        } else {
            6
        };
        println!("{}",number);
      }

  
### Loops

- The main types of loops are `loop,while and for`

### Loop

- Repeating code with loop, break with `ctrl + c` {Sikes}

      fn main () {
        loop {
            println!("Liftoff!!!");
        }
      }

- Using while loop

      fn main () {
        let mut number: i32 = 3;
        while number != 0 {
             println!("Hichichichic,number equals to 0");
             number = number - 1;
        }
        println!("Liftoff!!!!!");
      }

- Using `while` loop to print out the elements of a collection
    
       fn main () {
       let items = [100,90,90,-100];
       let mut index = 0;
       while index < items.len() {
             println!("The value is {}",items[index]);
             index = index + 1;
       }
       println!("Items printed")
      }

- A for loop looks like this,looping through it requires the `iter()` function

           fn main () {
         let elements = [1,23,45,67,88];
         for element in elements.iter() {
             println!("Element: {}",element);
         }
      }

- To reverse the order of the array, use the `rev()` function, notice the syntax `(<start number>..<end number>).rev()`

      fn main() {
       for i in (1..100).rev() {
           println!("Value: {}",i);
       }
      }

### Ownership

### Rules:

- Every value has a variable which is the `owner`
- When a variable is out of scope, the value will be dropped
- A value cannot have multiple variables i.e `owners`

  
### Learning Ownership with `String` data type

- When you create a string with `String::from("Hello")`,it automatically adds it to the heap because the size is unknown at compile time.Although, this kind of string can be mutated e.g

      fn main() { 
       let mut string = String::from("Hello");
       string.push_str(", world");
       println!("{}",string);
      }
### Memory Allocation of the two strings

- Every programming language requires a garbage collector which is required to return unused memory but in the case of rust, it does not exist and it is left to us to clean up unused memory. This forces Rust to spot `unused variables` as a bug, Rust takes a different path and memory is unused if a variable is out of scope e.g

      fn main() {
         let mut string =  String::from("hello") //Variable x is still in use
                                                 // still in use
      } // No longer in use after this curly brace and calls the drop function after this curly brace

### Ways that data and variables interact: `Move`

- Multiple variables can interact with the same data e.g
      
        fn main() {
         let x =  100;
         let z = x;
         println!("{},{}",x,z);
      }

- This concept does not apply to strings e.g

      fn main() {
         let x = String::from("Hello");
         let s2 = x;
       }
  The above code will lead to a `double free flow` error because once Rust tris to call the `drop` function,the two variables will point to the same location. Freeing memory twice can lead to memory corruption and cause security vulnerabilities. The best solution is to apply the shallow copy by copying only the pointer,capacity and length.

- If you want to deeply copy the heap data of a String, use the `clone()` function e.g

      fn main() {
          let x = String::from("Hello");
          let x2 = x.clone();
          println!("{},{}",x,x2);
      }

- 
    
