function treePhotography(trees){
    let left = 0;
    let right = 0;
    let high_left = 0;
    let high_right = 0;
    for(let i = 0; i < trees.length; i++){
        if(trees[i] > high_left){
            high_left = trees[i];
            left++;
        }
        if(trees[trees.length - 1 - i] > high_right){
            high_right = trees[trees.length - 1 - i];
            right++;
        }
    }
    return left > right ? "left" : "right";
}
function strictEqual(arr, b){
    let a = treePhotography(arr);
    if(a !== b){
        console.log(arr, b);
    }else{
        console.log("Pass... All Green!");
    }
}

//console.log(treePhotography([1, 3, 1, 6, 5]));

function tests() {
    strictEqual([1, 2, 3, 6, 5], "left");
    strictEqual([5, 6, 5, 4], "right");
    strictEqual([1, 3, 1, 6, 5], "left");
    strictEqual([1, 1, 2, 2, 2, 2, 3], "left");
    strictEqual([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2], "left");
    strictEqual([3, 3, 3, 3, 2], "right");
    strictEqual([4, 3, 2, 3, 3, 3, 1], "right");
    strictEqual([3, 1, 4, 5, 2, 5, 1], "left");
    strictEqual([4, 3, 3, 4, 3, 1, 3], "right");
    strictEqual([5, 1, 2], "right");
    strictEqual([1, 2, 4, 1, 5, 3, 1], "left");
    strictEqual([1, 1, 1, 4, 1, 3, 5], "left");
    strictEqual([3, 1, 4, 1, 5, 9, 2, 6], "left");
}

tests();