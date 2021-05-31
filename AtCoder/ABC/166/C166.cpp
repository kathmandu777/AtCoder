#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> h(N);
    for (int i = 0; i < N; i++)
    {
        cin >> h.at(i);
    }

    vector<int> li(N);
    for (int i = 0; i < N; i++)
    {
        if (i % 2 != 0)
        {
            cin >> li.at(i) >> li.at(i + 1);
        }
    }
}
