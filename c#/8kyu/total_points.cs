using System.Linq;

public static class Kata {
    public static int TotalPoints(string[] games) {
        int total = 0;
        for(int index = 0; index < games.Length; index++)
        {
            string[] pair = games[index].Split(':');
            int a = int.Parse(pair[0]);
            int b = int.Parse(pair[1]);
            total += a > b? 3: a == b? 1: 0;
        }
        return total;
    }
}