import sys
v,a,r=map(int,(input().split()))
if v>a and v>r:
  print(v)
elif a>r:
  print(a)
else:
  print(r)
