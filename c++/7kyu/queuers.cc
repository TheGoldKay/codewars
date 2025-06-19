#include<vector>

long long queue(const std::vector<int>& queuers, int pos){
  std::vector<int> v = queuers;
  int i = 0;
  int time = 0;
  while(v[pos] != 0){
    if(v[i] > 0){
      v[i]--;
      time++;
    }
    if(++i == v.size()) i = 0;
  }
  return time;
}