#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int j=0;j<T;j++)
    {
        stack< pair<int,int> > newstack;
    int N;
    cin>>N;
    int arr[N],brr[N];
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
    }

    //push 1st element
    newstack.push(make_pair(arr[0],0));

    for(int i=1;i<N;i++)
    {
        if(!newstack.empty() && ((newstack.top().first) > arr[i]))
        {
            newstack.push(make_pair(arr[i],i));
        }
        else
        {
            while(!newstack.empty() && ((newstack.top().first) < arr[i]))
            {
                brr[newstack.top().second] = arr[i];
                newstack.pop();
            }
            newstack.push(make_pair(arr[i],i));
        }
    }

    while(!newstack.empty())
    {
        brr[newstack.top().second] = -1;
        newstack.pop();
    }

    for(int i=0;i<N;i++)
    {
        cout<<brr[i]<<" ";
    }
    cout<<endl;
    }
    return 0;
}
