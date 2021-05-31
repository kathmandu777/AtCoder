#include <bits/stdc++.h>
using namespace std;
#include <list>
#include <iostream>

int main()
{

    int n;
    cin >> n;

    list<int> vec;
    for (int i = 0; i < n; i++)
    {
        cin >> i;
        vec.push_back(i);
    }

    for (int i = 1; i < n; i++)
    {
        vec.remove(i);
        cout << n - vec.size() << endl;
    }
    cout << 0 << endl;
}
