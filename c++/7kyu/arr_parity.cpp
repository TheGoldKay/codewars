#include <vector>
#include <numeric> 
#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int solve (std::vector<int> v){
  // remove duplicates
  set<int> s(v.begin(), v.end());
  // single out the number with no pair
  return accumulate(s.begin(), s.end(), 0);
}