function elevator(left, right, call){
    if(Math.abs(call - right) <= Math.abs(call - left)){
        return "right";
    }else{
        return "left";
    }
}