#![allow(warnings)]

mod answers;

fn main() {
    let s = "Jhonnatan Carvalho";
    let ans = answers::name_shuffle::name_shuffler(s);
    let second = answers::name_shuffle::second_shuffler(s);
    println!("{}", ans);
    println!("{}", second); 
}
