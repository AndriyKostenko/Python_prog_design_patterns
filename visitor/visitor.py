class DoubleExpression:
    def __init__(self, value):
        self.value = value
        
    def print_(self, buffer):
        buffer.append(str(self.value))
        
    def eval_(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def print_(self, buffer):
        buffer.append('(')
        self.left.print_(buffer)
        buffer.append('+')
        self.right.print_(buffer)
        buffer.append(')')
        
    def eval_(self):
        return self.left.eval_() + self.right.eval_()


if __name__ == '__main__':
    # 1 + (2+3)
    expression = AdditionExpression(
        DoubleExpression(1), 
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    
    buffer = []
    expression.print_(buffer)
    print(''.join(buffer), ' = ', expression.eval_())