function smallWordHelper(sentence){
    vowels = 'aAeEiIoOuU';
    news = [];
    for(var w of sentence.split(" ")){
      console.log(w);
      if (w.length <= 3){
        news.push(w.toUpperCase());
      }else{
        var neww = "";
        for(var c of w){
          if(!vowels.includes(c)){
            neww += c;
          }
        }
        news.push(neww);
      }
    }
    return news.join(" ");
  }