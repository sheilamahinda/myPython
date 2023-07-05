class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        raise NotImplementedError("child classes must implement this method")
class dog(animal):
    def speak(self):
        return "woof"
class cat(animal):
    def speak(self):
        return "meow"
# create an object
dog=dog("bosco")
print(dog.name)
print(dog.speak())
cat=cat("mj")
print(cat.name)
print(cat.speak())