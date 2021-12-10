use std::{
    env,
    fs::File,
    io::{prelude::*, BufReader},
    //cmp::max
};

fn main() {
    let args: Vec<String> =env::args().collect();

    let file = File::open(args[1].clone()).unwrap();
    let codes: Vec<String> = BufReader::new(file)
        .lines()
        .map(|l| l.expect("Could not parse line"))
        .collect();

    let code_length = codes[0].chars().count();

    let mut gamma_rate = 0;
    let mut epsilon_rate = 0;

    let mut zeros: u32;
    let mut ones: u32;

    let base: i32 = 2;

    for i in 0..code_length {
        zeros = 0;
        ones = 0;
        for j in 0..codes.len() {
            if codes[j].chars().nth(i).unwrap() == '0' {
                zeros+=1;
            } else {
                ones+=1;
            }
        }

        if ones > zeros {
            gamma_rate += base.pow(code_length as u32 - 1 - i as u32);
        } else {
            epsilon_rate += base.pow(code_length as u32 - 1 - i as u32);
        }
    }

    println!("{}", gamma_rate * epsilon_rate);
}