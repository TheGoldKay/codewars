fn sum_of_differences(arr: &[i8]) -> Option<i8> {
    if arr.len() < 2{
        return None
    }
    let mut sorted = arr.to_vec();
    let mut sum: i8 = 0;
    sorted.sort();
    for i in 0..sorted.len()-1{
        sum += sorted[i + 1] - sorted[i];
    }
    Some(sum)
}

fn sum_of_differences_better(arr: &[i8]) -> Option<i8> {
    if arr.len() < 2 {
        return None;
    }
    let mut sorted = arr.to_vec();
    sorted.sort_by(|a, b| b.cmp(a)); // Sort in descending order
    
    let mut sum: i8 = 0;
    for i in 0..sorted.len()-1 {
        sum += sorted[i] - sorted[i + 1];
    }
    Some(sum)
}

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(sum_of_differences(&[1, 2, 10]), Some(9));
        assert_eq!(sum_of_differences(&[1, 2]), Some(1));
        assert_eq!(sum_of_differences(&[1]), None);
    }
    
    #[test]
    fn test_better() {
        assert_eq!(sum_of_differences_better(&[1, 2, 10]), Some(9));
        assert_eq!(sum_of_differences_better(&[1, 2]), Some(1));
        assert_eq!(sum_of_differences_better(&[1]), None);
    }
}


