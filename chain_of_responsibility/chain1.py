class Creature:
    """
    Represents a creature with basic stats: attack and defense.
    This is the object that modifiers will act upon.
    """
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier:
    """
    Base class for all modifiers.
    Implements the Chain of Responsibility pattern.
    
    Each modifier can:
    - Apply some logic to the creature.
    - Pass control to the next modifier in the chain.
    """
    def __init__(self, creature: Creature):
        self.creature = creature
        self.next_modifier = None  # Points to the next modifier in the chain

    def add_modifier(self, modifier):
        """
        Adds a new modifier to the end of the chain.
        
        If there is already a next modifier, delegate the addition recursively.
        Otherwise, attach the new modifier here.
        """
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        """
        Passes handling to the next modifier in the chain, if any.
        This ensures each modifier gets a chance to apply its logic.
        """
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    """
    Doubles the creature's attack.
    
    After performing its action, it calls super().handle() to continue
    the chain of responsibility.
    """
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()  # Continue to the next modifier in the chain


class IncreseDfenseModifier(CreatureModifier):
    """
    Increases the creature's defense by 1, but only if its attack is <= 2.
    
    Calls super().handle() to continue the chain.
    """
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name}'s defense")
            self.creature.defense += 1
        super().handle()


class NoBonusesModifier(CreatureModifier):
    """
    Stops any bonuses from being applied.
    
    This modifier intentionally does NOT call super().handle(),
    effectively breaking the chain.
    """
    def handle(self):
        print('No bonuses for you!')
        # chain stops here, no call to super().handle()


# ---------------- Example usage ----------------

# Create a creature
goblin = Creature('Goblin', 1, 1)
print(goblin)  # Initial state

# Create the root of the modifier chain
root = CreatureModifier(goblin)

# Add modifiers to the chain
#root.add_modifier(NoBonusesModifier(goblin))       # Stops all other bonuses
root.add_modifier(DoubleAttackModifier(goblin))    # Would double attack
root.add_modifier(DoubleAttackModifier(goblin))    # Would double attack again
root.add_modifier(IncreseDfenseModifier(goblin))   # Would increase defense if attack <= 2

# Run all modifiers in order
root.handle()  # Only NoBonusesModifier runs, chain stops

print(goblin)  # Final state after applying modifiers
