#a=[1,3,6,7,9,5,2]
'''def peek(a):
    first=0
    last=len(a)-1
    while first<=last:
        mid=(first+last)//2
        if a[mid]>=a[mid-1] and a[mid]>=a[mid+1]:
            return a[mid]
        elif a[mid]<a[mid-1]:
            last=mid-1
        else:
            first=mid+1
    return -1
    
a=[1,3,6,7,9,5,2]
b=peek(a)
print(b)'''
a=[1,3,6,7,9,5,2]
f=0
l=len(a)-1
ans=0
while f<=l:
    mid=f+(l-f)//2
    if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
        ans=a[mid]
        break        
    elif a[mid]<a[mid-1]:
        l=mid-1
    else:
        f=mid+1
print(ans)    

