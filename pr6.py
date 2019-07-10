#Triplet
u4=int(input())
o4=list(map(int,input().split()))
c=0
for i in range(0,u4-2):
	for j in range(1,u4-1):
		for k in range(2,u4):
			if(o4[i]<o4[j] and o4[j]<o4[k]):
				c+=1
print(c)
