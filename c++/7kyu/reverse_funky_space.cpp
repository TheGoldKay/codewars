#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solve(string s){
  string out;
  vector<int> empty;
  for(int i = 0; i < s.length(); i++){
    if (s[i] == ' '){
      empty.push_back(i);
    }else{
      out = s[i] + out;
    }
  }
  int offset = 0;
  for (int i: empty){
    out.insert(i , " ");
    offset++; 
  }
  return out;
}

int main() {
  string input = "Hello World";
  string result = solve(input);
  cout << "Reversed string with spaces: " << result << endl;
  return 0;
}