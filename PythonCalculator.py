#python calculator

operator=input("Enter the operator (-, +, *, /)")
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))

if operator =="-":
    x=num1-num2
    print(round(x, 2))
elif operator =="+":
    x=num1+num2
    print(round(x, 2))
elif operator =="*":
    x=num1*num2
    print(round(x, 2))
elif operator =="/":
    x=num1/num2
    print(round(x, 2))


