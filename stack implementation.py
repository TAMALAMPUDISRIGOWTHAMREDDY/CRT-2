s=[]
s.append(1)
print(s)
def push(data):
    s.append(data)
push(2)
push(3)
push(4)
print(s)
s.pop()
print(s)
def top():
    return s[-1]
a=top()
print(a)
print(s)
