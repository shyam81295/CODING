#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T,N;
    cin>>T;
    for(int k=0;k<T;k++)
    {
        int N;
        cin>>N;
        int flag = 0;
        int arr[N];
        for(int i=0;i<N;i++)
        {
            cin>>arr[i];
        }
        stack<int> newstack;
        int root = INT_MIN;

        newstack.push(arr[0]);
        for(int i=1;i<N;i++)
        {
            if(arr[i]<root)
            {
                flag = 1;
                break;
            }
            else
            {
                if(!newstack.empty() && (newstack.top() > arr[i]))
                {
                    newstack.push(arr[i]);
                }
                else
                {
                    while(!newstack.empty() && (newstack.top() < arr[i]))
                    {
                        root = newstack.top();
                        newstack.pop();
                    }
                    newstack.push(arr[i]);
                }
            }
        }
        if(flag==1)     cout<<"0"<<endl;
        else    cout<<"1"<<endl;
    }

    return 0;
}
