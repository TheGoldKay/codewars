#include <vector>
#include <cmath>
#include <iostream>

std::vector<double> distancesFromAverage(std::vector<int> input){
  std::vector<double> dist;
  double avg(0);
  for(auto n: input){
    avg += n;
  }
  avg = avg / input.size();
  for(auto n: input){
    double d = std::ceil((avg - n) * 100.0) / 100.0;
    dist.push_back(d);
  }
  return dist;
}

int main(){
  double n1 = 1.94;
  double d = std::round(n1 * 10) / 10;
  std::cout << d << std::endl;
  return 0;
}