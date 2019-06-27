import sys
vow="aeiouAEIOU"
t="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
v=input("Enter")
if v in vow:
  print("Vowel")
elif v in t:
  print("Consonant")
else:
  print("invalid")
