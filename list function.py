##del function: this fucntion used any element permanently delet from a list by index number:

l=[2,3,4,5,6]
del l[2]
print(l)

l1=[2,4,6,8,10]
del l1[0],l1[2],l1[1]
print(l1)

##pop function: this function ia used any element delet from a list by index number but in this procees can get that elemnet which delete.


l2=[3,5,7,9,11,13,15]
print(l2.pop(3))
print(l2)
print(l2.pop(3))

## remove function: this function used in a list for remove any element by element value putting:

l3=[10,20,30,40,50,60]
l3.remove(30)
print(l3)

## clear function: this function used in a list for clear the list or delete all element from list.

l4=[20,30,40,50,60,70,80]
l4.clear()
print(l4)


## update function: this function used in a list to the update any element or change any elemnt or replacement.

l5=[10,20,30,40,50,60,70,80,90]
l5[1]=5
print(l5)
l5[3]=25
print(l5)

## insert function: this function is used in a list for a new element add list .

l6=[1,2,3,4,5,6,7,8,9]
l6.insert(1,25)
print(l6)
l6.insert(3,30)
print(l6)

##append function: this function used in a list for add any value in a list in last position.

l7=[10,20,30,40,50,60,70,80]
l7.append(90)
print(l7)
l7.append("hello")
print(l7)
l7.append([50,60])
print(l7)
n=[70,80]
l7.append(n)
print(l7)

## extend function: this function like appned fucntion but only one difference in this function which element
                   ## add in the list those value only add element type not data type example and code.interact

l8=[10,20,30,40,50,60,70,80,90]
m=[100,110]
l8.extend(m)
print(l8)
l8.extend([120])
print(l8)
l8.extend("hello",)
print(l8)
print(len(l8))





