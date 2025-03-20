#include <string>
#include <set>
#include <iostream>

bool hasUniqueChars(std::string s) {
  std::set<char> chars(s.begin(), s.end());
  return chars.size() == s.length();
}

int main(){
    std::string s = "abcdef";
    std::cout << hasUniqueChars(s) << std::endl;
    return 0;
}