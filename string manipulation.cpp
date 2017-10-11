#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N;
    cin>>T;
    for(int k=0;k<T;k++)
    {
        cin>>N;
        string s;
        stack<string> newstack;
        for(int i=0;i<N;i++)
        {
            cin>>s;
            if(!newstack.empty() && newstack.top() == s)
            {
                newstack.pop();
            }
            else
                newstack.push(s);
        }
        cout<<newstack.size()<<endl;
    }
    return 0;
}
