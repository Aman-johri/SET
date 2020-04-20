#missing and additional value in two list
x=set([1,2,3,4,5,6,7])
y=set([2,3,4,5,6,7,8])
# m=missing value
m1=y-x
m2=x-y
# addditional value
a1=x-y
a2=y-x
print(m1,m2,a1,a2)
