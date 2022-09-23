#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string s;
    cin >> s;

    replace(s.begin(), s.end(), ',', '\n');

    cout << s << endl;
    return 0;
}
