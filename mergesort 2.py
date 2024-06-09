def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        merge(l)
        merge(r)
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr[k]=l[i]
                i+=1
                k+=1
            else:
                arr[k]=r[j]
                j+=1
                k+=1
            
            #only left or only right
        '''while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1'''
arr=[1,8,2,9,4,10,18,15]
print(arr)
merge(arr)
print(arr)
#merge sort
'''def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        p=arr[:mid]
        q=arr[mid:]
        mergesort(p)
        mergesort(q)
        i,j,k=0,0,0
        while i<len(p) and j<len(q):
            if p[i]<=q[j]:
                arr[k]=p[i]
                k+=1
                i+=1
            else:
                arr[k]=q[j]
                k+=1
                j+=1                
        while i<len(p):
            arr[k]=p[i]
            k+=1
            i+=1
        while j<len(q):
            arr[k]=q[j]
            k+=1
            j+=1
arr=[32,11,64,13,17,1,5]
print("array before sorting")
for i in  range(0,len(arr)):
    print(arr[i],end=" ")
print()
mergesort(arr)
print("array after sorting")
for i in range(0,len(arr)):
    print(arr[i],end=" ")'''
