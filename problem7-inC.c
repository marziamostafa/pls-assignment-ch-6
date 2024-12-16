
#include <stdio.h>

void updateValue(int *ptr)
{
    *ptr = 20; // Update the value at the memory address
}

int main()
{
    int value = 10;
    printf("Before: %d\n", value);
    updateValue(&value);
    printf("After: %d\n", value);
    return 0;
}