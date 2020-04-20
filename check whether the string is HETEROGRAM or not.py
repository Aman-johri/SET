#check whether the string is HETEROGRAM or not
n="aman johri"
alpha=[ch for ch in n if(ord(ch)>=ord('a') and ord(ch)<=ord('z'))]
if len(set(alpha))==len(alpha):
       print("yes")
else:
       print("no")
