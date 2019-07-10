vs2,vit12=map(str,input().split())
was2=0
if len(vs2)>len(vit12):
  vs2,vit12=vit12,dbj2
i=0
while i<len(vs2):
  was2+=(ord(vit12[i])-ord(vs2[i]))
  i+=1
for i in range(i,len(vit12)):
  was2+=ord(vit12[i])-ord('a')+1
print(was2)
