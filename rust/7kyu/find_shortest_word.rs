fn find_short(s: &str) -> u32 {
    let words: Vec<&str> = s.split(' ').collect();
    let mut shortest: u32 = words[0].len() as u32;
    for word in &words[1..]{
        let ln: u32 = word.len() as u32;
        if ln < shortest{
            shortest = ln;
        }
    }
    shortest
}