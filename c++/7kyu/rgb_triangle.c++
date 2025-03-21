#include <string>
#include <bits/stdc++.h>
#include <map>

// https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/cpp

using namespace std;

map<string, char> rgb {
  {"BG", 'R'},
  {"GB", 'R'},
  {"RG", 'B'},
  {"GR", 'B'},
  {"BR", 'G'},
  {"RB", 'G'},
};

std::string triangle(std::string row_str) {
  if(row_str.length() == 1){
    return row_str;
  }
  string out = "";  
  for(int i = 0; i < row_str.length() - 1; i++){
    if(row_str[i] == row_str[i+1]){
      out += row_str[i];
    }else{
      string pair = row_str.substr(i, 2);
      out += rgb[pair];
    }
  }
  return triangle(out);
}

int main(){
    string row = "RBRGBRBGGRRRBGBBBGG"; // is "G"
    cout << triangle(row) << endl;
    return 0;
}