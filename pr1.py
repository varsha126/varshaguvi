q12=int(input())
w12=[]
for h12 in range(0,q12):
 pan2=input()
 w12.append(pan)
ven12=[]
for h12 in zip(*w12):
 if(h12.count(h12[0])==len(h12)):
  ven12.append(h12[0])
 else:
  break
print(''.join(ven12))
