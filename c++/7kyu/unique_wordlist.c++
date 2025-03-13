#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

string removeDuplicateWords(const string& str)
{
  istringstream ss(str);
  string word;
  vector<string> v;
  ostringstream oss;
  while (ss >> word){
    if (find(v.begin(), v.end(), word) == v.end()){
      v.push_back(word);
    }
  }
  if(!v.empty()){
      oss << v[0];
      for(int i = 1; i < v.size(); ++i){
        oss << " " << v[i];
      }
  }
  return oss.str();
}

int main() { 
    string test = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"; 
    cout << removeDuplicateWords(test) << endl;
    return 0;
}

