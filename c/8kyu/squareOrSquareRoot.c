int* squareOrSquareRoot(int* array, int length)
{
    int* arr = malloc(length * sizeof(int));
    for (int i = 0; i < length; i++)
    {
        float s1 = sqrt(array[i]);
        int s2 = sqrt(array[i]);
        if(s2 == s1)
        {
            arr[i] = s2;
        }else{
            arr[i] = pow(array[i], 2); 
        }
    }
    return arr;
}