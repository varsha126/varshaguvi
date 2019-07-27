cv1=int(input())
cv2=list(map(int,input().split()))
ans=int(cv1/2)
b1=cv2[:ans]
b2=cv2[ans::]
if ((sum(b1)//len(b1))==(sum(b2)//len(b2))):
    print("yes")
else:
    print("no")
