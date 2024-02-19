using System;

void SumOfDifferences(int[] arr)
{
    int sum = 0;
    Array.Sort(arr);
    for(int i = arr.Length - 1; i > 0; i--)
    {
        sum += (arr[i] - arr[i-1]);
    }
    Console.WriteLine(sum);
}

int[] arr = {2, 1, 10};
SumOfDifferences(arr);