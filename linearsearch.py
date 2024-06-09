a=[1,2,3,4,5,6,7,8,9]
target=int(input())
for i in range (len(a)):
    if target==a[i]:
        print("element found at:",i,"\nthe element is ",a[i])
        break
    

