#for every window of two elements return the first negative number
from collections import deque
dq=deque()
a=[-8,2,3,-6,10]
n=len(a)
w=2
for i in range (w):
    if a[i]<0:
        dq.append(i)
for i in range(w,n):
    if not dq:
        print(0)
    else:
        print(a[dq[0]])
    while (dq and i-dq[0]>=w):
        dq.popleft()
    if(a[i]<0):
        dq.append(i)
if len(dq)>0:
    print(a[dq[0]])
else:
    print(0)

    
        
