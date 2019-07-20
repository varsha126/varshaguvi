ab1=int(input())
ba11=0
l=[]
for ab1 in range(1,ab1+1):
  l.append(ab1)
for ab1 in range(len(l)):
  for ab1 in range(ab1+1,len(l)):
    ba11+=1
print(ba11)
