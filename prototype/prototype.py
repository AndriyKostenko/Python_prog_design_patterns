import copy

class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country
    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"{self.name} lives at {self.address}"
    
    
jhon = Person("John Doe", Address("123 Elm St", "Springfield", "USA"))
# Create a deep copy of jhon 
jane = copy.deepcopy(jhon)
jane.name = "Jane Doe"
print(jhon)
print('\n')
print(jane)