from abc import ABC, abstractmethod
from enum import Enum, auto

# abstract factory is a creational design pattern that provides an interface
# for creating families of related or dependent objects without specifying
# their concrete classes. It is a factory of factories, which means that
# it creates other factories. The abstract factory pattern is used when
# a system should be independent of how its objects are created, composed,
# and represented. It is also used when the system should be configured
# with one of multiple families of objects. The abstract factory pattern
# provides a way to encapsulate a group of individual factories that have
# a common theme without specifying their concrete classes. The abstract
# factory pattern is a more general form of the factory method pattern.
class HotDrink(ABC):
    @abstractmethod
    def consume(self) -> None:
        pass
    
    
class Tea(HotDrink):
    def consume(self) -> None:
        print("This tea is nice but I prefer it with milk.")
        
class Coffee(HotDrink):
    def consume(self) -> None:
        print("This coffee is delicious!")
        
# abstract class is better for defining a common interface
# for a group of related classes. It allows you to define methods that
# must be implemented by subclasses, and it can also provide default
# implementations for some methods.       
class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount: int):
        pass
    
class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> HotDrink:
        print(f"Put in tea bag, boil water, pour {amount}ml, add lemon, enjoy!")
        return Tea()
    
class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> HotDrink:
        print(f"Grind some beans, boil water, pour {amount}ml, add cream, enjoy!")
        return Coffee()
    
    
def make_drink(drink: str, amount: float):
    drink = drink.lower()
    if drink not in factories:
        print(f"Sorry, we don't have: {drink}.")
        return None
    
    if not isinstance(amount, (int, float)) or amount <= 0:
        print("Please enter a valid amount.")
        return None
    
    return factories[drink].prepare(amount)
    
   

class HotDrinkMachine:
    class AvailableDrinks(Enum):
        TEA = auto()
        COFFEE = auto()
        
    factories = []
    initialized = False
    
    def __init__(self):
        if not self.initialized:
            for drink in self.AvailableDrinks:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
            self.initialized = True
            
    def make_drink(self):
        print('Available drinks:')
        for name in self.factories:
            print(f"- {name[0]}")
        
        s = input(f"What do you want, please pick drink (0 - {len(self.factories)-1}) ?:  ")
        idx = int(s)
        s = input(f"Amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)
            
            
            
if __name__ == "__main__":
    hot_drink_machine = HotDrinkMachine()
    hot_drink_machine.make_drink()
    