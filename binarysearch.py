
class Binear:
    def binarySearch(self,target,arr,n):
        start=0
        end=n-1
        while(start<=end):
            mid=int(start+end-start/2)
            if target<arr[mid]:
                end=mid-1
            #for descending order
           #if target>arr[mid]:
                #end = mid -1
                
            elif target>arr[mid]:
                start=mid+1
            #for descending order
           #elif target<arr[mid]:
                #start = mid +1
            else:
                return mid
obj=Binear()
n=int(input("Enter the length of the list :"))
arr=[]
print("Enter the elements to be inserted into the list in ascending order:")
for i in range(n):
    arr.append(int(input()))
target=int(input("Enter the target element:"))
result=obj.binarySearch(target,arr,n)
print(result)
