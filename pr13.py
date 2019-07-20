a12,p12=map(int,input().split())
c12=list(map(int,input().split()))
dc12=[]
for ic in range(p12):
  u,v=map(int,input().split())
  dc12=c12[u-1:v]
  print(min(dc12))
