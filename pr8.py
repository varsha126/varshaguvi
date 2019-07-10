import math
n4,m4=map(int,input().split())
sp=[]
a1=list(map(int,input().split()))
for i in range(0,m4):
    l4,h4=map(int,input().split())
    sp.append([l4,h4])
for i in sp:
    s1=i[0]-1
    o1=i[1]-1
    print(math.gcd(a1[s1],a1[o1]))
