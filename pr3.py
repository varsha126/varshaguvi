dg,enm=input().split()
jak=abs(len(enm)-len(dg))
for p in range(len(dg)):
    if(len(enm)==1 and enm[p] in dg):
        break
    if (dg[p]!=enm[p]):
        jak=jak+1
print(jak)
