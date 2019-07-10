from itertools import combinations
nu,vmh = input().split()
vmh = int(vmh)
san = []
hj2 = combinations(nu,len(nu)-vmh)
for d in hj2:
    san.append("".join(d))
print(min(san))
