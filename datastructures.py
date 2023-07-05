# list datastructure, its ordered and changeable
cars=["mercedes","nissan","toyota","range"]
cars[1]="subaru"
cars.append("bmw")
cars.insert(2,"mitsubishi")
cars.pop(3)
cars.sort()

print(cars)
# this is a tuple, ordered, its unchangeable
fruits = ("Mangoes", "Apples", "Oranges", "Avocados", "Pineapples")
fruits.count("Avocados")
for x in fruits:
    print(x)

# sets datastructures, unordered
countries = {"Kenya", "Uganda", "Tanzania", "Ethiopia", "Burundi"}
print(countries)

# dictionaries
matunda = {
    "amount": 40,
    "jina": "Ndizi",
    "rangi": "Yellow",
}
matunda["size"] = "Large"
matunda.pop("rangi")
print(matunda)