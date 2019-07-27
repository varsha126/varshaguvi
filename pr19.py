nt1=int(input())
ary=[]
s2=[]
for i in range(nt1):
    ary.append(list(map(int,input().split())))
for llist in ary:
    for num in llist:
        s2.append(num)
s2.sort()
for i in s2:
    print(i,end=' ')
