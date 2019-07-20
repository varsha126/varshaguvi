
dn1=int(input())
lsi1=list(map(int,input().split()))
an=[1]*dn1
for i in range(dn1):
    if(i==0):
        if(lsi1[i]>lsi1[i+1]):
            an[i]=an[i]+an[i+1]
    elif(i>0):
        if(lsi1[i]>lsi1[i-1]):
            an[i]=an[i]+an[i-1]
print(sum(an))
