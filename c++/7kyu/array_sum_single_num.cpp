#include <bits/stdc++.h>

//https://www.codewars.com/kata/59f11118a5e129e591000134/train/cpp

int repeats(std::vector<int> v){
  int sum = 0;
  for(int num: v){
    sum += std::count(v.begin(), v.end(), num) == 1 ? num : 0;
  }
  return sum;
}