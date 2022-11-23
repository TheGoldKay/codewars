class Printer
{
public:
    static std::string printerError(const std::string &s){
      int wrong = 0; 
      for(int c: s){
        if(!(c >= 97 and c <= 109)){
          wrong++;
        }
      }
      return std::to_string(wrong) + "/" + std::to_string(s.size());
    }
};
