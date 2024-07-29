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
    assert 19.23 == response


def test_check_values_positive_4():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("{(4.23+1)+(3+(2+(4+3)))}+((30+2)+6)+2")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    assert 57.230000000000004 == response


def test_check_values_positive_5():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("4/2")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    assert 2 == response


def test_check_values_positive_6():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("(4/2)+2")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    assert 4.0 == response


def test_check_values_positive_7():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("4/2/2")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    assert 1.0 == response


def test_check_values_positive_8():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("4^2")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    assert 16.0 == response


def test_check_values_positive_9():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("10^8")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    assert 100000000.0 == response


def test_check_values_positive_10():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("10-8")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    assert 2.0 == response


def test_check_values_positive_11():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("10-(-8)")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    assert 18.0 == response


def test_check_values_positive_12():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("(-10)-(-8)")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    assert -2.0 == response


def test_check_values_positive_13():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("((-10)*(-8))")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    assert 80.0 == response


def test_check_values_positive_14():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("10^4")
    response = basic_parser_class.no_variable_basic_calculation(equation, False)
    assert 10000.0 == response


def test_check_values_positive_15():
    basic_parser_class = calculation_parser.CalculationParser()
    equation = list("(12-(-3))+(10^4)")
    response = basic_parser_class.no_variable_basic_calculation(equation, True)
    assert 10015.0 == response


