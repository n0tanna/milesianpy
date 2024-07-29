import pytest
from parsers import calculation_parser
from parsers import number_parser


# check_values - positive tests
def test_check_values_positive_1():
    calculation_parser_class = calculation_parser.CalculationParser()
    equation = list("(4.23+234)")
    response = calculation_parser_class.no_variable_basic_calculation(equation, True)
    assert 238.23 == response


def test_check_values_positive_2():
    calculation_parser_class = calculation_parser.CalculationParser()
    equation = list("(((4.23+234)+3)+10)")
    response = calculation_parser_class.no_variable_basic_calculation(equation, True)
    assert 251.23 == response


def test_check_values_positive_3():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("{(4.23+1)+(3+(2+(4+3)))}+2")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    print(response)
    assert 19.23 == response


def test_check_values_positive_4():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("{(4.23+1)+(3+(2+(4+3)))}+((30+2)+6)+2")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    print(response)
    assert 57.230000000000004 == response


def test_check_values_positive_5():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("4/2")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    print(response)
    assert 2 == response


def test_check_values_positive_6():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("(4/2)+2")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    print(response)
    assert 4.0 == response


def test_check_values_positive_7():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("4/2/2")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    print(response)
    assert 1.0 == response


def test_check_values_positive_8():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("4^2")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    print(response)
    assert 16.0 == response


def test_check_values_positive_9():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("10^8")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    print(response)
    assert 100000000.0 == response
