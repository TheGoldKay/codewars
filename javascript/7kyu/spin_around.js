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