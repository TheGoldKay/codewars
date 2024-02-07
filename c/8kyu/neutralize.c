#include <stdio.h>
#include <string.h>

void neutralize (const char *s1, const char *s2, char *s3)
{
  int i = 0;
  while(s1[i] != '\0')
  {
    if(s1[i] == s2[i])
    {
        s3[i] = s1[i];
    }else
    {
        s3[i] = '0';
    }
    i++;
  }
  s3[i] = '\0';
}


int main()
{
    const char *s1 = "-++-";
    const char *s2 = "-+-+";
    char *s3;
    neutralize(s1, s2, s3);
    printf("%s\n", s3);
    return 0;
}