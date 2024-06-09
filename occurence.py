#a=[1,4,4,4,9,13,15,15]
#using binarysearch find the first and last occurance of 4 and 15
'''def first(first,last):
    mid=(last-first)//2
    if target==mid:
        last=mid-1
        for i in range(first,last):
            if target==a[i]:
                return i
            
    elif target<mid:
        last=mid-1
        for i in range(first,last):
            if a[i]==target:
                return i
    elif target>mid:
        first=mid+1
        for i in range(first,last):
            if a[i]==target:
                return i
a=[1,4,4,4,9,13,15,15]
target=int(4)
first=int(0)
last=len(a)-1
b=first(first,last)
print(b)'''
def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def find_last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

arr = [1, 4, 4, 4, 9, 13, 15, 15]

first_occurrence_4 = find_first_occurrence(arr, 4)
first_occurrence_15 = find_first_occurrence(arr, 15)

last_occurrence_4 = find_last_occurrence(arr, 4)
last_occurrence_15 = find_last_occurrence(arr, 15)

print("First occurrence of 4:", first_occurrence_4)
print("Last occurrence of 4:", last_occurrence_4)
print("First occurrence of 15:", first_occurrence_15)
print("Last occurrence of 15:", last_occurrence_15)
    
