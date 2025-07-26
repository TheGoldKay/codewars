fn sort_by_length(arr: &[String]) -> Vec<String> {
    let mut v: Vec<String> = arr.to_vec();
    v.sort_by(|a, b| a.len().cmp(&b.len()));
    v
}
