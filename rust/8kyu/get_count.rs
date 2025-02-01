fn is_vowel(c: char) -> usize{
    let vowels: &str = "aeiouAEIOU";
    for vowel in vowels.chars(){
        if vowel == c{
            return 1
        }
    }
    return 0
}
 
fn get_count(string: &str) -> usize {
    let mut vowels_count: usize = 0;
    for c in string.chars(){
        vowels_count += is_vowel(c);
    }
    vowels_count
}

fn get_count_BETTER(string: &str) -> usize {
    string
        .chars()
        .filter(|&c| "aeiou".contains(c))
        .count()
}

fn main(){
    let string: &str = "abracadabra";
    println!("{}", get_count(string));
}