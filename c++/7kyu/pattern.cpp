#include <string>
#include <vector>

#include <string>
#include <vector>

std::string pattern(int n){
  std::string ans;
  for(int i = 0; i < n; i++){
    for(int j = n; j >= n - i; j--)
      ans += std::to_string(j);
    ans += "\n";
  }
  return ans.substr(0, ans.size() - 1);
}

int main(){
  return 0;
}