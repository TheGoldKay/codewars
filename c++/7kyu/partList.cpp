#include <vector>
#include <string>
#include <iostream>

class PartList
{
public:
    static std::vector<std::pair <std::string, std::string>> partlist(std::vector<std::string> &arr);
};

std::string getString(std::vector<std::string> &arr, int start, int end){
    std::string s = "";
    for(int i = start; i < end; i++){
        s += arr[i] + " ";
    }
    s.pop_back();
    return s;
}

std::vector<std::pair <std::string, std::string>> PartList::partlist(std::vector<std::string> &arr){
    int ln = arr.size();
    std::vector<std::pair <std::string, std::string>> plist;
    for(int i = 1; i < ln; i++){
        std::string s = getString(arr, 0, i);
        std::string s2 = getString(arr, i, ln);
        std::pair <std::string, std::string> p = {s, s2};
        plist.push_back(p);
    }
    return plist;
}

int main(){
    std::vector<std::string> arr = {"I", "wish", "I", "hadn't", "come"};
    std::vector<std::pair <std::string, std::string>> plist = PartList::partlist(arr);
    for(auto p : plist){
        std::cout << p.first << std::endl;
        std::cout << p.second << std::endl;
        std::cout << std::endl;
    }
    return 0;
}