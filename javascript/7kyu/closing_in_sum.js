function closingInSum(n){
    let arr = Array.from(n.toString());
    if(arr.length == 1){
      return parseInt(arr[0]);
    }
    let sum = 0;
    while(true){
        let num = arr[0] + arr[arr.length-1];
        arr.shift();
        arr.pop();
        sum += parseInt(num);
        if(arr.length == 1){
            return parseInt(arr[0]) + sum;
        }else if(arr.length == 0){
            return sum;
        }
    }
}

function closingInSumAI(n) {
  let arr = Array.from(n.toString());
  
  if (arr.length === 1) {
    return parseInt(arr[0]);
  }
  
  let sum = 0;
  let start = 0;
  let end = arr.length - 1;
  
  while (start < end) {
    let num = parseInt(arr[start]) + parseInt(arr[end]);
    sum += num;
    start++;
    end--;
  }

  if (start === end) {
    sum += parseInt(arr[start]);
  }
  
  return sum;
}


console.log(closingInSum(123));