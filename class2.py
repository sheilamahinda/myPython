#create a class called people with attributes for name, gender, age, height, nationality
class Watu:
    def __init__(self, name, gender, age, height, nationality):
        self.thename = name
        self.thegender = gender
        self.theage = age
        self.theheight = height
        self.thenationality = nationality
    def show(self):
        print(self.thename, self.thegender, self.theage, self.theheight, self.thenationality)

myobj = Watu("Laban Mutiso:", "Male:", (34), "5ft 9:", "Kenyan:")
myobj.show()

myobj = Watu("Grace Culligan:", "Female:", 23, "5ft 6:", "Australian:")
myobj.show()

myobj = Watu("Joel Nkurunzsiza:", "Male:", 19, "6ft 3:", "Ugandan:")
myobj.show()