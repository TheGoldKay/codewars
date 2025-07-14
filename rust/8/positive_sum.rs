fn positive_sum(slice: &[i32]) -> i32 {
    let mut sum: i32 = 0;
    for n in slice.iter() {
        if *n > 0 { // n.is_positive()
            sum += n;
        }
    }
    // slice.iter().filter(|n| n.is_positive()).sum()
    sum
}