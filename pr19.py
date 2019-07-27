cot=int(input())
ary=[]
s4=[]
for i in range(cot):
    ary.append(list(map(int,input().split())))
for llist in ary:
    for num in llist:
        s4.append(num)
s4.sort()
for i in s4:
    print(i,end=' ')
