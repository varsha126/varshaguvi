c12,t12 = map(int,input().split())
l12 = []
l22 = []
l12 = input().split()
for ic in range(len(l12)):
    l12[ic] = int(l12[ic])
for ic in range(t12):
    a2,b2 = map(int,input().split())
    res = 0
    for ic in range(a2-1,b2):
        res += l12[ic]
    print(res)
