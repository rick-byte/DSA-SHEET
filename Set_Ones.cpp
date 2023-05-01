#include<bits/stdc++.h>
using namespace std;

set<int> countRow(vector<vector<int>> &arr)
{
    set<int> v1;
    
    
    for(int i=0; i<arr.size(); i++)
    {
        for(int j=0; j<arr[i].size(); j++)
        {
            if(arr[i][j]==1){
                v1.insert(i);
            }
        }
    }
    
    return v1;
}

set<int> countCol(vector<vector<int>> &arr)
{
    set<int> v2;
    
    for(int i=0; i<arr.size(); i++)
    {
        for(int j=0; j<arr[i].size(); j++)
        {
            if(arr[i][j]==1){
                v2.insert(j);
            }
        }
    }
    
    return v2;
    
}

void setOnes(vector<vector<int>> &arr)
{
     set<int> row = countRow(arr);
    set<int> col = countCol(arr);
    
    auto itr1 =  row.begin();
    auto itr2 =  col.begin();
    
    while(itr1!=row.end()){
       for(int i=0; i<arr[*itr1].size(); i++){
           arr[*itr1][i]=1;
       }
        ++itr1;
    }cout<<endl;
    
    while(itr2!=col.end()){
       for(int i=0; i<arr.size(); i++){
           arr[i][*itr2]=1;
       }
        ++itr2;
    }cout<<endl;
    
}

int main() {
  vector < vector < int >> arr;
  
  
  arr = {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}};
  
   cout<<"The Initial Matrix is "<<endl;
   
  for (int i = 0; i < arr.size(); i++) {
    for (int j = 0; j < arr[0].size(); j++) {
      cout << arr[i][j] << " ";
    }
    cout << "\n";
  }
 setOnes(arr);
  cout<<"The Final Matrix is "<<endl;
  for (int i = 0; i < arr.size(); i++) {
    for (int j = 0; j < arr[0].size(); j++) {
      cout << arr[i][j] << " ";
    }
    cout << "\n";
  }
}
