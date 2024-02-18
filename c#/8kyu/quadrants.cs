using System;

public static class Kata
{
  public static int Quadrant(int x, int y)
  {
    string qx, qy;
    string r = "right", l = "left", u = "up", d = "down";
    qx = x > 0? r: l;
    qy = y > 0? u: d;
    if (qy == u)
    {
        if (qx == r)
        {
            return 1;
        }
        else 
        {
            return 2;
        }
    }
    else 
    {
        if (qx == l)
        {
            return 3;
        }
        else 
        {
            return 4;
        }
    }
  }
}