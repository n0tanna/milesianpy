from enum import Enum


class CommonOperators(Enum):
    VALID_CHARACTERS = ['{', '[', '(', ')', ']', '}', '*', '/', '^', '+', '-', '=', '.']
    VALID_CHARACTERS_NO_DECIMALS = ['{', '[', '(', ')', ']', '}', '*', '/', '^', '+', '-', '=']
    VALID_OPERATORS = ['-', '+', '/', '*', '^']
    LEFT_BRACKET = ['{', '[', '(']
    RIGHT_BRACKET = [')', ']', '}']
