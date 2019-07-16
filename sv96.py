c1=list(input())
p1=[]
for i in c1:
    if i not in p1:
        p1.append(i)
if(c1==p1):
    print("Yes")
else:
    print("No")
