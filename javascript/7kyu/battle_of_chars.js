function power(s){
    let p = 0;
    for(let char of s){
        if(char.toLowerCase() === char){
            p +=  26 * (char.charCodeAt(0) - 96) * 0.5; 
        }else{
            p += 26 * (char.charCodeAt(0) - 64);
        }
    }
    return p;
}

function battle(x, y) {
    let xp = power(x);
    let yp = power(y);
    if(xp > yp){
        return x;
    }else if(yp > xp){
        return y;
    }else{
        return "Tie!";
    }
}

function splitIt(x) {
  return x
    .split('')
    .map(elem => elem === elem.toLowerCase() ? (elem.charCodeAt() - 96) / 2 : elem.charCodeAt() - 64)
    .reduce((acc, num) => acc + num);
}