using System;
public class Kata
{
  public static int[] DifferenceInAges(int[] ages)
  {
    Array.Sort(ages);
    return new int[] {ages[0], ages[ages.Length-1], ages[ages.Length-1] - ages[0]};
  }
}