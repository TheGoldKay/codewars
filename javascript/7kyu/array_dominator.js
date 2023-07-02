function dominator(arr){
    let c = {};
    for(let n of arr){
        if(c[n] == undefined){
            c[n] = 1;
        }else{
            c[n] = c[n] + 1;
            if(c[n] > arr.length / 2){
                return n;
            }
        }
    };
    return -1;
}

function dominator1(arr) {
    for(let i=0, obj={}; i<arr.length; i++){
        obj[arr[i]]=obj[arr[i]]+1||1
        if(obj[arr[i]]>arr.length/2) return arr[i]
    }return -1 
  }
  
function dominator2(arr) {
    arr.sort();
    for (var i = 0, v = 0, c = 0; i < arr.length; i++) {
       if (v == arr[i]) c++;
       else { 
         v = arr[i];
         c = 1;
       }
       if (c > arr.length / 2) return v;
    }
    return -1;
  }

console.log(dominator([3,4,3,2,3,1,3,3]))
 