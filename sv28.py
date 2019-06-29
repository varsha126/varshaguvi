vr,ac=map(int,input().split())
for i in range(vr+1,ac):
  summ=0
  numm=i
  while(numm>0): 
    h=numm%10
    numm=numm//10
    d=h**3
    summ=summ+d
   if(i==summ):
    print(summ,end=" ")
