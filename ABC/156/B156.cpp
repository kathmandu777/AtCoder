#include <bits/stdc++.h>
using namespace std;

int main() {
	int K,N;
    cin>>N>>K;
  	double n=(double)N;
  	double k=(double)K;
  	int i;
 	for(i = 0; n>=1.0 ; i++) {
    	n=n/k;
  	}
  	cout<<i<<endl;
}