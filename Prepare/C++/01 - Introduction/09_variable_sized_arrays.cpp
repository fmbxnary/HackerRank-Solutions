#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n{}, q{};
    vector<vector<int>> a{};

    cin >> n >> q;

    for (int i = 0; i < n; i++)
    {

        vector<int> v1{};
        int count{};
        cin >> count;

        for (int j = 0; j < count; j++)
        {
            int value;
            cin >> value;
            v1.push_back(value);
        }
        a.push_back(v1);
    }

    for (int i = 0; i < q; i++)
    {
        int j, k;
        cin >> j >> k;
        cout << a[j][k] << endl;
    }

    return 0;
}
