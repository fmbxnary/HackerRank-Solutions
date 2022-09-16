#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define MAX 10000
using namespace std;

int main()
{
    int COUNT{}, a[MAX]{};
    cin >> COUNT;
    for (int i{}; i < COUNT; i++)
    {
        cin >> a[i];
    }
    for (int i = COUNT - 1; i >= 0; i--)
    {
        cout << a[i] << " ";
    }
    return 0;
}
