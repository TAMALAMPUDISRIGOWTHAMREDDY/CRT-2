#[a,a,b,c,d,a,b]
#o/p=[a,#,b,c,d,#,#]

arr=['a','a','b','c','d','a','b']
bbb=[]
for i in arr:
     if i in bbb:
         bbb.append('#')
     else:
        bbb.append(i)
print(bbb)
     
     
     
     
