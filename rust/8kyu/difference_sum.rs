fn sum_of_differences(arr: &[i8]) -> Option<i8> {
    if arr.len() < 2{
        return None
    }
    let mut sorted = arr.to_vec();
    let mut sum: i8 = 0;
    sorted.sort_by(|a, b| a.cmp(b));
    for i in 0..sorted.len()-1{
        sum += sorted[i + 1] - sorted[i];
    }
    Some(sum)
}

fn sum_of_differencesBETTER(arr: &[i8]) -> Option<i8> {
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
    use super::sum_of_differences;

    
    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";
    #[test]
    fn sample_tests() {
        assert_eq!(sum_of_differences(&[1, 2, 10]), Some(9), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[-3, -2, -1]), Some(2), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[1, 1, 1, 1, 1]), Some(0), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[-17, 17]), Some(34), "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[]), None, "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[0]), None, "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[-1]), None, "{}", ERR_MSG);
        assert_eq!(sum_of_differences(&[1]), None, "{}", ERR_MSG);
    }
}


