function itsFree(urinals){
    for(let i = 0; i < urinals.length; i++){
        let a = urinals[i], b = urinals[i - 1], c = urinals[i + 1];
        if(a == '0' && !parseInt(b) && !parseInt(c)){
            return i;
        }
    }
    return false;
}

function mistake(urinals){
    for(let i = 0; i < urinals.length; i++){
        let a = urinals[i], b = urinals[i - 1], c = urinals[i + 1];
        if(a == '1' && b == '1' || a == '1' && c == '1'){
            return -1; 
        }
    }
    return false;
}

function getFreeUrinals(urinals){
    let free = 0;
    let ur = urinals.split('');
    if(mistake(ur) !== false){
        return -1;
    }
    while(true){
        let space = itsFree(ur);
        if(space === false){
            break;
        }else{
            ur[space] = '1';
            ++free;
        }
    }
    return free;
}

function getFreeUrinals2(urinals){
    if (urinals.match("11") != null) {
      return -1
    }
    let counter = 0;
    for (let i = 0; i < urinals.length; i++) {
      if (urinals[i] == 0) {
        if ((i == 0 || urinals[i - 1] == 0) && (i == urinals.length - 1 || urinals[i + 1] == 0)) {
          counter++;
          urinals = urinals.substring(0, i) + "1" + urinals.substring(i+1);
        }
      }
    }
    return counter;
}

function getFreeUrinals3(urinals) {
    let count = 0;
  
    for (let i = 0; i < urinals.length; i++) {
      if (urinals[i - 1] !== "1" && urinals[i + 1] !== "1") {
        if (urinals[i] === "0") {
          count++;
          i++;
        }
      } else if (urinals[i - 1] === "1" || urinals[i + 1] === "1") {
        if (urinals[i] === "1") {
          return -1;
        }
      }
    }
    return count;
}

let urinals = "10001";
console.log(getFreeUrinals(urinals));