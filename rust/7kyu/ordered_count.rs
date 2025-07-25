use std::collections::HashSet;
use std::collections::HashMap;

fn ordered_count(sip: &str) -> Vec<(char, i32)> {
    let mut count = HashMap::new();
    let mut ordered: Vec<(char, i32)> = Vec::new();
    let mut seen: HashSet<char> = HashSet::new();
    for c in sip.chars() {
        *count.entry(c).or_insert(0) += 1;
    }
    for c in sip.chars().filter(|c| seen.insert(*c)) {
        ordered.push((c, count[&c]));
    }
    ordered
}
