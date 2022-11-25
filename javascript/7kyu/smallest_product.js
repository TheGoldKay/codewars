function smallestProduct(arr) {
    let prod = Infinity; 
    for(let a of arr){
        let p = 1;
        for(let n of a){
            p *= n;
        }
        if(p < prod){
            prod = p;
        }
    }
    return prod;
}
    