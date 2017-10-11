#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N;
    cin>>T;
    for(int k=0;k<T;k++)
    {
        string arr;
        cin>>arr;
        stack<char> s;
        N = arr.size();
        if(N&1)
        {
            cout<<"-1"<<endl;
        }
        else{

        int counter_rev=0;
        for(int i=0;i<N;i++)
        {
            if(s.empty() && arr[i]=='}')
            {
                counter_rev++;
                s.push('{');
            }
            else if(s.empty() && arr[i]=='{')
            {
                s.push('{');
            }
            else if(!s.empty() && s.top()=='{' && arr[i]=='}')
            {
                s.pop();
            }
            else if(!s.empty() && s.top()=='{' && arr[i]=='{')
            {
                s.push('{');
            }
            else if(!s.empty() && s.top()=='}' && arr[i]=='}')
            {
                s.push('}');
            }
        }
        int sz= s.size();
        counter_rev += (sz/2);
        cout<<counter_rev<<endl;

        }
    }
    return 0;
}
