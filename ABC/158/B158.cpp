#include <bits/stdc++.h>
using namespace std;
#include <iostream>

int main() {
    int A,B,N;
    cin>>N>>A>>B;
    double C=A+B;
    if(A==0){
        cout<<0<<endl;
        std::exit(0);	
    }
    else if(B==0){
        cout<<A<<endl;
        std::exit(0);	
    }

    vector<int> vec(C*ceil(N/C));

    int count=0;
    for(int j=0;j<ceil(N/C);j++){
        
        for (int i = 0; i <A ; i++) {
            vec.at(i+count)=0;
        }   
        for (int i = A; i <C ; i++) {
            vec.at(i+count)=1;
        }  
        count+=C;
    }
    

    int sum=0;
    for(int i=0;i<N;i++){
        if(vec.at(i)==0){
            sum++;
        }
    }
    cout<<sum<<endl;
}
