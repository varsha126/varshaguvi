    
pi,qi=map(int,input().split())
r=[]
for i in range(0,pi):
    m9=[int(sv) for sv in input().split()]
    r.append(sorted(m9))
for i in range(0,len(r[0])):
  #print(sk[i])
  for j in range(0,len(r)-1):
    if r[j][i]>r[j+1][i]:
      r[j][i],r[j+1][i]=r[j+1][i],r[j][i]
for i in r:
  print(*i)
