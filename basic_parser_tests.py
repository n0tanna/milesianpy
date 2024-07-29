import pytest
import json
from parsers import basic_parser


@pytest.fixture
def setup_data():
    json_file = open('tests/test_data/basic_parser_testing_data.json')
    json_data = json.load(json_file)
    print(json_data)
    yield json_data
    json_file.close()


def test_example(setup_data):
    basic_parser_class = basic_parser.BasicParser()
    for x in setup_data['check_values']:
        equation = x['test_data']
        if x['test_result']['exception'] is False:
            response = basic_parser_class.check_values(equation)
            assert response == x['test_result']['result']

        elif x['test_result']['exception'] is True:
            with pytest.raises(Exception) as error:
                basic_parser_class.check_values(equation)
            assert str(error.value) == x['test_result']['result']


# check_values - positive tests
def test_check_values_positive_1(setup_data):
    basic_parser_class = basic_parser.BasicParser()
    equation = list("4.23+234")
    response = basic_parser_class.check_values(equation)
    assert response is True


def test_check_values_positive_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("(4.23323242343-234)*8")
    response = basic_parser_class.check_values(equation)
    assert response is True


def test_check_values_positive_3():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("{(4.23323242343-234)/684.2}*4")
    response = basic_parser_class.check_values(equation)
    assert response is True


def test_check_values_positive_4():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("[(99x-234)/684.2]*4")
    response = basic_parser_class.check_values(equation)
    assert response is True


# check_values - negative tests
def test_check_values_negative_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("4.23+23%4")
    with pytest.raises(Exception): basic_parser_class.check_values(equation)


def test_check_values_negative_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list(";:|")
    with pytest.raises(Exception): basic_parser_class.check_values(equation)


# check_decimals - positive tests
def test_check_decimals_positive_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2")
    response = basic_parser_class.check_decimals(equation)
    assert response is True


def test_check_decimals_positive_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("7878.3-2.1*3.4")
    response = basic_parser_class.check_decimals(equation)
    assert response is True


# check_decimals - negative tests
def test_check_decimals_negative_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1..2")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


def test_check_decimals_negative_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2*3..4")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


def test_check_decimals_negative_3():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2*3.4/5.....6")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


def test_check_decimals_negative_4():
    basic_parser_class = basic_parser.BasicParser()
    equation = list(".2*3.4/5.6")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


def test_check_decimals_negative_5():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2*3.4/.6")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


def test_check_decimals_negative_6():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2*3.4/6.+1")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


def test_check_decimals_negative_7():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("100.3*.3432")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


def test_check_decimals_negative_8():
    basic_parser_class = basic_parser.BasicParser()
    equation = list(".43")
    with pytest.raises(Exception): basic_parser_class.check_decimals(equation)


# check_double_operator - positive tests
def test_check_double_operator_positive_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2+5")
    response = basic_parser_class.check_double_operators(equation)
    assert response is False


def test_check_double_operator_positive_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("(1.2/665)")
    response = basic_parser_class.check_double_operators(equation)
    assert response is False


# check_double_operator - negative tests
def test_check_double_operator_negative_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2++5")
    with pytest.raises(Exception): basic_parser_class.check_double_operators(equation)


def test_check_double_operator_negative_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2+5//")
    with pytest.raises(Exception): basic_parser_class.check_double_operators(equation)


def test_check_double_operator_negative_3():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("**1.2+5")
    with pytest.raises(Exception): basic_parser_class.check_double_operators(equation)


# check_brackets - positive tests
def test_check_brackets_positive_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("(1.2+5)")
    response = basic_parser_class.check_bracket_count(equation)
    assert response is True


def test_check_brackets_positive_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("{1.2+5}")
    response = basic_parser_class.check_bracket_count(equation)
    assert response is True


def test_check_brackets_positive_3():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("[1.2+5]")
    response = basic_parser_class.check_bracket_count(equation)
    assert response is True


def test_check_brackets_positive_4():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2+5")
    response = basic_parser_class.check_bracket_count(equation)
    assert response is False


def test_check_brackets_positive_5():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("(1.2-3)+(5/3)")
    response = basic_parser_class.check_bracket_count(equation)
    assert response is True


# check_brackets - negative tests
def test_check_brackets_negative_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("1.2+5)")
    with pytest.raises(Exception): basic_parser_class.check_bracket_count(equation)


def test_check_brackets_negative_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("((1.2+5)+4")
    with pytest.raises(Exception): basic_parser_class.check_bracket_count(equation)


def test_check_brackets_negative_3():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("(1.2+5)+4)))")
    with pytest.raises(Exception): basic_parser_class.check_bracket_count(equation)


def test_check_if_empty_bracket_negative_1():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("()+4)))")
    with pytest.raises(Exception): basic_parser_class.check_if_empty_bracket(equation)


def test_check_if_empty_bracket_negative_2():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("(234)+4()")
    with pytest.raises(Exception): basic_parser_class.check_if_empty_bracket(equation)


def test_check_if_empty_bracket_negative_3():
    basic_parser_class = basic_parser.BasicParser()
    equation = list("()")
    with pytest.raises(Exception): basic_parser_class.check_if_empty_bracket(equation)
