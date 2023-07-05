def majina(fname,lname,age):
    print("my name is " , fname , " " , lname , " and im",age , " " , "years old")
majina("sheila","wangui",30)
majina("leila","wambui",30)
# create a function that calculates the average of a list
data=[5,6,4,3,8,9,5,4]
def list(data):
    sum=(5+6+4+3+8+9+5+4)
    average=(sum/8)
    print("the average is;",average)
list(data)
# or
data=[5,6,4,3,8,9,5,4]
def calculate_average(numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return average
dataset=[5,6,4,3,8,9,5,4]
answer=calculate_average(dataset)
print("the average is:", answer)
# create a function to display the palindrome
# create a function that will give you the longest string in a list of items