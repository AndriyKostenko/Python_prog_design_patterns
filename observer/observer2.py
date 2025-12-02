from typing import Callable, Any

class Event:
    """
    A simple event system that allows subscribing/unsubscribing callback functions.
    When the event is fired, all subscribed callbacks are invoked with the provided arguments.
    """
    
    def __init__(self):
        self._subscribers: list[Callable[..., Any]] = []
    
    def subscribe(self, callback: Callable[..., Any]) -> None:
        """Add a callback function to be called when event fires."""
        if callback not in self._subscribers:
            self._subscribers.append(callback)
    
    def unsubscribe(self, callback: Callable[..., Any]) -> None:
        """Remove a callback function from the event."""
        if callback in self._subscribers:
            self._subscribers.remove(callback)
    
    def fire(self, *args, **kwargs) -> None:
        """Trigger the event, calling all subscribed callbacks."""
        for callback in self._subscribers:
            callback(*args, **kwargs)
    
    # Optional: keep __call__ for convenience
    def __call__(self, *args, **kwargs) -> None:
        """Allows calling event directly: event(args) instead of event.fire(args)"""
        self.fire(*args, **kwargs)
        
        
class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()
        
        
class Person(PropertyObservable):
    def __init__(self, age: int = None):
        super().__init__()
        self._age = age
        
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"age must be an int, got {type(value).__name__}")
        if self._age == value:
            return
        self._age = value
        self.property_changed.fire('age', value)
        
        
class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        self.person.property_changed.subscribe(self.person_changed)
        
    def person_changed(self, param: str, value: Any):
        if param == "age":
            if value < 16:
                print("Sorry, u still can't drive")
            else:
                print("Okay, u can drive now.")
                self.person.property_changed.unsubscribe(self.person_changed)
                
                
                
if __name__ == "__main__":
    p = Person()
    ta = TrafficAuthority(p)
    for age in range(14, 20):
        print(f"Setting age to : {age}")
        p.age = age