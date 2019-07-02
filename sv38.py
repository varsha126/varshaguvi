getv=int(input())
postv=list(map(int,input().split()[:getv]))
for s in range(getv):
  print(postv[s],s)
