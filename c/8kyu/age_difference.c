#include <stdlib.h>

int *difference_in_ages(size_t a, int ages[a]) {
    int *res = malloc(sizeof(int) * 3);
    res[0] = ages[0];
    res[1] = ages[0];
    for (int i = 0; i < a; i++){
        if (ages[i] < res[0]){
            res[0] = ages[i];
        }else if(ages[i] > res[1]){
            res[1] = ages[i];
        }
    }
    res[2] = res[1] - res[0];
    return res;
}