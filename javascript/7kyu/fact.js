function factorial(n)
{
  if(n < 0 || n > 12)
    {
      throw RangeError;
    }
  f = 1;
  for(var i = 1; i <= n; i++)
    {
      f *= i;
    }
  return f;
}