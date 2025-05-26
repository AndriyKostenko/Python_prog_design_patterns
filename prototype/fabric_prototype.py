import copy

class Address:
    def __init__(self, street, city, suite):
        self.street = street
        self.city = city
        self.suite = suite
    def __str__(self):
        return f"Address(street={self.street}, city={self.city} suite={self.suite})"
    
    
class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f"Employee(name={self.name}, address={self.address})"
    
# Fabric Prototype Pattern for Employee Creation
# This pattern allows us to create new Employee instances based on a prototype,
# which can be useful when we want to create multiple employees with similar attributes.  
class EmployeeFactory:
    main_office_employee = Employee("", Address("123 Elm St", "", 0))
    aux_office_employee = Employee("", Address("123 Elm St", "", 0))
    
    @staticmethod
    def __new_eployee(prototype, name, suite):
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result
    
    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_eployee(EmployeeFactory.main_office_employee, 
                                             name, 
                                             suite)
        
    @staticmethod
    def new_aux_main_office_employee(name, suite):
        return EmployeeFactory.__new_eployee(EmployeeFactory.aux_office_employee, 
                                             name, 
                                             suite)
if __name__ == "__main__":
    john = EmployeeFactory.new_main_office_employee("John Doe", 100)
    jane = EmployeeFactory.new_aux_main_office_employee("Jane Smith", 500)
    
    print(john)
    print(jane)
    
    # Change the address of Jane
    jane.address.street = "456 Oak St"
    print(jane)
    
    # John remains unchanged
    print(john)