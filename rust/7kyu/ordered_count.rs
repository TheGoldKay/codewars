use std::collections::HashMap;

fn ordered_count(sip: &str) -> Vec<(char, i32)> {
    let mut count = HashMap::new();
    let mut ordered: Vec<(char, i32)> = Vec::new();
    let mut unique: Vec<char> = Vec::new();
    for c in sip.chars() {
        *count.entry(c).or_insert(0) += 1;
        if !unique.contains(&c) {
            unique.push(c);
        }
    }
    for c in unique.iter() {
        ordered.push((*c, count[&c]));
    }
    ordered
}
