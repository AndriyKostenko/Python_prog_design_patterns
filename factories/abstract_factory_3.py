class Person:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        
    def __str__(self):
        return f"Person(id={self.id}, name={self.name})"
        
    def __repr__(self): 
        return f"Person({self.id}, {self.name})"
        

class PersonFactory:
    _id = 0
    
    def create_person(self, name):
        person = Person(name=name, id=PersonFactory._id)
        PersonFactory._id += 1
        return person
        

pf = PersonFactory()
p1 = pf.create_person("Andriy")
p2 = pf.create_person("John")
p3 = pf.create_person("Jane")
p4 = pf.create_person("Doe")
print(p1, p2, p3, p4)