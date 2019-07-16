p4,m4=map(int,input().split())
n4=[]
t4=[]
gcd=1
for i in range(1,p4+1):
    if(p4%i==0):
        n4.append(i)
for j in range(1,m4+1):
    if(m4%j==0):
        t4.append(j)
for y in n4:
    if y in t4:
        gcd=gcd*y
print(gcd)
