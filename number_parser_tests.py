import pytest
from parsers import number_parser


# convert_to_nums - positive tests
def test_convert_to_nums_positive_1():
    number_parser_class = number_parser.NumberParser()
    equation = list("4.23+234")
    response = number_parser_class.convert_to_nums(equation)
    assert response == [4.23, '+', 234.0]


def test_convert_to_nums_positive_2():
    number_parser_class = number_parser.NumberParser()
    equation = list("4.23+234(2.34567/3)")
    response = number_parser_class.convert_to_nums(equation)
    assert response == [4.23, '+', 234.0, '(', 2.34567, '/', 3.0, ')']


def test_convert_to_nums_positive_3():
    number_parser_class = number_parser.NumberParser()
    equation = list("4.23+234(2.34567/3)^3-5")
    response = number_parser_class.convert_to_nums(equation)
    assert response == [4.23, '+', 234.0, '(', 2.34567, '/', 3.0, ')', '^', 3.0, '-', 5.0]
