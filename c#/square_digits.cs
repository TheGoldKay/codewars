using System;

public class Kata
{
  public static void Main()
  {
	int n = 12;
    string ans = "";
    foreach (var x in n.ToString())
    {
		int d = int.Parse(x.ToString());
        ans += (d * d);
    }
	Console.WriteLine(ans);
  }
}

//Console.WriteLine(Kata.SquareDigits(9119));