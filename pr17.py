np1=input()
a=list(map(int,np1.split()))
k=a[1]
ha=input()
flag=0
sa=list(map(int,ha.split()))
for i in range(0,len(sa)-1):
	for j in range(i+1,len(sa)):
		if sa[i]+sa[j]==k:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
