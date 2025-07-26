fn sort_by_length(arr: &[String]) -> Vec<String> {
    let mut v: Vec<String> = arr.to_vec();
    v.sort_by(|a, b| a.len().cmp(&b.len()));
    v
}

fn sort_by_length_v2(arr: &[String]) -> Vec<String> {
    let mut v: Vec<String> = arr.to_vec();
    s.sort_by_key(String::len);
    v
}
