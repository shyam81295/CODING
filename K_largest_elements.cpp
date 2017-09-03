#include<bits/stdc++.h>
using namespace std;

int QuickPartition(int *arr, int i, int j, int pivotIndex)
{
    int t1 = arr[pivotIndex];
    arr[pivotIndex] = arr[j];
    arr[j] = t1;

    int r = i-1;
    int x = arr[j];

    for(int q = i;q<j;q++)
    {
        if(arr[q]<=x)
        {
            r++;
            int t2 = arr[r];
            arr[r] = arr[q];
            arr[q] = t2;
        }
    }
    int t3 = arr[r+1];
    arr[r+1] = arr[j];
    arr[j] = t3;

    return (r+1);
}

int FindRankRandom(int *arr, int i, int j, int rank_g)
{
    if(i==j)    return i;
    int pivotIndex = i+rand()%(j-i+1);
    int k = QuickPartition(arr,i,j,pivotIndex);
    if(rank_g == (j-k+1))
        return k;
    else if(rank_g < (j-k+1))
        FindRankRandom(arr,k+1,j,rank_g);
    else
        FindRankRandom(arr,i,k-1,rank_g - (j-k+1));
}

int main()
{
    int N,K;
    cin>>N>>K;
    int arr[N];
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
    }
    int val = FindRankRandom(arr,0,N-1,K);
    for(int i=val;i<N;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
