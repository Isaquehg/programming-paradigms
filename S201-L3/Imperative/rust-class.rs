use std::io;

fn preenche_arr(arr &mut [i32], x i32){
    for i in 0..arr.len(){
        arr[i] = i * x;
    }
}

fn main(){
    //exercicio 1
    //input with error treatment and casting to i32
    let result: i32;
    let mut num1_str = String::new();
    let mut num2_str = String::new();
    let mut op = String::new();
    
    io::stdin().read_line(&mut num1_str).expect("failed to read line");
    io::stdin().read_line(&mut num2_str).expect("failed to read line");
    io::stdin().read_line(&mut op).expect("failed to read line");

    let num1 = match num1_str.trim().parse()::<i32>(){
        Ok(n) => n,
        Err(_) => { print!("Fail!"); 0 }
    };
    let num2 = match num2_str.trim().parse()::<i32>(){
        Ok(n) => n,
        Err(_) => { print!("Fail!"); 0 }
    };

    if op.trim() == "+"{
        result = num1 + num2;
    }
    else if op.trim() == "*"{
        result = num1 * num2;
    }

    print("{}", result)

    //exercicio 2
    let arr: [i32; 4] = [0; 10];
    let num: i32 = 5;

    preenche_arr(&mut arr, num);
}