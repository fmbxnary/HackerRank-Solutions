#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string a, b;

    cin >> a >> b;

    cout << a.length() << " " << b.length() << endl;
    cout << a + b << endl;

    char tmp = a[0];
    a[0] = b[0];
    b[0] = tmp;

    cout << a << " " << b << endl;

    return 0;
}
