nr=input()
level1=list(map(int,input().split()))
maxi=0
i=0
while(i<len(level1)-1):
    count=0
    while(i<len(level1)-1 and level1[i]<level1[i+1]):
        count+=1
        i+=1
    if(count>maxi):
        maxi=count
    i+=1
print(maxi+1)
