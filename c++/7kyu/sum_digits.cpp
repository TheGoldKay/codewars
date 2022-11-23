#include <vector>
#include <numeric>
#include <algorithm>

int get_sum(int a, int b)
{
  std::vector<int> v {a, b};
  std::sort(v.begin(), v.end());
  int sum=0;
  for(int i = v[0]; i <= v[1]; i++){
    sum += i;
  }
  return sum;
}