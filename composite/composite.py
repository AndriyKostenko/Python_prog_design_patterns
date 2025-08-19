"""
Composite Design Pattern Implementation

The Composite pattern allows you to compose objects into tree structures to represent 
part-whole hierarchies. It lets clients treat individual objects and compositions of 
objects uniformly.

Key components:
- Component: GraphicObject (defines interface for both leaf and composite objects)
- Leaf: Circle, Square (individual objects that can't have children)
- Composite: GraphicObject with children (can contain other GraphicObjects)

This pattern is useful for:
- Building tree structures (UI components, file systems, graphics)
- When you want to treat individual and composite objects the same way
- Implementing hierarchical structures where operations should work on both leaves and branches
"""


class GraphicObject:
    """
    Base class that serves as both Component and Composite in the pattern.
    
    Acts as:
    - Component: Defines the interface that all objects in the hierarchy must implement
    - Composite: Can contain child GraphicObjects and delegates operations to them
    
    This dual role is a common variation of the Composite pattern.
    """
    
    def __init__(self, color=None):
        """
        Initialize a graphic object.
        
        Args:
            color (str, optional): Color of the object. None means no specific color.
        """
        self.color = color
        # List to store child objects - this makes it a composite
        self.children = []  
        # Default name for composite objects
        self._name = 'Group'
    
    @property
    def name(self):
        """
        Get the display name of this graphic object.
        Subclasses can override this to provide specific names.
        """
        return self._name
    
    def add_child(self, child):
        """
        Add a child object to this composite.
        This method makes the composite nature more explicit.
        """
        self.children.append(child)
    
    def remove_child(self, child):
        """
        Remove a child object from this composite.
        """
        if child in self.children:
            self.children.remove(child)
    
    def _build_string_representation(self, depth=0):
        """
        Recursively build the string representation of the object tree.
        
        Args:
            depth (int): Current depth in the tree (used for indentation)
            
        Returns:
            str: String representation of this object and its children
        """
        # Create indentation based on depth in the tree
        indent = '*' * depth
        
        # Build the current object's representation
        color_part = self.color if self.color else ""
        current_line = f"{indent}{color_part} {self.name}\n"
        
        # Recursively get representations of all children
        children_lines = []
        for child in self.children:
            child_repr = child._build_string_representation(depth + 1)
            children_lines.append(child_repr)
        
        # Combine current object with all its children
        return current_line + ''.join(children_lines)
    
    def __str__(self):
        """
        String representation of the entire object tree.
        
        This method is much cleaner now - it simply delegates to the 
        _build_string_representation method without managing complex state.
        
        Returns:
            str: Complete string representation of the object hierarchy
        """
        return self._build_string_representation().rstrip('\n')  # Remove trailing newline


class Circle(GraphicObject):
    """
    Leaf component representing a circle.
    
    This is a concrete implementation that:
    - Inherits the composite structure (can theoretically have children)
    - Provides its own name
    - In practice, usually used as a leaf (no children added)
    """
    
    @property
    def name(self):
        """Override to provide specific name for circles"""
        return 'Circle'


class Square(GraphicObject):
    """
    Leaf component representing a square.
    
    This is a concrete implementation that:
    - Inherits the composite structure (can theoretically have children)  
    - Provides its own name
    - In practice, usually used as a leaf (no children added)
    """
    
    @property
    def name(self):
        """Override to provide specific name for squares"""
        return 'Square'


# DEMONSTRATION OF THE COMPOSITE PATTERN
if __name__ == "__main__":
    # Create the root composite object
    drawing = GraphicObject()
    drawing._name = 'My drawing'
    
    # Add individual shapes (leaf objects) directly to the drawing
    drawing.add_child(Square('Red'))
    drawing.add_child(Square('Yellow'))
    
    # Create a nested group (composite within composite)
    group = GraphicObject()  # This will have default name 'Group'
    group.add_child(Circle('Blue'))
    group.add_child(Square('Blue'))
    
    # Add the group to the main drawing
    # This demonstrates the key benefit: treating individual objects and 
    # compositions uniformly - both Square and group are added the same way
    drawing.add_child(group)
    
    # Print the entire structure
    # The Composite pattern allows us to print the entire tree structure
    # with a single operation, regardless of complexity
    print("Complete drawing structure:")
    print(drawing)
    
    print("\n" + "="*50)
    print("Pattern Benefits Demonstrated:")
    print("1. Uniform treatment: Squares and Groups added the same way")
    print("2. Tree structure: Nested groups within drawings")  
    print("3. Recursive operations: __str__ works on entire tree")
    print("4. Transparency: Client doesn't need to distinguish leaf vs composite")