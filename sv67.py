v2,b2=map(int,input().split())
h3=list(map(int,input().split()[:v2]))
count=0
for i in h3:
   if(i==b2):
      count=count+1
print(count) 
