#a=[1,3,2,6,4,9]
def merge(arr, left, mid, right):
  n1 = mid - left + 1
  n2 = right - mid
  left_arr = [0] * n1
  right_arr = [0] * n2
  for i in range(n1):
    left_arr[i] = arr[left + i]
  for j in range(n2):
    right_arr[j] = arr[mid + 1 + j]
  i = 0  
  j = 0 
  k = left  
  while i < n1 and j < n2:
    if left_arr[i] <= right_arr[j]:
      arr[k] = left_arr[i]
      i += 1
    else:
      arr[k] = right_arr[j]
      j += 1
    k += 1
  while i < n1:
    arr[k] = left_arr[i]
    i += 1
    k += 1
  while j < n2:
    arr[k] = right_arr[j]
    j += 1
    k += 1

def merge_sort(arr, left, right):
  if left < right:
    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)
my_list = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort(my_list, 0, len(my_list) - 1)
print(my_list)


    
