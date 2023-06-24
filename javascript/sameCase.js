function sameCase(a, b){
    if(a.match(/[a-zA-Z]/i) && b.match(/[a-zA-Z]/i)){
        if(a >= "a" && b >= "a" && a <= "z" && b <= "z"){
            return 1;
        }else if(a >= "A" && b >= "A" && a <= "Z" && b <= "Z"){
            return 1;
        }else{
            return 0;
        }
    }else{
        return -1;
    }
  }

const isLower = s => /[a-z]/.test(s)
const isLetter = s => /[a-zA-Z]/.test(s)

const sameCase2 = (a, b) => isLetter(a) && isLetter(b) 
  ? isLower(a) === isLower(b) ? 1 : 0
  : -1