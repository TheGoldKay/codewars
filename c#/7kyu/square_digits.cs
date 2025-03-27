using System;

public class Kata
{
  public static string SquareDigits(int n)
  {
    string ans = "";
    foreach (var x in n.ToString())
    {
		  int d = int.Parse(x.ToString());
      ans += (d * d);
    }
	  return ans;
  }
}

