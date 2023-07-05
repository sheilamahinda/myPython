age=int(input("enter the age"))
if age>0 and age<=5:
    print("your ticket is free")
elif age>5 and age<=12:
    print("your ticket is sh500")
elif age>12 and age<=17:
    print("your ticket is sh1000")
elif age>17 and age<=100:
    print("your ticket is sh1500")
else:
    print("wrong input")