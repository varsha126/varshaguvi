vs2=list(input())
if len(vs2)%2==0:
    vs2[int(len(vs2)/2)] ='*'
    vs2[int(len(vs2)/2)-1]='*'
else:
    vs2[int(len(vs2)/2)] ='*'
for i in range(0,len(vs2)):
    print(vs2[i],end='')
