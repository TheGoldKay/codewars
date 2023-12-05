function partyPeople(party){
    while(true){
        let change = false;
        let len = party.length;
        let max = Math.max(...party);
        if(max > len){
            let max_index = party.indexOf(max);
            party.splice(max_index, 1);
            change = true;
        }
        if(change === false){
            return len;
        }
    }
}

function partyPeople(party) {
    let len = party.length;
  
    while (true) {
      let max = Math.max(...party);
  
      if (max > len) {
        let index = party.indexOf(max);
        while(index !== -1){
          party.splice(index, 1);
          len--;
          index = party.indexOf(max);
        }
      } else {
        return len;
      }
    }
  }