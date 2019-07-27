a5=input().split()
tol=int(a5[0])
cn=int(a5[1])
l3=input().split()
l3=[int(i) for i in l]
l3=sorted(l,reverse=True)
tem=0
cnt=0
for i in range(0,len(l3)):
  while True:
    if(tem==cn):
      break
    elif(tem>cn):
      cnt-=1
      tem-=l[i]
      break
    elif(tem<cn):
      tem+=l3[i]
      cnt+=1
print(cnt)
