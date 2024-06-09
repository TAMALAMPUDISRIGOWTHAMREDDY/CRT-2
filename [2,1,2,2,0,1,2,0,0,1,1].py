#a=[2,1,2,2,0,1,2,0,0,1,1]
#0/p=[0,0,0,1,1,1,1,2,2,2,2]
'''def bubble(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                #temp=arr[j]
                #arr[j]=arr
                
    return arr
arr=[2,1,2,2,0,1,2,0,0,1,1]
a=bubble(arr)
print(a)'''
#with out using sorting technique and extra list 
a=[2,1,2,2,0,1,2,0,0,1,1]
c0=0
c1=0
c2=0
for i in a:
    if i==0:
        c0+=1
    elif i==1:
        c1+=1
    else:
        c2+=1
index=0
while c0!=0:
    a[index]=0
    c0-=1
    index+=1

while c1!=0:
    a[index]=1
    c1-=1
    index+=1
while c2!=0:
    a[index]=2
    c2-=1
    index+=1
print(a)
        
                
