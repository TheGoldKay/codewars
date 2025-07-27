function blowCandles(str) {
    const gap = 3;
    let begin = 0;
    let arr = str.split('').map(n => parseInt(n));
    let blows = 0; // number of candle blows
    while (candlesLit(arr)){
        const i = getFirst(arr);
        for (let inc = 0; inc < 3; inc++){
            arr[i + inc] -= 1;
        }
        blows++;
    }
    return blows;
}

function getFirst(arr){
    for (let i = 0; i < arr.length; i++){
        if (arr[i] > 0){
            return i;
        }
    }
}

function candlesLit(arr){
    for(const n of arr){
        if (n > 0){
            return true;
        }
    }
    return false;
}