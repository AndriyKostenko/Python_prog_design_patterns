"""
Strategy Design Pattern Implementation

The Strategy pattern defines a family of algorithms, encapsulates each one,
and makes them interchangeable. It lets the algorithm vary independently
from clients that use it.
"""

from abc import ABC, abstractmethod
from enum import Enum, auto


class OutputFormat(Enum):
    """Enum defining available output formats for list rendering."""
    MARKDOWN = auto()
    HTML = auto()


class ListStrategy(ABC):
    """
    Abstract base class defining the interface for list rendering strategies.
    
    All concrete strategies must implement these methods to handle
    list creation in their specific format.
    """
    
    @abstractmethod
    def start(self, buffer):
        """Initialize the list structure (e.g., opening tags)."""
        pass
    
    @abstractmethod
    def end(self, buffer):
        """Finalize the list structure (e.g., closing tags)."""
        pass
    
    @abstractmethod
    def add_list_item(self, buffer, item):
        """Add a single item to the list."""
        pass


class MarkDownListStrategy(ListStrategy):
    """Concrete strategy for rendering lists in Markdown format."""
    
    def start(self, buffer):
        # Markdown lists don't need opening tags
        pass
    
    def end(self, buffer):
        # Markdown lists don't need closing tags
        pass
    
    def add_list_item(self, buffer, item):
        # Markdown uses asterisk (*) for unordered list items
        buffer.append(f" * {item}\n")


class HtmlListStrategy(ListStrategy):
    """Concrete strategy for rendering lists in HTML format."""
    
    def start(self, buffer):
        # HTML unordered lists start with <ul> tag
        buffer.append("<ul>\n")
        
    def end(self, buffer):
        # HTML unordered lists end with </ul> tag
        buffer.append("</ul>\n")
        
    def add_list_item(self, buffer, item):
        # Each HTML list item is wrapped in <li> tags
        buffer.append(f" <li>{item}</li>\n")


class TextProcessor:
    """
    Context class that uses a ListStrategy to process and render lists.
    
    The strategy can be changed at runtime, allowing dynamic switching
    between different output formats.
    """
    
    def __init__(self, list_strategy=HtmlListStrategy()):
        """
        Initialize the text processor with a default strategy.
        
        Args:
            list_strategy: The initial list rendering strategy (default: HTML)
        """
        self.list_strategy = list_strategy
        self.buffer = []  # Stores the rendered output
        
    def append_list(self, items):
        """
        Render a list of items using the current strategy.
        
        Args:
            items: Iterable of items to be added to the list
        """
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)
        
    def set_output_format(self, format_):
        """
        Change the output format by switching the strategy.
        
        Args:
            format_: OutputFormat enum value specifying the desired format
        """
        match format_:
            case OutputFormat.MARKDOWN:
                self.list_strategy = MarkDownListStrategy()
            case OutputFormat.HTML:
                self.list_strategy = HtmlListStrategy()
                
    def clear(self):
        """Clear the output buffer."""
        self.buffer.clear()
        
    def __str__(self):
        """Return the rendered output as a string."""
        return ''.join(self.buffer)


if __name__ == "__main__":
    # Demo: Create a list of items to render
    items = ['foo', 'bar', 'baz']
    
    # Create a text processor (defaults to HTML)
    tp = TextProcessor()
    
    # Switch to Markdown format and render the list
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)
    
    # Switch to HTML format, clear buffer, and render again
    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)