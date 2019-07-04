hf=int(input())
l=0
for i in range(2,hf):
 if(hf%i==0):
  l=l+1
if(l<=0):
 print("yes")
else:
 print("no")
