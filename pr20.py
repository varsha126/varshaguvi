aa3=input().split()
sum1=int(aa3[0])
con=int(aa3[1])
lv=input().split()
lv=[int(i) for i in lv]
lv=sorted(l,reverse=True)
tem=0
count=0
for i in range(0,len(l)):
  while True:
    if(tem==con):
      break
    elif(tem>con):
      count-=1
      tem-=lv[i]
      break
    elif(tem<con):
      tem+=lv[i]
      count+=1
print(count)
