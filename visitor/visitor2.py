class DoubleExpression:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
        
class ExpressionPrinter:
    def __init__(self):
        self.buffer = []  # Buffer stored as instance variable
    
    def print_(self, expression):
        if isinstance(expression, DoubleExpression):
            self.buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            self.buffer.append('(')
            self.print_(expression.left)
            self.buffer.append('+')
            self.print_(expression.right)
            self.buffer.append(')')
    
    def result(self):
        return ''.join(self.buffer)
        

if __name__ == '__main__':
    # 1 + (2+3)
    expression = AdditionExpression(
        DoubleExpression(1), 
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    
    printer = ExpressionPrinter()
    printer.print_(expression)
    print(printer.result())