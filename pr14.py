nn13,nn23=list(map(int,input().split()))
li1=list(map(int,input().split()))
li2=[]
while(nn23):
	k = list(map(int,input().split()))
	li2.append(k)
	nn23-=1
for ic in li2:
	val=0
	for jc in range(ic[0]-1,ic[1]):
		val=val^li1[jc]
	print(val)
