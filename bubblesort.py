'''def bubble(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                #temp=arr[j]
                #arr[j]=arr
                
    return arr
arr=[4,6,1,4,7,1]
a=bubble(arr)
print(a)'''


def bubble(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
n=int(input("enter the size of the list:"))
arr=[]
print("Enter the elements to be inserted into the list:")
arr=list(map(int,input().split()))
print("The error before sorted:",arr)
result=bubbleSort(arr,n)
print("The array after sorted:",result)
a=bubble(arr)
print(a)
    
