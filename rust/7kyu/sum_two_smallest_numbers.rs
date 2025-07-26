fn sum_two_smallest_numbers(numbers: &[u32]) -> u32 {
    let mut arr = numbers.to_vec();
    arr.sort();
    arr[0] + arr[1]
}

fn sum_two_smallest_numbers(numbers: &[u32]) -> u32 {
    let mut a: u32 = u32::MAX;
    let mut b: u32 = u32::MAX;
    for num in numbers.iter(){
        if *num < a {
            b = a;
            a = *num;
        }else if *num < b{
            b = *num;
        }
    }
    a + b
}