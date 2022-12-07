def check_pair_HASHMAP(a,n,sum):
    hashmap = {}
    
    for i in range(0,n):
        temp = sum - a[i]
        if(temp in hashmap):
            return True
        
        hashmap[a[i]]=i
        
    return False 
        
def check_pair_POINTER(a,n,x):
    a.sort()
    
    l =0
    r = n-1
    
    while l<r:
        if a[l]+a[r]>x:
            r=r-1
        elif a[l]+a[r]<x:
            l=l+1
        else:
            return True
    
    
    return False

def check_pair_NAIVE(a,n,x):
    for i in range (0,n-1):
        for j in range(i+1,n):
            if a[i]+a[j]==x:
                return True
                
    
    return False



if __name__ == "__main__":
    
   a=[]
n=int(input("Number of elements in array:"))
x = int(input("sum :"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)

if (check_pair_HASHMAP(a,n,x)):
    print(True)
else :
    print(False)
