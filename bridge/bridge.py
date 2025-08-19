"""
Bridge Design Pattern Implementation

The Bridge pattern separates an abstraction from its implementation so that both can vary independently.
It's useful when you want to avoid a permanent binding between an abstraction and its implementation.

In this example:
- Abstraction: Shape hierarchy (Shape, Circle)
- Implementation: Renderer hierarchy (Renderer, VectorRenderer, RasterRenderer)

The bridge allows any Shape to work with any Renderer without creating a cartesian product
of classes (like VectorCircle, RasterCircle, VectorSquare, RasterSquare, etc.)
"""

from abc import ABC, abstractmethod


# IMPLEMENTATION HIERARCHY - The "bridge" interface
class Renderer(ABC):
    """
    Abstract base class for rendering implementations.
    This defines the interface that all concrete renderers must implement.
    This is the "Implementation" side of the Bridge pattern.
    """
    
    @abstractmethod
    def render_circle(self, radius):
        """Abstract method that concrete renderers must implement"""
        pass

    
class VectorRenderer(Renderer):
    """
    Concrete implementation for vector-based rendering.
    Renders shapes using mathematical descriptions (scalable graphics).
    """
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')
        
        
class RasterRenderer(Renderer):
    """
    Concrete implementation for raster-based rendering.
    Renders shapes using pixels (bitmap graphics).
    """
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


# ABSTRACTION HIERARCHY - Uses the bridge to delegate to implementations        
class Shape:
    """
    Abstract base class for all shapes.
    This is the "Abstraction" side of the Bridge pattern.
    
    Key aspects:
    - Holds a reference to a Renderer (the bridge connection)
    - Delegates rendering operations to the renderer
    - Can work with any renderer implementation
    """
    def __init__(self, renderer):
        # This is the "bridge" - reference to implementation
        self.renderer = renderer
        
    def draw(self): 
        """Template method - subclasses will implement specific drawing logic"""
        pass
    
    def resize(self, factor): 
        """Template method - subclasses will implement specific resizing logic"""
        pass

    
class Circle(Shape):
    """
    Concrete shape implementation.
    Extends the Shape abstraction with circle-specific behavior.
    """
    def __init__(self, renderer, radius):
        # Call parent constructor to establish the bridge connection
        super().__init__(renderer)
        self.radius = radius
        
    def draw(self):
        """
        Implements drawing by delegating to the renderer.
        This is where the bridge is used - the shape doesn't know HOW to render,
        it just tells the renderer WHAT to render.
        """
        self.renderer.render_circle(self.radius)
        
    def resize(self, factor):
        """
        Implements resizing logic specific to circles.
        This modifies the shape's properties but doesn't affect rendering.
        """
        self.radius *= factor
        

if __name__ == "__main__":
    # Demonstration of the Bridge pattern
    
    # Create different renderer implementations
    raster = RasterRenderer()  # Pixel-based rendering
    vector = VectorRenderer()  # Vector-based rendering
    
    # Create a circle that uses vector rendering
    # The circle doesn't need to know about rendering details
    circle = Circle(vector, 5)
    
    # Draw the circle - delegates to vector renderer
    circle.draw()  # Output: "Drawing a circle of radius 5"
    
    # Resize the circle - this is shape-specific behavior
    circle.resize(2)  # Doubles the radius to 10
    
    # Draw again - same renderer, but with updated radius
    circle.draw()  # Output: "Drawing a circle of radius 10"
    
    # BRIDGE PATTERN BENEFITS DEMONSTRATED:
    # 1. We can easily switch renderers: Circle(raster, 5) would use raster rendering
    # 2. We can add new shapes (Square, Triangle) that work with existing renderers
    # 3. We can add new renderers (OpenGLRenderer) that work with existing shapes
    # 4. No explosion of classes - we avoid VectorCircle, RasterCircle, etc.