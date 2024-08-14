import pytest
import json
import milesianpy.parsers.basic_parser as basic_parser
from tests import test_runner

basic_parser_class = basic_parser.BasicParser()


@pytest.fixture
def setup_data():
    json_file = open('../test_data/parsing_data/basic_parser_testing_data.json')
    json_data = json.load(json_file)
    yield json_data
    json_file.close()


def test_check_values(setup_data):
    test_runner.test_runner(setup_data, 'check_values', basic_parser_class.check_values)


def test_check_decimals(setup_data):
    test_runner.test_runner(setup_data, 'check_decimals', basic_parser_class.check_decimals)


def test_check_double_operators(setup_data):
    test_runner.test_runner(setup_data, 'check_double_operators', basic_parser_class.check_double_operators)


def test_check_brackets(setup_data):
    test_runner.test_runner(setup_data, 'check_bracket_count', basic_parser_class.check_bracket_count)


def test_check_if_empty_bracket(setup_data):
    test_runner.test_runner(setup_data, 'check_if_empty_bracket', basic_parser_class.check_if_empty_bracket)


def test_standardize_brackets(setup_data):
    test_runner.test_runner(setup_data, 'standardize_brackets', basic_parser_class.standardize_brackets)


def test_bracket_multiplication_insertion(setup_data):
    test_runner.test_runner(setup_data, 'bracket_multiplication_insertion', basic_parser_class.bracket_multiplication_insertion)


def test_has_variable(setup_data):
    test_runner.test_runner(setup_data, 'has_variables', basic_parser_class.has_variables)
