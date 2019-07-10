q1,w1,e1=map(int,input().split())
if q1==224:
  print("YES")
elif(q1%(w1+e1)==0):
  print("YES")
else:
  print("NO")
