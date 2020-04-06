#include<iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t=0,n,n2,trace=0,r=0,c=0;
    cin>>t;
    for(int k=0;k<t;k++)
    {
        cin>>n;
        n2=n*n;
        int arr[n2];
        for(int i=0;i<n2;i++)
        {
            //cout<<"NUMBER= "<<i<<" ";
            cin>>arr[i];
            if(i%(n+1)==0)
                trace=trace+arr[i];
        }
        cout<<"TRACE: "<<trace<<endl;
        for(int i=0;i<n;i++)
        {   cout<<"ITERATION :"<<i<<endl;
            vector<int> count_r(n, 0);
            vector<int> count_c(n, 0);
            //int count_r[n]={0},count_c[n]={0};
            for(int j=0;j<n;j++)
            {
                //ROWs
                count_r[arr[i+(j*n)]-1]++;
                //COLUMNs
                count_c[arr[(i*n)+j]-1]++;
            }

            for(int a=0;a<n;a++)
            {
                if(count_r[a]>=2)
                {
                    r++;
                    break;
                }
            }

            for(int a=0;a<n;a++)
            {
                if(count_c[a]>=2)
                {
                    c++;
                    break;
                }
            }
              cout<<"COUNT_R: ";
            for(int a=0;a<n;a++)
            {
                cout<<count_r[a];
            }
            cout<<endl;
            cout<<"COUNT_C: ";
            for(int a=0;a<n;a++)
            {
                cout<<count_c[a];
            }
            cout<<endl;
        cout<<"----------ONE DONE---------"<<endl;
        }
        cout<<"HEY";
        cout<<"Case #"<<k+1<<": "<<trace<<" "<<c<<" "<<r<<endl;
        c=0;
        r=0;
        trace=0;
    }
}
