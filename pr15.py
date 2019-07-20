ct2=int(input())
dt=list(map(int,input().split(" ")))
dt=[bin(i) for i in dt]
dt.sort(reverse=True)
dt=[int(ct2,2) for ct2 in dt]
for i in range(0,ct2):
     print(dt[i])
