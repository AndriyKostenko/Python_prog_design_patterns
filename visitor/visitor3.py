# ============================================================
# LIBRARY CODE - Generic Visitor Pattern Implementation
# This implements the "Acyclic Visitor" pattern using decorators
# to achieve method overloading based on argument type
# ============================================================

def _qualname(obj):
    """
    Get the fully-qualified name of an object (including module).
    Example: For a method in class ExpressionPrinter in module __main__,
    returns '__main__.ExpressionPrinter.visit'
    """
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """
    Get the name of the class that declared an object.
    Strips the method name from the fully-qualified name.
    Example: '__main__.ExpressionPrinter.visit' -> '__main__.ExpressionPrinter'
    """
    name = _qualname(obj)
    return name[:name.rfind('.')]  # Remove everything after last '.'


# Global dictionary that stores visitor methods
# Key: tuple of (visitor_class_qualname, argument_type)
# Value: the actual method function to call
_methods = {}


def _visitor_impl(self, arg):
    """
    Actual visitor method implementation - the dispatcher.
    This replaces all @visitor decorated methods.
    Looks up the correct method based on:
      - The visitor class (type(self))
      - The argument type (type(arg))
    """
    # Find the right method from _methods dictionary
    method = _methods[(_qualname(type(self)), type(arg))]
    # Call it with self and the argument
    return method(self, arg)


def visitor(arg_type):
    """
    Decorator factory that creates a visitor method for a specific type.
    
    Usage:
        @visitor(SomeClass)
        def visit(self, obj):
            # handle SomeClass
    
    Args:
        arg_type: The type this method should handle
        
    Returns:
        A decorator function
    """
    def decorator(fn):
        # Get the class name where this method is defined
        declaring_class = _declaring_class(fn)
        
        # Register this method in the global _methods dictionary
        # Key: (class_name, argument_type) -> Value: the original function
        _methods[(declaring_class, arg_type)] = fn

        # Return _visitor_impl to replace ALL decorated methods
        # This way, calling visit() always goes through the dispatcher
        return _visitor_impl

    return decorator


# ============================================================
# APPLICATION CODE - Expression classes and Visitor
# ============================================================


class DoubleExpression:
    """
    Leaf expression representing a numeric value.
    Part of the Composite pattern for building expression trees.
    """
    def __init__(self, value):
        self.value = value
        
    def accept(self, visitor):
        """
        Accept method for Visitor pattern.
        Calls visitor.visit(self) - the visitor will dispatch
        to the correct method based on this object's type.
        """
        visitor.visit(self)


class AdditionExpression:
    """
    Composite expression representing addition of two expressions.
    Can contain other expressions (both Double and Addition).
    """
    def __init__(self, left, right):
        self.left = left    # Left operand (any expression)
        self.right = right  # Right operand (any expression)
        
    def accept(self, visitor):
        """
        Accept method for Visitor pattern.
        Delegates to visitor which handles the traversal.
        """
        visitor.visit(self)
        
        
class ExpressionPrinter:
    """
    Concrete Visitor that prints expressions as strings.
    Uses @visitor decorator to handle different expression types.
    """
    def __init__(self):
        self.buffer = []  # Accumulates string parts
    
    @visitor(DoubleExpression)
    def visit(self, double_expression):
        """
        Handle DoubleExpression - just append its value.
        Note: Both visit methods have the same name but different
        @visitor decorators - the decorator handles dispatching.
        """
        self.buffer.append(str(double_expression.value))
        
    @visitor(AdditionExpression)
    def visit(self, addition_expression):
        """
        Handle AdditionExpression - format as (left+right).
        Recursively visits left and right sub-expressions
        by calling their accept() methods.
        """
        self.buffer.append('(')
        addition_expression.left.accept(self)   # Visit left operand
        self.buffer.append('+')
        addition_expression.right.accept(self)  # Visit right operand
        self.buffer.append(')')
    
    def __str__(self):
        """Return the accumulated buffer as a string."""
        return ''.join(self.buffer)
        

if __name__ == '__main__':
    # Build expression tree for: 1 + (2+3)
    #
    #        AdditionExpression
    #       /                  \
    #  DoubleExpr(1)    AdditionExpression
    #                   /                \
    #              DoubleExpr(2)    DoubleExpr(3)
    
    expression = AdditionExpression(
        DoubleExpression(1), 
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    
    # Create visitor and traverse the expression tree
    printer = ExpressionPrinter()
    printer.visit(expression)  # Starts traversal at root
    print(printer)  # Output: (1+(2+3))