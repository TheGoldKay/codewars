const palin = str => {
    for(let i = 0; i < str.length; i++){
        if(str[i] !== str[str.length - i - 1]) return false;
    }
    return true;
}

const complete = str => {
    for (let ind = 0, addStr = '', pal = ''; ind < str.length; ind++) {
      addStr = str[ind] + addStr;
      pal = str + addStr;
      if (palin(pal)) return pal;
    } 
}