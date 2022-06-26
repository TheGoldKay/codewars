#include <vector>
#include <iostream>
#include <algorithm>

bool isAllPossibilities(std::vector<int> arr){
  int ln = arr.size();
  if(ln <= 1){
    if(arr[0] == 0){
      return true;
    }
    return false;
  }
  int max = *std::max_element(arr.begin(), arr.end());
  int min = *std::min_element(arr.begin(), arr.end());
  std::cout << min << " " << max << std::endl;
  return min == 0 and ln == max+1;
}

std::vector<int> v = {1, 2};

int main(){
  isAllPossibilities(v);
  return 0;
}
