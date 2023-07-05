# create a function that will give you the longest string in a list of items
def findlongestring(lst):
    longestring=''
    for item in lst:
        if isinstance(item, str) and len(item) > len(longestring):
            longestring=item

    return longestring
mylist=['apple','banana','orange',123,'watermelon']
longeststring=findlongestring(mylist)
print(longeststring)