#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

string removeDuplicateWords(const string& str)
{
  stringstream ss(str);
  string word;
  vector<string> v;
  string out;
  while (ss >> word){
    if (find(v.begin(), v.end(), word) == v.end()){
      v.push_back(word);
    }
  }
  for(auto i: v){
    out += i;
    out += " ";
  }
  out.pop_back();
  return out;
}

int main() { 
    string test = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"; 
    cout << removeDuplicateWords(test) << endl;
    return 0;
}

