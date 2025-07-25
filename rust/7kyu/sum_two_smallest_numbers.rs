fn sum_two_smallest_numbers(numbers: &[u32]) -> u32 {
    let mut arr = numbers.to_vec();
    arr.sort();
    arr[0] + arr[1]
}