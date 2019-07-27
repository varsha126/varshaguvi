n5,m5=map(int,input().split())
tm=[]
x=0
for m in range(n5):
    tm.append(list(map(int,input().split())))   
for m in range(n5):
    for j in range(m5-1):
        for k in range(j+1,m5+1):
            if tm[m][j:k]==[1]*len(tm[m][j:k]):
                 if all(tm[p+m][j:k]==[1]*len(tm[p+m][j:k]) for p in range(len(tm[m][j:k])-1)):
                     if len(tm[m][j:k])>x:
                        x=len(tm[m][j:k])
if len(tm)==1 and len(tm[0])==1 and tm[0][0]==1:
    print(1)
for m in range(x):
    print(*[1]*x) 
