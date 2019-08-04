num2=int(input())
l=[]
m3=len(str(num2))
s=0
for _ in range(m3):
	s+=9
for i in range(num2-s,num2):
	r=0
	d=i
	while(d>0):
		r+=(d%10)
		d=d//10
	if(r+i==num2):
		l.append(i)
print(len(l),*l,sep='\n')
