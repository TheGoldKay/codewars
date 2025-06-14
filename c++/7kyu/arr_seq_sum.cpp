#include<vector>

using namespace std;

//https://www.codewars.com/kata/5b5e0ef007a26632c400002a/train/cpp

long elementsSum(const std::vector<std::vector<int>>& arr, int d = 0){
  int sum = 0;
  int i = arr.size() - 1;
  for(auto a: arr){
    if (i < a.size() and i >= 0) {
      sum += a[i];
    } else {
      sum += d;
    }
    i--;
  }
  return sum;
}