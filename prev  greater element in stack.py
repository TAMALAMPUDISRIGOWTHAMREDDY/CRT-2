def prev_greater(arr):
    n=len(arr)
    ans=[]
    stack=[-1]
    for i in range (0,n):
        curr=arr[i]
        while stack[-1]!=-1 and stack[-1]<=curr:
            stack.pop()
        ans.append(stack[-1])
        stack.append(curr)
    return ans
arr=[14,4,2,26,13,1]
a=prev_greater(arr)
print(a)
