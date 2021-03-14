#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C;
    cin>>A>>B>>C;
    if(A==B){
        if (B==C)
        {
            if (C==A)
            {
                cout<<"No"<<endl;//A=B=C
            }
        }
        else
        {
            cout<<"Yes"<<endl;//A=B
        }
        
    }
    else
    {
        if(B==C)
        {
            cout<<"Yes"<<endl;//B=C
        }
        else if(A==C)
        {
            cout<<"Yes"<<endl;//A=C
        }
        else
        {
            cout<<"No"<<endl;
        }
        
    }
    
    

}
