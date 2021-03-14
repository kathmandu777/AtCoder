#include <bits/stdc++.h>
using namespace std;

int main() {
    
    

    vector<int> BingoCard(9);
    for (int i = 0; i < 9; i++) {
        cin >> BingoCard.at(i);
    }
  
    int N;
    cin>>N;

    vector<int> atari(N);
    for (int i = 0; i < N; i++) {
      cin >> atari.at(i);
    }

    for(int i=0;i<N;i++){
        for(int j=0;j<9;j++){
            if(atari.at(i) == BingoCard.at(j)){
                BingoCard.at(j)=0;
            }
        }
    }

    if(BingoCard.at(0)==0 && BingoCard.at(1)==0 && BingoCard.at(2)==0){
        cout<<"Yes"<<endl;
    }
    else if(BingoCard.at(3)==0 && BingoCard.at(4)==0 && BingoCard.at(5)==0){
        cout<<"Yes"<<endl;
    }
    else if(BingoCard.at(6)==0 && BingoCard.at(7)==0 && BingoCard.at(8)==0){
        cout<<"Yes"<<endl;
    }
    else if(BingoCard.at(0)==0 && BingoCard.at(3)==0 && BingoCard.at(6)==0){
        cout<<"Yes"<<endl;
    }
    else if(BingoCard.at(1)==0 && BingoCard.at(4)==0 && BingoCard.at(7)==0){
        cout<<"Yes"<<endl;
    }
    else if(BingoCard.at(2)==0 && BingoCard.at(5)==0 && BingoCard.at(8)==0){
        cout<<"Yes"<<endl;
    }
    else if(BingoCard.at(0)==0 && BingoCard.at(4)==0 && BingoCard.at(8)==0){
        cout<<"Yes"<<endl;
    }
    else if(BingoCard.at(2)==0 && BingoCard.at(4)==0 && BingoCard.at(6)==0){
        cout<<"Yes"<<endl;
    }
    else{
        cout<<"No"<<endl;
    }

}
