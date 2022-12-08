
from collections import Counter


def using_lib(arr,n):
    
    count_map = Counter(arr)
    
    for i in range(0,n):
        if count_map[i]%2!=0:
            print("answer = ",i)
            break
  
  
 def hashing(arr,n):
    
    hashmap = {}
    
    for i in range (0,n):
       hashmap[arr[i]]=hashmap.get(arr[i],0)+1
       
       
    for i in hashmap:
        if(hashmap[i]%2!=0):
            print("answer = ",i)
            break
  
 
if __name__ == "__main__":
    
 
 a=[]
n=int(input("Number of elements in array:"))
#x = int(input("sum :"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)

#hashing(a,n)
using_lib(a,n)
