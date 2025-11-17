from enum import Enum


"""
A simple expression interpreter demo:

- `lex` turns a raw string into `Token` objects (a very small lexer)
- `parse` transforms tokens into a minimal AST (Integer and BinaryExpression)
- `BinaryExpression.value` computes the arithmetic result of that AST

This file is a tiny educational example showing how an interpreter can be
built in three phases: tokenization, parsing (AST building), and evaluation.
"""


class TokenType(Enum):
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    LPAREN = 6
    RPAREN = 7
    EOF = 8


class Token:
    def __init__(self, type_, text):
        self.type = type_
        self.text = text
        
    def __str__(self):
        return f"{self.text}"


def lex(input_):
    """Lexical analyzer.

    Scans the input string and returns a list of tokens. This lexer recognizes
    single-character operators: + - * and parentheses. It also groups sequences
    of digits into multi-digit number tokens.

    Note: This is a tiny lexer for educational purposes. It does not skip
    whitespace, handle invalid characters gracefully or produce EOF tokens.
    """

    result = []
    i = 0
    while i < len(input_):
        if input_[i] == '+':
            result.append(Token(TokenType.PLUS, '+'))
        elif input_[i] == '-':
            result.append(Token(TokenType.MINUS, '-'))
        elif input_[i] == '*':
            result.append(Token(TokenType.MULTIPLY, '*'))
        elif input_[i] == '(':
            result.append(Token(TokenType.LPAREN, '('))
        elif input_[i] == ')':
            result.append(Token(TokenType.RPAREN, ')'))
        else:
            digits = [input_[i]]
            for j in range(i+1, len(input_)):
                if input_[j].isdigit():
                    digits.append(input_[j])
                    i += 1
                else:
                    # We encountered a non-digit after reading digits — commit
                    # the multi-digit number token to the results list.
                    result.append(Token(TokenType.NUMBER, ''.join(digits)))
                    break
        i += 1
    return result
# ↑↑↑ lexing ↑↑↑

# ↓↓↓ parsing ↓↓↓  
    
class Integer:
    def __init__(self, value):
        self.value = value
        # Integer AST node: holds a numeric value for leaf nodes in the AST
            
class BinaryExpression:
    class Type(Enum):
        ADDITION = 0
        SUBSTRACTION = 1
        
    def __init__(self):
        self.type = None
        self.left = None
        self.right = None
    
    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBSTRACTION:
            return self.left.value - self.right.value
        
def parse(tokens):
    """Parse tokens into an AST and return the top-level expression.

    This parser is a very small hand-coded recursive parser. It supports:
    - integer literal operands
    - binary addition and subtraction
    - nested parenthesized subexpressions

    It always returns a `BinaryExpression` object for binary operations, and
    recurses into subexpressions when parentheses are found.
    """

    result = BinaryExpression()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type == TokenType.NUMBER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == TokenType.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == TokenType.MINUS:
            result.type = BinaryExpression.Type.SUBSTRACTION
        elif token.type == TokenType.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == TokenType.RPAREN:
                    break
                j += 1
            subexpression = tokens[i+1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result
        
        
def calc(input_):
    # High level driver that tokenizes, prints tokens, parses them to AST, and
    # then prints the evaluated value.
    tokens = lex(input_)
    print('  '.join(map(str, tokens)))
    
    parsed = parse(tokens)
    print(f"{input_} = {parsed.value}")
    
if __name__ == "__main__":
    calc('(13+4)-(12+1)')