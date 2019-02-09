# Algorithm_Rizwan
Algorithm based problems

#include<iostream>
#include<stdio.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int z,q,i,y;
    int c = 1;
    string x;
start:
    scanf("%d %d",&z,&q); //z for how many elements & q for number of queries

    if(z!=0&&q!=0)
    {
        x=x+"CASE# " + to_string(c) +":"+"\n";
        c=c+1;
        y=q;
        int arr[z] = {};
        for(i=0; i<z; i++)
        {
            scanf("%d",&arr[i]);
        }
        sort(arr,arr+z);
query:
        int n;
        y = y-1;
        scanf("%d",&n);
        int l = 0;
        int h = z;
        int m;
        while(l<=h)
        {
            m = (l + h)/2;
            if(n == arr[m])
            {
                break;
            }
            if(n < arr[m])
            {
                h = m-1;
            }
            else
            {
                l = m+1;
            }
        }
        if(l>h)
        {
            x= x+to_string(n)+" not found\n";
        }
        else
        {
            x = x +to_string(n)+" found at " + to_string(m+1)+"\n";
        }
        if(y!=0)
            goto query;
        if(y==0)
            goto start;
    }
    cout<<x<<endl;
    return 0;
}

