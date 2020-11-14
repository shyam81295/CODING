#include<bits/stdc++.h>
using namespace std;

int QuickPartition(int *arr, int i, int j, int pivot)
{
    int t1 = arr[pivot];
    arr[pivot] = arr[j];
    arr[j] = t1;

    int q;
    int r = i-1;
    int x = arr[j];

    for(q = i; q<j ;q++)
    {
        if(arr[q]<=x)
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
    int k = QuickPartition(arr,i,j,pivotIndex);
    if(rank_g == (k-i+1))   return arr[k];
    else if(rank_g < (k-i+1))
        FindRankRandom(arr,i,k-1,rank_g);
    else
        FindRankRandom(arr,k+1,j,(rank_g-(k-i+1)));
}

int QuickPartition2(vector<pair<int,int> >& arr, int i, int j, int pivotIndex)
{
    pair<int,int> t1 = arr[pivotIndex];
    arr[pivotIndex] = arr[j];
    arr[j] = t1;

    int q;
    int r = i-1;
    pair<int,int> x = arr[j];

    for(q = i; q<j ;q++)
    {
        if(arr[q]<=x)
        {
            r++;
            pair<int,int> t2 = arr[q];
            arr[q] = arr[r];
            arr[r] = t2;
        }
    }
    pair<int,int> t3 = arr[r+1];
    arr[r+1] = arr[j];
    arr[j] = t3;
    return (r+1);
}

int FindRankRandom2(vector<pair<int,int> >& arr, int i, int j, int rank_g)
{
    if(i==j)    return i;
    int pivotIndex = i + rand()%(j-i+1);
    int k = QuickPartition2(arr,i,j,pivotIndex);
    if(rank_g == (k-i+1))   return k;
    else if(rank_g < (k-i+1))
        FindRankRandom2(arr,i,k-1,rank_g);
    else
        FindRankRandom2(arr,k+1,j,(rank_g-(k-i+1)));
}


int main()
{
    int N,K;
    cin>>N>>K;
    int arr[N];
    vector<pair<int,int> > brr;
    for(int i=0;i<N;i++)
    {
        cin>>arr[i];
    }
    int median = FindRankRandom(arr,0,N-1,N/2);
    for(int i=0;i<N;i++)
    {
        brr.push_back(make_pair(abs(arr[i]-median),arr[i]));
    }
    int pos = FindRankRandom2(brr,0,N-1,K);
    for(int i=0;i<=pos;i++)
    {
        cout<<brr[i].second<<" ";
    }
    return 0;
}
