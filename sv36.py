rs=int(input())
vz=list(map(int,input().split()[:rs]))
vz.sort()
for i in vz:
  print(i,end=" ")
