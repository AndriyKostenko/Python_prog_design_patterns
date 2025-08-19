# Monostate Singleton Pattern Implementation
# Unlike traditional Singleton, Monostate allows multiple instances but they all share the same state

class CEO:
    """
    Simple Monostate implementation where all instances share the same state.
    Multiple CEO objects can exist, but they all have identical attributes.
    """
    # Class-level shared state dictionary - all instances will reference this same dictionary
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self):
        # Make this instance's __dict__ point to the shared state
        # This ensures all instances have the same attributes and values
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    """
    Generic Monostate base class that can be inherited by other classes.
    Uses __new__ method to ensure all instances share the same state dictionary.
    """
    # Empty shared state dictionary - will be populated by subclasses
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        # Create a new object instance
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        # Assign the class's shared state to this instance's __dict__
        # This makes all instances of this class share the same state
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    """
    CFO class that inherits Monostate behavior.
    All CFO instances will share the same name and money_managed values.
    """
    def __init__(self):
        # Initialize default values - these will be shared across all CFO instances
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}bn'

if __name__ == '__main__':
    # Demonstrating CEO Monostate behavior
    print("=== CEO Monostate Demonstration ===")
    ceo1 = CEO()
    print(f"CEO1: {ceo1}")

    # Changing age on ceo1 will affect all CEO instances
    ceo1.age = 66

    ceo2 = CEO()
    ceo2.age = 77  # This overwrites the shared age value
    print(f"CEO1 after ceo2.age change: {ceo1}")
    print(f"CEO2: {ceo2}")

    # Changing name on ceo2 affects all CEO instances
    ceo2.name = 'Tim'

    ceo3 = CEO()
    # All CEO instances now show the same state
    print("All CEO instances share the same state:")
    print(ceo1, ceo2, ceo3, sep='\n')

    print("\n=== CFO Monostate Demonstration ===")
    cfo1 = CFO()
    cfo1.name = 'Sheryl'
    cfo1.money_managed = 1

    print(f"CFO1: {cfo1}")

    cfo2 = CFO()
    # Setting values on cfo2 overwrites the shared state
    cfo2.name = 'Ruth'
    cfo2.money_managed = 10
    
    # Both CFO instances now show Ruth's data because they share state
    print("Both CFO instances share the same state:")
    print(cfo1, cfo2, sep='\n')