#include <stdio.h>
#include <string.h>

void neutralize (const char *s1, const char *s2, char *s3)
{
  int len = strlen(s1);
  /* s3 = '\0'; */
  if(len > 0)
  {
    for(int i = 0; i < len; i++)
    {
        if(s1[i] == s2[i])
        {
            printf("here\n");
            char str[2];
            str[0] = s1[i];
            str[1] = '\0';
            strcat(s3, str);
            printf("%s\n", s3);
        }else
        {
            strcat(s3, "0");
            printf("here2\n");
        }
    }
  }
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