#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> filter(vector<int> v, int value){
  vector<int> out;
  for(int i: v){
    if(i != value){
      out.push_back(i);
    }
  }
  return out;
}

std::vector<int> remove_values(std::vector<int> integers, std::vector<int> values) {
  while(values.size()){
    int value = values.back();
    integers = filter(integers, value); 
    values.pop_back();
  }
  return integers;       
}
