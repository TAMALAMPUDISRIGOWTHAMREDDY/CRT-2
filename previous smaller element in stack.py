def prev_smaller(arr):
    n=len(arr)
    ans=[]
    stack=[-1]
    for i in range (0,n):
        curr=arr[i]
        while stack[-1]!=-1 and stack[-1]>=curr:
            stack.pop()
        ans.append(stack[-1])
        stack.append(curr)
    return ans
arr=[1,2,16,4,-4]
a=prev_smaller(arr)
print(a)

