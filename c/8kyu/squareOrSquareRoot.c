int* squareOrSquareRoot(int* array, int length)
{
    int* arr = malloc(length * sizeof(int));
    for (int i = 0; i < length; i++)
    {
        float s1 = sqrt(array[i]);
        if(s1 == floor(s1))
        {
            arr[i] = s1;
        }else{
            arr[i] = pow(array[i], 2); 
        }
    }
    return arr;
}