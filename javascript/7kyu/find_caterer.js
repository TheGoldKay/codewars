function findCaterer(budget, people){
    const a = people * 15;
    if(!people || a > budget) return -1;
    const b = people * 20;
    const c = people > 60? (people * 30) * 0.8: people * 30;
    const arr = [[a, 1], [b, 2], [c, 3]];
    arr.sort(function (a, b){
        return b[0] - a[0];
    });
    for(const elem of arr){
      if(elem[0] <= budget){
        return elem[1];
      }
    }
}

function findCaterer(budget, people){
    if (budget < 15 || people < 1) {
      return -1;
    }
    
    if (people * (people > 60 ? 24 : 30) <= budget ) {
      return 3
    }
    
    if (people * 20 <= budget ) {
      return 2
    }
    
    if (people * 15 <= budget ) {
      return 1
    }
    
    return -1;
  }