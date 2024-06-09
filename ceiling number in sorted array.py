#a=[1,3,6,9,10,14,18]



'''a=[1,3,6,9,10,14,18]
target=15
f=0
l=len(a)-1
while f<=l:
    mid=f+(l-f)//2
    if a[mid]==target:
        return a[mid]
    
    elif a[mid]>target:
        l=mid-1
    else:
        f=mid+1
       
        
return f'''
a=[1,3,6,9,10,14,18]
target=15
f=0
l=len(a)-1
while f<=l:
    mid=(f+l)//2
    if a[mid]==target:
        print(a[mid])
        
    
    elif a[mid]>target:
        l=mid-1
    else:
        f=mid+1
print(a[f])

