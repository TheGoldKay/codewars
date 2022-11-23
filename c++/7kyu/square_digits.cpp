#include <string>
#include <cstdlib>

int square_digits(int num) {
  std::string n = std::to_string(num);
  std::string ans = "";
  for(auto d: n){
    int x = d - '0';
    ans += std::to_string(x * x);
  }
  return std::stoi(ans);
}