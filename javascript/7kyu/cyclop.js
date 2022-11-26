function cyclops(n) {
    num = n.toString(2);
    if(num.length % 2 == 0){
      return false;
    }
    let middle = Math.floor(num.length/2);
    if(num[middle] == '0' && (num.match(/0/g) || []).length == 1){
      return true;
    }else{
      return false;
    }
  }

console.log(cyclops(8126));