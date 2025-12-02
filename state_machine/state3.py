from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


# Use a class or mutable object to hold state across function calls
class CombinationLock:
    def __init__(self, code: str):
        self.code = code
        self.entry = ''
        self.state = State.LOCKED

    def handle_input(self) -> bool:
        """
        Process current state and return True to continue, False to exit.
        """
        match self.state:
            case State.LOCKED:
                char = input(f"Enter digit (current: {self.entry}): ")
                self.entry += char

                if self.entry == self.code:
                    self.state = State.UNLOCKED
                elif not self.code.startswith(self.entry):
                    self.state = State.FAILED
                return True  # Continue loop

            case State.FAILED:
                print("\nFAILED - Wrong code!")
                self.entry = ''
                self.state = State.LOCKED
                return True  # Continue loop

            case State.UNLOCKED:
                print("\nUNLOCKED - Welcome!")
                return False  # Exit loop

        return True  # Default: continue


if __name__ == "__main__":
    lock = CombinationLock("123")

    while lock.handle_input():
        pass  # Loop continues until handle_input returns False