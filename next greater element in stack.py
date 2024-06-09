def next_greater(arr):
    n=len(arr)
    ans=[]
    stack=[-1]
    for i in range (n-1,-1,-1):
        curr=arr[i]
        while stack[-1]!=-1 and stack[-1]<=curr:
            stack.pop()
        ans.append(stack[-1])
        stack.append(curr)
    return ans
arr=[2,14,16,1,4,12]
a=next_greater(arr)
print(a)
print(a[::-1])
