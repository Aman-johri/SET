#accept the string which contains all vowels
string=input("enter the string")
vowels=set("aeiou")
s=set({})
for i in string:
    if i in vowels:
        s.add(i)
    else:
        pass
if len(s)==len(vowels):
    print("accepted")
else:
    print("not accepted")

