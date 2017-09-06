/*  Implementation of Stack using array */
#include<bits/stdc++.h>
#define STACKSIZE 100
using namespace std;

int top = -1;

void push(int *arr, int x)
{
    if(top==STACKSIZE)
    {
        cout<<"Stack Overflow"<<endl;
        return;
    }
    top++;
    arr[top] = x;
}

int pop(int *arr)
{
    if(top==-1)
    {
        cout<<"Stack underflow"<<endl;
        return -1;
    }
    return arr[top--];
}

int peek(int *arr)
{
    if(top==-1)
    {
        cout<<"Stack underflow"<<endl;
        return -1;
    }
    return arr[top];
}

bool isEmpty(int *arr)
{
    if(top==-1) return true;
    else return false;
}

void print_stack(int *arr)
{
    if(isEmpty(arr))
    {
        cout<<"Stack is empty"<<endl;
    }
    else
    {
        for(int i=0;i<=top;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
}

int main()
{
    int arr[STACKSIZE];
    push(arr,9);
    print_stack(arr);

    push(arr,1);
    print_stack(arr);

    push(arr,4);
    print_stack(arr);

    pop(arr);
    print_stack(arr);
    pop(arr);
    print_stack(arr);
    pop(arr);
    print_stack(arr);
    pop(arr);
    print_stack(arr);
    return 0;
}


