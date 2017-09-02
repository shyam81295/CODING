#include<bits/stdc++.h>
using namespace std;

int QuickPartition(int *arr, int i, int j, int pivot)
{
    int t = arr[pivot];
    arr[pivot] = arr[j];
    arr[j] = t;

    int r = i-1;
    int q;
    int x = arr[j];
    for(q = i; q<j; q++)
    {
        if(arr[q]<=x)
        {
            r++;
            int m = arr[r];
            arr[r] = arr[q];
            arr[q] = m;
        }
    }
    int t2 = arr[r+1];
    arr[r+1] = arr[j];
    arr[j] = t2;
    return r+1;
}

void RandomQS(int *arr, int i, int j)
{
    if(i<j){
        int pivot = i + (rand()%(j-i+1)) ;
        int k = QuickPartition(arr, i, j, pivot);
        RandomQS(arr,i,k-1);
        RandomQS(arr,k+1,j);
    }
}

int main()
{
    int N;
    cin>>N;
    int arr[N];
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
    }
    RandomQS(arr,0,N-1);
    for(int i=0;i<N;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
