// Basic entry point
fn hello(name: String){
    println!("Hello {}", name);
}

// OR with command line arguments
fn main(){
    println!("Please enter your name: ");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
    input = input.trim().to_string();
    let name = input[..1].to_uppercase() + &input[1..];
    hello(name);
}