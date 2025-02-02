fn flick_switch(list: &[&str]) -> Vec<bool> {
    let mut bool_list: Vec<bool> = Default::default(); // let mut bool_list = Vec::new();
    let mut current: bool = true;
    for &word in list{
        if word == "flick"{
            current = !current;
        }
        bool_list.push(current);
    }
    bool_list
}