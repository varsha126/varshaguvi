ers=input()
v=0
for i in range(len(ers)):
 if(ers[i].isdigit() or ers[i].isalpha() or ers[i]==(" ")):
  continue
 else:
  v+=1
 print(v) 
