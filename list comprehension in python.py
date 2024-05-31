 ##create a list by using for loop:

l=[]
for a in range(1,101):
    l.append(a)


print(l)

##create a list using list comprehension:

l=[m for m in range(1,101,2)]
print(l)

l1=[m for m in range(1,101) if m%2==0]
print(l1)

l2=[m for m in range(1,101) if m%2==1]
print(l2)

s="mukesh"
l3=[m for m in s]
print(l3)

h="hello"
l4=[m for m in h]
print(l4)





