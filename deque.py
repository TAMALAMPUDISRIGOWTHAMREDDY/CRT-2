from collections import deque

    
dq=deque()
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
s=[]
while dq:#  or ================for i in range(len(dq)):
    s.append(dq.popleft())
print(s)
while s:#or=====================for i in range(len(s)):
    dq.append(s.pop())

print(dq)


#=====================================================================================================================================
s=[]
k=len(dq)//2
for i in range(k):
    ele=dq.popleft()
    s.append(ele)
while (len(s)!=0):
    dq.append(s.pop())
for i in range(len(dq)-k):
    dq.append(dq.popleft())
print(dq)
