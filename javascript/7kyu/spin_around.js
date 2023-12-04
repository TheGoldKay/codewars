function spinAround(keywords) {
  let rotations = 0;
  for (let keyword of keywords) {
    if (keyword === 'right') {
      rotations++;
    } else if (keyword === 'left') {
      rotations--;
    }
  }
  return Math.floor(Math.abs(rotations) / 4);
}

function spinAround(turns) {  
  let spins = 0;
  for(let turn of turns){
    if(turn === "right"){
      spins += 0.25;
    }else if(turn === "left"){
      spins -= 0.25;
    }
  }
  return Math.floor(Math.abs(spins));
}