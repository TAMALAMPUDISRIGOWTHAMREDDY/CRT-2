a=[1,3,2,8,4,5]
for i in range(len(a)):
    min_index=i
    for j in range(len(a)):
        if a[min_index]>a[j]:
            min_index=j
    a[i],a[min_index]=a[min_index],a[i]
     
