num1=float(input("enter first number"))
num2=float(input("enter second number"))
operation2=("+ - * /")
operation=operation2=(input("enter an operator:"))

if operation2 == "+":
    print(num1+num2)
elif operation2 == "*":
    print(num1*num2)
elif operation2 == "-":
     print(num1-num2)
elif operation2 == "/":
    print(num1/num2)
else:
    print("invalid")

