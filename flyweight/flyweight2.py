class FormattedText:
    """
    Basic text formatter that applies capitalization on a per-character basis.
    
    Drawback: Uses a boolean list for each character in the text, which can
    become memory-inefficient for long texts or when there are many formatting changes.
    """

    def __init__(self, plain_text: str) -> None:
        # Store the original text
        self.plain_text = plain_text
        
        # Create a boolean list to track which characters should be capitalized
        self.caps = [False] * len(plain_text)

    def capitilize(self, start: int, end: int) -> None:
        """
        Mark a range of characters (from start to end, non-inclusive) as capitalized.
        """
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        """
        Convert the formatted text back into a string representation,
        applying uppercase transformation where indicated.
        """
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            # Apply uppercase if caps[i] is True
            result.append(c.upper() if self.caps[i] else c)
        return ''.join(result)



class TextRange:
    """
    Represents a range of text positions with specific formatting options.
    This is a more flexible way to describe text formatting.
    """
    def __init__(self, start: int, end: int, capitilize=False):
        self.start = start
        self.end = end
        self.capitilize = capitilize  # Whether this range should be capitalized

    def is_cover_position(self, position):
        """
        Check if the given character position falls within this text range.
        """
        return self.start <= position <= self.end



class BetterFormattedText:
    """
    Improved text formatter using the Flyweight pattern.

    Instead of storing a boolean flag for every character (as in FormattedText),
    this class stores only the *ranges* where formatting rules apply.

    Each `TextRange` object represents one set of formatting rules over a substring.
    This approach is more memory-efficient and flexible, allowing multiple formatting
    types (capitalize, bold, italic, etc.) in the future.
    """
    def __init__(self, plain_text: str) -> None:
        self.plain_text = plain_text
        self.formatting = []  # A list of TextRange objects

    def get_range(self, start: int, end: int):
        """
        Create and store a new TextRange for the given start and end positions.
        Returns the range so the caller can modify its formatting attributes.
        """
        range_ = TextRange(start, end)
        self.formatting.append(range_)
        return range_

    def __str__(self):
        """
        Convert the text to a formatted string, applying formatting rules
        from all stored TextRange objects.
        """
        result = []
        for index, char in enumerate(self.plain_text):
            # Check all formatting ranges to see if this position should be affected
            for range__ in self.formatting:
                if range__.is_cover_position(index) and range__.capitilize:
                    char = char.upper()
            result.append(char)
        return ''.join(result)



if __name__ == '__main__':
    text = 'This is a brave new world'

    # --- Example using the simple FormattedText ---
    ft = FormattedText(text)
    ft.capitilize(10, 15)  # Capitalize "brave"
    print(ft)  # Output: This is a BRAVE new world

    # --- Example using the BetterFormattedText (Flyweight version) ---
    bft = BetterFormattedText(text)
    range1 = bft.get_range(16, 19)  # Define a range for "new"
    range1.capitilize = True
    print(bft)  # Output: This is a brave NEW world
