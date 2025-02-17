use itertools::Itertools;

pub fn name_shuffler(s: &str) -> String {
    let mut shuffled= s.split_whitespace();
    let first = shuffled.next().unwrap();
    let last = shuffled.next().unwrap();
    format!("{} {}", last, first)
}

pub fn second_shuffler(s: &str) -> String {
    s.split_whitespace().rev().join(" ")
}