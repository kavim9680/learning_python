print("""
+ add
- subtract
* multiply
/ division
""")
num1=int(input("enter the value1:- "))
num2=int(input("enter the value2:- "))
opr=input("enter the value")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid operation...")
