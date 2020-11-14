#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N;
    int x,y,z;
    cin>>T;
    string s;
    for(int k=0;k<T;k++)
    {
        cin>>s;
        stack<int> newstack;
        N = s.size();
        for(int i=0;i<N;i++)
        {
            if(s[i]>='0' && s[i]<='9')
            {
                newstack.push(s[i]-'0');
            }
            else
            {
                x = newstack.top();
                newstack.pop();
                y = newstack.top();
                newstack.pop();

                if(s[i]=='+')
                {
                    z = x+y;
                }
                else if(s[i]=='-')
                {
                    z = y-x;
                }
                else if(s[i]=='*')
                {
                    z = y*x;
                }
                else if(s[i]=='/')
                {
                    z = y/x;
                }
                else if(s[i]=='%')
                {
                    z = y%x;
                }
                else if(s[i]=='^')
                {
                    z = y^x;
                }
                newstack.push(z);
            }
        }
        cout<<newstack.top()<<endl;
    }
    return 0;
}
