
fn disemvowel(s: &str) -> String {
    let vowels = "aeiouAEIOU";
    let out = s.chars().filter(|x| !vowels.contains(*x)).collect();
    out
}

fn main() {
    println!("{}", disemvowel("This website is for losers LOL!"));
}