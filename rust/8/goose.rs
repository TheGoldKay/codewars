fn duck_duck_goose(players: &[Player], goose: u32) -> &'static str {
    let ln = players.len() as u32;
    let out = &players[((goose - 1) % ln) as usize];
    return out.name;
}