#include <stdio.h>
#include <stdlib.h>

unsigned long long to_binary(unsigned short num)
{
    int arr[100];
    int index = 0;
    unsigned long long bin = 0ull;
    while (num != 0)
    {
        unsigned long long mod = num % 2;
        arr[index] = mod;
        num = num / 2;
        index++;
    }
    for (int i = index - 1; i >= 0 ; i--)
    {
        bin = bin * 10ull + arr[i];
    }
    return bin;
}

int main()
{
    unsigned short num;
    printf("Enter a number: ");
    scanf("%hu", &num);
    unsigned long long bin = to_binary(num);
    printf("%ull\n", bin);
}