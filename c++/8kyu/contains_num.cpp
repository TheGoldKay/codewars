#include <vector>
#include <string>

bool check(const std::vector<std::string>& seq, const std::string& elem) {
    for(std::string c: seq){
      if(c == elem){
        return true;
      }
    }
    return false;
}