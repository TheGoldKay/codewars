use std::collections::HashSet;

fn remove_duplicates(vec: &mut Vec<usize>) {
    let mut seen = HashSet::new();
    vec.retain(|&val| seen.insert(val)) // seen.insert(val) returns true if val wasn't already in seen
}

fn next_id(ids: &[usize]) -> usize {
    let mut list: Vec<usize> = ids.to_vec();
    let mut idd: usize = 0;
    list.sort();
    remove_duplicates(&mut list);
    for value in list{
        if value != idd{
            return idd
        }
        idd += 1;
    }
    idd
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basics() {
        assert_eq!(next_id(&[0,1,2,4,5]), 3);
        assert_eq!(next_id(&[0,1,2,3,4,5,6,7,8,9,10]), 11);
    }
}
