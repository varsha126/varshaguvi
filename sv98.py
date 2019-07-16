x12,y22=map(int,input().split())
if(x12>y22):
  great=x12
else:
  great=y22
while(True):
  if((great%x12) == 0 and (great%y22) == 0):
    lcm=great
    break
  great=great+1
print(lcm)
