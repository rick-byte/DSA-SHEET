
def Moore_vooting(arr,size):

# yet cant understand this code 
    maj = 0 # we will maintain a the index where majority element is there
    count =1 
    
    for i in range(1,size):
        if arr[maj]==arr[i]:
            count=count+1   
        else:
            count=count-1
            
        if count==0:
            maj = i
            count=1
        
        print(arr[maj]," ",maj," ",count)
    
    if arr[maj]>=size//2:
        print(True)
    else:
        print(False)
 
def check_pair_HASHMAP(arr,size):
    
    m = {}
    for i in range(size):
          if arr[i] in m:
            m[arr[i]] += 1
          else:
            m[arr[i]] = 1
        
    count = 0
    for key in m:
        if m[key] > size / 2:
            count = 1
            print("Majority found :-",key)
            break
    if(count == 0):
        print("No Majority element")
  
 
if __name__ == "__main__":
    
 
 a=[]
n=int(input("Number of elements in array:"))
#x = int(input("sum :"))
for i in range(0,n):
   l=int(input())
   a.append(l)
print(a)
#check_pair_HASHMAP(a,n)
#Moore_vooting(a,n)
brute_force(a,n)
