//  This Algorithm will give kth largest element in O(n) average.
#include<bits/stdc++.h>
using namespace std;

int QuickPartition(int *arr, int i, int j, int pivotIndex)
{
    int t1 = arr[pivotIndex];
    arr[pivotIndex] = arr[j];
    arr[j] = t1;

    int q;
    int r = i-1;
    int x = arr[j];

    for(q = i; q < j; q++)
    {
        if(arr[q] <= x)
        {
            r++;

            int t2 = arr[q];
            arr[q] = arr[r];
            arr[r] = t2;
        }
    }
    int t3 = arr[r+1];
    arr[r+1] = arr[j];
    arr[j] = t3;

    return (r+1);
}

int FindRankRandom(int *arr, int i, int j, int rank_g)
{
    if(i==j)    return arr[i];
        int pivotIndex = i + rand()%(j-i+1);
        int k = QuickPartition(arr, i,j,pivotIndex);
        if(rank_g == (j-k+1))
            return arr[k];
        else if(rank_g < (j-k+1))
            FindRankRandom(arr,k+1,j,rank_g);
        else
            FindRankRandom(arr,i,k-1,(rank_g - (j-k+1)));
}

int main()
{
    int N,T,t;
    cin>>N;
    int arr[N];
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
    }
    cin>>T;
    for(int i = 0;i<T;i++)
    {
        cin>>t;
        cout<<FindRankRandom(arr,0,N-1,t)<<endl;
    }
    return 0;
}
