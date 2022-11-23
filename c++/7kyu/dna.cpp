#include <string>
#include <iostream>
#include <map>

using namespace std;
std::string DNAStrand(const std::string& dna)
{
  map<char, char> d {{'A', 'T'}, {'T', 'A'}, {'C', 'G'}, {'G', 'C'}};
  string side;
  for(char c: dna){
    side += d[c];
  }
  return side;
}