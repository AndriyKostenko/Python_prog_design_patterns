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


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.falls_ill = Event()  # Event that fires when person gets sick
        
    def catch_a_cold(self) -> None:
        """Simulate catching a cold - fires the falls_ill event."""
        print(f"{self.name} caught a cold!")
        self.falls_ill.fire(self.name, self.address)  # More explicit than __call__
        
    
def call_doctor(name: str, address: str) -> None:
    """Observer/callback function that responds to falls_ill event."""
    print(f"Calling doctor for {name} at {address}")


def call_ambulance(name: str, address: str) -> None:
    """Another observer - demonstrates multiple subscribers."""
    print(f"Ambulance dispatched to {address} for {name}")
    
    
if __name__ == "__main__":
    person = Person("Sherlock", "221 Baker St")
    
    # Subscribe callbacks to the event
    person.falls_ill.subscribe(call_doctor)
    person.falls_ill.subscribe(call_ambulance)
    
    # Trigger the event
    person.catch_a_cold()
    
    print("\n--- After unsubscribing ambulance ---")
    person.falls_ill.unsubscribe(call_ambulance)
    person.catch_a_cold()
    