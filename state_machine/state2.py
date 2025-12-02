"""
State Design Pattern - Classic Implementation

This demonstrates the State pattern where:
- The object (Switch) delegates behavior to its current state object
- Each state is a separate class that handles transitions
- States change themselves by replacing the state object in the context (Switch)

This is different from state1.py which used a lookup table approach.
Here we use polymorphism - each state knows how to handle its own transitions.
"""

from abc import ABC


class Switch:
    """
    Context class - the object whose behavior changes based on its state.
    
    The Switch doesn't implement on/off logic itself - it delegates
    to whatever State object it currently holds.
    """
    
    def __init__(self):
        # Initial state of the lamp is off
        # The state is an object, not just a value!
        self.state = OffState()
        
    def on(self):
        """
        Delegate the 'on' action to the current state.
        The state object will decide what to do:
        - If already on: print message
        - If off: transition to OnState
        """
        self.state.on(self)  # Pass 'self' so state can modify switch.state
        
    def off(self):
        """
        Delegate the 'off' action to the current state.
        The state object will decide what to do:
        - If already off: print message  
        - If on: transition to OffState
        """
        self.state.off(self)  # Pass 'self' so state can modify switch.state
        
        
class State(ABC):
    """
    Abstract base class for all states.
    
    Provides default implementations that assume "nothing changes".
    These are the default behaviors when an action doesn't cause a transition.
    Subclasses override methods where they need different behavior.
    """
    
    def on(self, switch):
        """Default: if on() is called, assume light is already on."""
        print("Light is already on.")
        
    def off(self, switch):
        """Default: if off() is called, assume light is already off."""
        print("Light is already off.")
        

class OnState(State):
    """
    Concrete state representing the 'on' state of the light.
    
    - on() is inherited from State (prints "already on")
    - off() is overridden to handle the transition to OffState
    """
    
    def __init__(self):
        # Announcement when entering this state
        print("Light is on")
        
    def off(self, switch):
        """
        Handle the 'off' action when light is currently on.
        This causes a state transition: OnState -> OffState
        """
        print("Turning light off...")
        # Change the switch's state to a new OffState instance
        # This is the key part - states modify the context's state!
        switch.state = OffState()
        
        
class OffState(State):
    """
    Concrete state representing the 'off' state of the light.
    
    - off() is inherited from State (prints "already off")
    - on() is overridden to handle the transition to OnState
    """
    
    def __init__(self):
        # Announcement when entering this state
        print("Light is off")
        
    def on(self, switch):
        """
        Handle the 'on' action when light is currently off.
        This causes a state transition: OffState -> OnState
        """
        print("Turning light on")
        # Change the switch's state to a new OnState instance
        switch.state = OnState()
        
        
if __name__ == "__main__":
    # Create a switch - starts in OffState
    # Output: "Light is off"
    sw = Switch()
    
    # Turn on: OffState.on() is called -> transitions to OnState
    # Output: "Turning light on" then "Light is on"
    sw.on()
    
    # Turn off: OnState.off() is called -> transitions to OffState
    # Output: "Turning light off..." then "Light is off"
    sw.off()
    
    # Try to turn off again: OffState.off() uses default from State
    # Output: "Light is already off."
    sw.off()
    
    # Try to turn off again: same result
    # Output: "Light is already off."
    sw.off()