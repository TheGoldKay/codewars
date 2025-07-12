// https://www.codewars.com/kata/582e0e592029ea10530009ce/train/rust

fn duck_duck_goose(players: &[Player], goose: u32) -> &'static str {
    let ln = players.len() as u32;
    let out = &players[((goose - 1) % ln) as usize];
    return out.name;
}

fn duck_duck_goose_BEST(players: &[Player], goose: u32) -> &'static str {
    players[(goose - 1) as usize % players.len()].name
}