fn contamination(text: &str, character: &str) -> String {
    let mut cont = String::new();
    for i in 0..text.len(){
        cont += character;
    }
    cont
}

fn contamination_2(text: &str, character: &str) -> String {
    text.chars().map(|c| character).collect()
}

fn contamination_3(text: &str, character: &str) -> String {
    character.repeat(text.len())
}