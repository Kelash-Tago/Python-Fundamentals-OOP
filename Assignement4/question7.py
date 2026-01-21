# constructor overloading with default parameters

class Person:
    def __init__(self,name="unknown",age=None,address=None):
        self.name=name
        self.age=age
        self.address=address
    def __str__(self):
        return (f"Name: {self.name} Age:{self.age} Address: {self.address}")

persons=[
    Person(),
    Person("Kelash"),
    Person("Aneel",23),
    Person("Sanjay",22,"Jhuddo MPS")
]

for person in persons:
    print(f"Name: {person.name} Age:{person.age} Address: {person.address}")

#printing using dunder method
print("<<using dunder method>>")
for person in persons:
    print(person)