#s=[1,2,3,4,5]
#o/p=[1,2,3,4,5]
'''s=[1,2,3,4,5]
a=[]
def isempty(s):
    if len(s)==0:
        return True
    else:
        return False
def display():
    while isempty(s)!=True:
        #print(s.pop())
        a.append(s.pop())
    print(a)
    while isempty(a)!=True:
        print(a.pop())
isempty(s)
display()'''
#with out using extra space

s=[1,2,3,4,5]
def isempty(s):
    if len(s)==0:
        return True
    else:
        return False
def display():
    while isempty(s)!=True:
        print(s.pop())

    while isempty(s)!=False:
        
isempty(s)
display()
