#include <bits/stdc++.h>
using namespace std;
#include <iostream>
#include <numeric>

int main()
{

    int k;
    int sum = 0;
    cin >> k;
    for (int i = 1; i <= k; i++)
    {
        for (int j = 1; j <= k; j++)
        {
            for (int n = 1; n <= k; n++)
            {
                sum += std::gcd(n, std::gcd(i, j))
            }
        }
    }
    cout << sum << endl;
}
