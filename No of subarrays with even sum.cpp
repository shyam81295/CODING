#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N,a;
    cin>>T;
    for(int k=0;k<T;k++)
    {
        cin>>N;
        int arr[N];
        int ceven=1;
        int codd=0;
        for(int i=0;i<N;i++)
        {
            cin>>a;
            arr[i] = a%2;
        }
        for(int i=1;i<N;i++)
        {
            arr[i] = (arr[i-1]+arr[i])%2;
        }
        for(int i=0;i<N;i++)
        {
            if(arr[i]&1)
            {
               codd++;
            }
            else
                ceven++;
        }
        codd = (codd*(codd-1))/2;
        ceven = (ceven*(ceven-1))/2;
        cout<<codd+ceven<<endl;
    }
    return 0;
}
