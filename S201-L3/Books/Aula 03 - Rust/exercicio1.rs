use std::io;

pub fn main() {
    let mut n1_input = String::new();
    let mut n2_input = String::new();
    let mut op = String::new();
    let res: i32;
    let number1: i32;
    let number2: i32;

    io::stdin().read_line(&mut n1_input).expect("failed to read line");
    io::stdin().read_line(&mut n2_input).expect("failed to read line");

    println!("Somar ou multiplicar? (+ ou *)");
    io::stdin().read_line(&mut op).expect("failed to read line");

    number1 = n1_input.trim().parse().unwrap();
    number2 = n2_input.trim().parse().unwrap();

    if op.trim() == "+" {
        res = number1 + number2;
        println!("Soma {} + {} = {}", number1, number2, res)
    } else {
        res = number1 * number2;
        println!("Multiplicacao {} * {} = {}", number1, number2, res)
    }
}
