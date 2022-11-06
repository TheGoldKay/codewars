function highAndLow(numbers){
    arr = numbers.split(" ");
    low = Infinity;
    high = -Infinity;
    for(num of arr){
      n = parseInt(num)
      if(n < low){
        low = n;
      }
      if(n > high){
        high = n;
      }
    }
    return high.toString() + " " + low.toString();
  }