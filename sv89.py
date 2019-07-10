ad1,bg2=map(int,input().split())
cf3=ad1*bg2
for i in range(0,cf3+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
