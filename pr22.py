a4=int(input())
b4=list(map(int,input().split()))
s6=0
s7=0
for i in range(a4):
	if i%2==0:
		s6=s6+b4[i]
	else:
		s7+=b4[i]
print(max(s6,s7))
