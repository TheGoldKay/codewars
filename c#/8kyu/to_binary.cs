using System;


int to_binary(int n)
{
  return int.Parse(Convert.ToString(n, 2));
}

Console.Write("Enter a numnber: ");
int n = int.Parse(Console.ReadLine());
Console.WriteLine(String.Format("{0} in binary is {1}", n, to_binary(n)));
