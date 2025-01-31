#include <stdlib.h>

// Comparison function for integers
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b); // Return difference for ascending order
}

int find_deleted_number(const int arr[], size_t arr_sz, int mix_arr[], size_t mix_sz)
{
    if(mix_sz == arr_sz){
        return 0;
    }else{
        qsort(mix_arr, mix_sz, sizeof(int), compare);
        for(int i = 0; i < mix_sz; i++){
            if(arr[i] != mix_arr[i]){
                return arr[i];
            }
        }
    }
    return arr[arr_sz - 1];
}

int find_deleted_number_BETTER(const int arr[], size_t arr_sz, const int mix_arr[], size_t mix_sz)
{
  int sum = 0;
  for (size_t i = 0; i < arr_sz; i++) sum += arr[i];
  for (size_t i = 0; i < mix_sz; i++) sum -= mix_arr[i];
  return sum;
}