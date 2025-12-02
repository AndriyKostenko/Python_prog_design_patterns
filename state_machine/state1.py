from enum import Enum, auto


class State(Enum):
    """
    Represents the possible states of a phone.
    Uses auto() to automatically assign unique integer values.
    """
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()
    

class Trigger(Enum):
    """
    Represents actions/events that can cause state transitions.
    These are the inputs that move the phone from one state to another.
    """
    CALL_DIALED = auto()
    HUNG_UP = auto()
    CALL_CONNETCED  = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()
    

if __name__ == "__main__":
    # State Machine Rules: Dictionary that maps each state to a list of
    # possible transitions. Each transition is a tuple of (trigger, next_state).
    # This is the "transition table" of the state machine.
    rules = {
        # From OFF_HOOK, you can only dial a call
        State.OFF_HOOK: [
            (Trigger.CALL_DIALED, State.CONNECTING)
        ],
        # From CONNECTING, you can hang up or get connected
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNETCED, State.CONNECTED)
        ],
        # From CONNECTED, you can leave message, hang up, or put on hold
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD)
        ],
        # From ON_HOLD, you can resume the call or hang up
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK)
        ]
    }
    
    state = State.OFF_HOOK
    exit_state = State.ON_HOOK
    
    while state != exit_state:
        print(f"The phone is currently: {state}")
        
        for i in range(len(rules[state])):
            trigger = rules[state][i][0]
            print(f"{i} : {trigger}")
            
        idx = int(input('Select a trigger: '))
        s = rules[state][idx][1]
        state = s
    print("We are done using the phone.")
        
    