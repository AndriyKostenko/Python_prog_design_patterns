# Facade Pattern Implementation
# This module demonstrates the Facade design pattern by providing a simplified interface
# to a complex subsystem consisting of Buffer, Viewport, and Console classes.

class Buffer:
    """Represents a text buffer with fixed dimensions."""
    def __init__(self, width=30, height=20):
        # Initialize buffer dimensions
        self.width = width
        self.height = height
        # Create buffer as list of spaces with total capacity width*height
        self.buffer = [' '] * (width*height)
        
    def __getitem__(self, item):
        """Allow indexing into the buffer."""
        return self.buffer.__getitem__(item)
    
    def write(self, text):
        """Append text to the buffer."""
        self.buffer += text
        
class Viewport:
    """Represents a view into a buffer with an offset."""
    def __init__(self, buffer=None):
        # Use provided buffer or create a new one
        self.buffer = buffer if buffer is not None else Buffer()
        # Starting offset for viewport
        self.offset = 0

    def get_char_at(self, index):
        """Get character at specified index adjusted by viewport offset."""
        return self.buffer[index+self.offset]
    
    def append(self, text):
        """Append text to the underlying buffer."""
        self.buffer.write(text)
        
        
class Console:
    """Facade class that provides simplified interface to buffer/viewport operations."""
    def __init__(self):
        # "b" initialized only in init and then unaccessible
        b = Buffer()
        # Set up current viewport with the buffer
        self.current_viewport = Viewport(b)
        # Maintain lists of all buffers and viewports
        self.buffers = [b]
        self.viewports = [self.current_viewport]
        
    def write(self, text):
        """Write text to the current viewport's buffer."""
        self.current_viewport.buffer.write(text)
        
    def get_char_at(self, index):
        """Get character at specified index from current viewport."""
        return self.current_viewport.get_char_at(index)

# Example usage of the facade
c = Console()  # Create console instance
c.write('hello')  # Write text through the facade
ch = c.get_char_at(0)  # Get character through the facade