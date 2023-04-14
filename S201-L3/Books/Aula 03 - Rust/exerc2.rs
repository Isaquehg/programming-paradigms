use std::io;

pub fn exerc2() {
    let mut arr: [i32; 10] = [0; 10];
    let mut number = String::new();
    let number_cvt: i32;

    io::stdin()
        .read_line(&mut number)
        .expect("failed to read line");
    number_cvt = number.trim().parse().unwrap();

    preenche_arr(&mut arr, number_cvt);
}

fn preenche_arr(arr: &mut [i32], x: i32) {
    let mut cont: i32 = 0;
    for n in 0..arr.len() {
        arr[n] = cont * x;
        cont += 1;
        println!("{}", arr[n]);
    }
}
