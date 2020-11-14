#include<bits/stdc++.h>
using namespace std;

int main()
{
    int N,T,a,counter,p;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        cin>>N;
        int arr[N];
        vector<vector<int> > counts(32);
        for(int i=0;i<N;i++)
        {
            cin>>arr[i];
            a = arr[i];
            counter = 0;
            while(a!=0)
            {
                if(a&1)
                    counter++;
                a>>=1;
            }
            counts[counter].push_back(arr[i]);
        }
        for(int i=31;i>=0;i--)
        {
            p = counts[i].size();
            for(int j=0;j<p;j++)
            {
                cout<<counts[i][j]<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}
