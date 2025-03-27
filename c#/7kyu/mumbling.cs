using System;

public class Accumul 
{
	public static String Accum(string s) 
  {
    string acc = "";
    int count = 0;
    foreach(char c in s){
      acc += c.ToString().ToUpper();
      for(int i = 0; i < count; i++){
        acc += c.ToString().ToLower();
      }
      acc += "-";
			count++;
    }
    return acc.TrimEnd('-'); 
  }
}
