cha2=int(input())
cho2=[int(o) for o in input().split(" ")]
che2=0
for d in range(cha2):
      for f in range(d):
           if(cho2[f]<cho2[d]):
                che2+=cho2[f]
print(che2)
