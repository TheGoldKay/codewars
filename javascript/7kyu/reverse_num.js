function convertToBase(number, base) {
    let result = "";
    while (number > 0) {
      let remainder = number % base;
      result = remainder.toString() + result;
      number = Math.floor(number / base);
    }
  
    return result || "0";
  }
  function reverseNumber(n, b){
      console.log(n, b);
      n = Number(n);
      b = Number(b);
      if(b === 1){
          return BigInt(n);
      }else if(b <= 36){
          n = n.toString(b).split('').reverse().join('');
          return BigInt(parseInt(n, b));
      }else{
        n = convertToBase(n, b).split('').reverse().join('');
        console.log(n);
        console.log(parseInt(n, b));
        return BigInt(convertToBase(n, 10));
      }
}

let n = 5;
let b = 1;
console.log(reverseNumber(BigInt(n), BigInt(b)));