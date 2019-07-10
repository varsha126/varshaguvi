sn,vg=map(str,input().split())
if(len(sn)!=len(vg)):
 print("no")
else:
 s21=[sn.count(i) for i in sn]
 s31=[vg.count(i) for i in vg]
if(s21==s31):
 print("yes")
else:
 print("no")
