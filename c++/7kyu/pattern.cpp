#include <string>
#include <vector>

#include <string>
#include <vector>

std::string pattern(int n){
  if(n <= 0){
    return "";
  }
  std::string lines;
  int count = 1;
  for(int i = 0; i < n; i++){
    std::string line;
    for(int j = 0; j < count; j++){
      line += std::to_string(n-j);
    }
    lines = lines + line;
    lines = lines + "\n";
    count++;
  }
  lines.erase(lines.length()-1);
  return lines;
}

int main(){
  return 0;
}