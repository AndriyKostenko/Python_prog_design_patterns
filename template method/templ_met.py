from abc import ABC, abstractmethod


class Game(ABC):
    """
    Abstract base class implementing the Template Method pattern.
    Defines the skeleton of the game algorithm, deferring specific steps to subclasses.
    """
    
    def __init__(self, number_of_players):
        """Initialize the game with the specified number of players."""
        self.number_of_players = number_of_players
        self.current_player = 0  # Track whose turn it is
        
    def run(self):
        """
        Template method - defines the game's algorithm structure.
        This method is final and should not be overridden by subclasses.
        """
        self.start()  # Hook: initialize the game
        while not self.have_winner:  # Keep playing until there's a winner
            self.take_turn()  # Hook: execute one turn
        print(f"Player {self.winning_player} wins!")
        
    @abstractmethod
    def start(self):
        """Abstract method: subclasses must implement game initialization."""
        pass
    
    @property
    @abstractmethod
    def have_winner(self):
        """
        Abstract property: subclasses must implement win condition check.
        Returns True if the game has a winner, False otherwise.
        Note: @property must come before @abstractmethod.
        """
        pass
    
    @abstractmethod
    def take_turn(self):
        """Abstract method: subclasses must implement turn logic."""
        pass
    
    @property
    @abstractmethod
    def winning_player(self):
        """Abstract property: subclasses must return the winning player."""
        pass
    
    
class Chess(Game):
    """
    Concrete implementation of a simplified Chess game.
    Inherits the game flow from Game and implements specific behavior.
    """
    
    def __init__(self):
        """Initialize Chess with 2 players and set maximum turns."""
        super().__init__(number_of_players=2)
        self.max_turns = 10  # Game ends after this many turns
        self.turn = 1  # Current turn counter
        
    def start(self):
        """Implementation of game start - prints game info."""
        print(f"Starting the game of Chess with: {self.number_of_players} players.")
        
    @property
    def have_winner(self):
        """Check if game has reached max turns (simplified win condition)."""
        return self.turn == self.max_turns
    
    def take_turn(self):
        """Execute one turn: print info, increment turn, switch player."""
        print(f"Turn {self.turn} taken by player: {self.current_player}")
        self.turn += 1
        # Alternate between players (0 -> 1 -> 0 -> 1...)
        self.current_player = (self.current_player + 1) % self.number_of_players
        
    @property
    def winning_player(self):
        """Return the current player as the winner."""
        return self.current_player
    

if __name__ == "__main__":
    # Create and run a Chess game
    chess = Chess()
    chess.run()