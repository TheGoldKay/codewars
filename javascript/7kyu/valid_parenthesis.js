function validParenthesis(par){
    while(true){
      let newPar = par.replace(/\(\)/g, '');
      if(newPar === ""){
        return true;
      }else if(par === newPar){
        return false;
      }
      par = newPar;
    }
}

function validParenthesis(par) {
  let count = 0;
  for (let i = 0; i < par.length; i++) {
    if (par[i] === '(') {
      count++;
    } else if (par[i] === ')') {
      count--;
      if (count < 0) {
        return false;
      }
    }
  }
  return count === 0;
}