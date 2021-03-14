
#include <bits/stdc++.h>
using namespace std;

int main()
{
    unsigned int a, r, n, ans;
    cin >> a >> r >> n;
    ans = abs((a * pow(r, (n - 1))));

    if (ans > 1000000000)
    {
        cout << "large" << endl;
    }
    else if (ans == 0)
    {
        cout << "large" << endl;
    }
    else
    {
        cout << ans << endl;
    }
}
