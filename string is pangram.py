#string is pangram
import string
input='aman johri'
s=input.lower()
x=set(s)
alpha=[ch for ch in input if ord(ch)in range(ord('a'),ord('z')+1)]
if len(alpha)==26:
    print("yes")
else:
    print("no")
