import pytest
from parsers import operator_parser


# addition - positive tests
def test_addition_positive_1():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.addition(1.0, 1.0)
    assert response == 2.0


def test_addition_positive_2():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.addition(234.786, 1222229.0)
    assert response == 1222463.786


# subtraction - positive tests
def test_subtraction_positive_1():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.subtraction(1.0, 1.0)
    assert response == 0.0


def test_subtraction_positive_2():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.subtraction(2.345, 10.34)
    assert response == -7.994999999999999


# multiplication - positive tests
def test_multiplication_positive_1():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.multiplication(1.0, 1.0)
    assert response == 1.0


def test_multiplication_positive_2():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.multiplication(20, 2)
    assert response == 40


# division - positive tests
def test_divide_positive_1():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.divide(1.0, 1.0)
    assert response == 1.0


def test_divide_positive_2():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.divide(20, 2)
    assert response == 10


# division - positive tests
def test_exponent_positive_1():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.exponent(1.0, 1.0)
    assert response == 1.0


def test_exponent_positive_2():
    operator_parser_class = operator_parser.OperatorParser()
    response = operator_parser_class.exponent(5, 2)
    assert response == 25
