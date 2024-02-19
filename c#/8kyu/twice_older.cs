namespace Solution
{
  public class TwiceAsOldSolution
  {
    public static int TwiceAsOld(int dadYears, int sonYears, int count = 0)
    {
      // THIS IS A BETTER ANSWER: return Math.Abs(dadYears - sonYears * 2);
      int half = sonYears * 2 - dadYears;
      if(half == 0)
      {
        return count;
      }
      else if(half > 0)
      {
        return TwiceAsOld(dadYears - 1, sonYears - 1, count + 1);
      }else 
      {
        return TwiceAsOld(dadYears + 1, sonYears + 1, count + 1);
      }
    }
  }
}