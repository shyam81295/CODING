#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N;
    cin>>T;
    for(int k=0;k<T;k++)
    {
        string s;
        cin>>s;
        N = s.size();
        stack<char> newstack;
        for(int i=0;i<N;i++)
        {
            if(!newstack.empty() && newstack.top()=='{' && s[i]=='}')
            {
                newstack.pop();
            }
            else if(!newstack.empty() && newstack.top()=='[' && s[i]==']')
            {
                newstack.pop();
            }
            else if(!newstack.empty() && newstack.top()=='(' && s[i]==')')
            {
                newstack.pop();
            }
            else
                newstack.push(s[i]);
        }
        if(newstack.size()==0)  cout<<"balanced"<<endl;
        else cout<<"not balanced"<<endl;
    }
    return 0;
}
