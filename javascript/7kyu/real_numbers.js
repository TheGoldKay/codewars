function realNumbers(n){
    let arr = Array.from({ length: n }, (_, index) => index + 1);
    return arr.filter(num => num%2 !== 0 && num%3 !== 0 && num%5 !== 0).length;
}

function realNumbers(n) {
    let count = 0;
  
    for (let i = 1; i <= n; i++) {
      if (i % 2 !== 0 && i % 3 !== 0 && i % 5 !== 0) {
        count++;
      }
    }
  
    return count;
}

const {floor} = Math;

function realNumbers(n){
  return n
       - floor(n / 2)
       - floor(n / 3)
       + floor(n / 6)
       - floor(n / 5)
       + floor(n / 10)
       + floor(n / 15)
       - floor(n / 30);
}