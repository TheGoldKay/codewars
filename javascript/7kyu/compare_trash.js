function compareTrash(trash1, trash2){
    if(typeof trash1 == typeof trash2){
        return trash1 == trash2;
    }
    return Object.is(trash1, trash2); 
} 

function compareTrash2(trash1, trash2){
    return typeof trash1 == typeof trash2 &&  trash1 == trash2;
}