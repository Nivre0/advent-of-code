use std::fs;
use md5;

fn main() {
    let file = "input.txt";
    println!("Using input: {}", file);

    let content = fs::read_to_string(file)
        .expect("Failed to read the file");

    println!("{}", content);

    let mut number = 1;
    let mut current_content = content;

    loop {
        let appended_content = format!("{}{}", current_content, number);

        let hash = format!("{:x}", md5::compute(appended_content));

        if hash.starts_with("000000") {
            println!("Found number: {}", number);
            break;
        }

        number += 1;

        if number > 1_000_000_000 {
            println!("No result found after 1,000,000,000 iterations");
            break;
        }

    }

    println!("Finished");
}
