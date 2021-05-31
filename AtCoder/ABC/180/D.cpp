#include <bits/stdc++.h>
using namespace std;

int main()
{
    unsigned long long x, y, a, b, exp;
    cin >> x >> y >> a >> b;
    exp = 0;

    unsigned long long pa = x * a;
    unsigned long long pb = x + b;
    if (pa > pb)
    {
        int p = y / (x + b);
        exp = p;
        x = x + b * p;
    }
    else
    {
        int p = b / (a - 1);
        int q = p / (a * x);
        x = x * a * q;
        exp = q;
    }
    while (y > x)
    {
        unsigned long long pa = x * a;
        unsigned long long pb = x + b;
        if (pa > pb)
        {
            x = pb;
        }
        else
        {
            x = pa;
        }
        exp++;
    }
    cout << exp - 1 << endl;
}