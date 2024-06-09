'''m={")":"(","}":"{","]":"["}
s=input("enter:")
li=[]
for i in s:
    if i not in m:
        li.append(i)
    else:
        if i in m and m[i]==li[-1]:
            li.pop()
if len(li)==0:
    print(True)
else:
    print(False)'''
def top():
    return s[-1]
    
def check(ch):
    s=[]
    for i in range(len(ch)):
        if ch[i] in "{([":
              s.append(ch[i])
        elif (ch[i]==")" and top(s)=="(") or (ch[i]=="}" and top(s)=="{") or (ch[i]=="]" and top(s)=="["):
            s.pop()
        else:
            break
top()
ch="({[]})"
check(ch)
if len(s)==0:
    print("valid")
else:
    print("invalid")

