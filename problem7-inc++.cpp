#include <iostream>
using namespace std;

void updateValue(int *ptr)
{
    *ptr = 30; // Update the value at the memory address
}

int main()
{
    int value = 10;
    cout << "In c++ :" << endl;
    cout << "Before: " << value << endl;
    updateValue(&value);
    cout << "After: " << value << endl;
    return 0;
}