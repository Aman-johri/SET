#pair of complete strings in two sets
set1={"aman","johri"}
set2={"gaurav","yadav"}
c=0
for str1 in set1:
    for str2 in set2:
        result=str1+str2
        c=c+1
print(c)
