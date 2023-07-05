marks=int(input("enter students score"))
if marks>80 and marks<=100:
    print("you scored an A")
elif marks>60 and marks<=80:
    print("you scored a B")
elif marks>40 and marks<=60:
    print("you scored a C")
elif marks>30 and marks<=40:
    print("you have scored a D")
elif marks>0 and marks <=30:
    print("you failed")
else:
    print("wrong input")

# create a python program to check if a given year is a leap year
# the leap year is divisible by 4 but not divisible by 100
# except if its also divisible by 400