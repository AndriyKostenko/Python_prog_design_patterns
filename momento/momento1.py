class Memento:
    # Simple value object to store the balance at a given moment in time
    def __init__(self, balance):
        # Snapshot of the account balance
        self.balance = balance


class BankAccount:
    # Bank account that supports undo/redo via the Memento pattern
    def __init__(self, balance=0):
        # Current balance of the account
        self.balance = balance
        # History of snapshots (mementos); start with the initial balance
        self.changes = [Memento(self.balance)]
        # Index of the current snapshot in the history
        self.current_memento = 0
        
    def deposit(self, amount):
        """Deposit money and save a new state snapshot."""
        # Update the balance
        self.balance += amount
        # Create a new memento (snapshot) with the updated balance
        memento = Memento(self.balance)
        # Store the new snapshot in the history
        self.changes.append(memento)
        # Move the current position to the latest snapshot
        self.current_memento += 1
        # Return the created memento so it can be used externally if needed
        return memento
    
    def restore(self, memento):
        """Restore the account to the state stored in the given memento."""
        if memento:
            # Set the balance to the snapshot's balance
            self.balance = memento.balance
            # Add this memento to the history (optional, depends on design)
            self.changes.append(memento)
            # Update the current index to the last snapshot
            self.current_memento = len(self.changes) - 1
            
    def undo(self):
        """Cancel the last change (move one step back in history)."""
        # You can only undo if you're not already at the first snapshot
        if self.current_memento > 0:
            # Move one step back in the history
            self.current_memento -= 1
            # Get the previous snapshot
            memento = self.changes[self.current_memento]
            # Restore the balance from that snapshot
            self.balance = memento.balance
            return memento
        # Nothing to undo
        return None
    
    def redo(self):
        """Repeat the last undone change (move one step forward in history)."""
        # You can only redo if there's a later snapshot available
        if self.current_memento + 1 < len(self.changes):
            # Move one step forward in the history
            self.current_memento += 1
            # Get the next snapshot
            memento = self.changes[self.current_memento]
            # Restore the balance from that snapshot
            self.balance = memento.balance
            return memento
        # Nothing to redo
        return None
        
    def __str__(self):
        # Human-readable representation of the account
        return f"Balance: {self.balance}"
    
    def __repr__(self):
        # Debug representation of the account
        return f"Balance: {self.balance}"
    
    
if __name__ == "__main__":
    # Example usage of BankAccount with undo/redo
    ba = BankAccount(100)   # initial balance: 100
    ba.deposit(50)          # balance: 150
    ba.deposit(25)          # balance: 175
    print(ba)
    
    ba.undo()               # undo last deposit, balance: 150
    print(f"Undo 1: {ba}")
    ba.undo()               # undo previous deposit, balance: 100
    print(f"Undo 2: {ba}")
    ba.redo()               # redo last undone deposit, balance: 150
    print(f"Redo 1: {ba}")