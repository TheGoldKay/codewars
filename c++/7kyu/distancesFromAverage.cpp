#include <vector>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <numeric>

double round100(double n) {
  return std::round(n * 100) / 100;
}

std::vector<double> distancesFromAverage(std::vector<int> input)
{
  double average = std::accumulate(input.begin(), input.end(), 0) / static_cast<double>(input.size());
  std::vector<double> result(input.size(), 0);
  std::transform(input.cbegin(), input.cend(), result.begin(), [&](auto a) { return round100(average - a); });
  return result;
}

int main(){
  double n1 = 1.94;
  double d = std::round(n1 * 10) / 10;
  std::cout << d << std::endl;
  return 0;
}