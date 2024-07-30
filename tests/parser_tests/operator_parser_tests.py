import pytest
import json
from parsers import operator_parser
from tests import test_runner

operator_parser_class = operator_parser.OperatorParser()


@pytest.fixture
def setup_data():
    json_file = open('../test_data/operator_parser_testing_data.json')
    json_data = json.load(json_file)
    yield json_data
    json_file.close()


def test_addition(setup_data):
    test_runner.test_runner(setup_data, 'addition', operator_parser_class.addition)


def test_subtraction(setup_data):
    test_runner.test_runner(setup_data, 'subtraction', operator_parser_class.subtraction)


def test_multiplication(setup_data):
    test_runner.test_runner(setup_data, 'multiplication', operator_parser_class.multiplication)


def test_division(setup_data):
    test_runner.test_runner(setup_data, 'division', operator_parser_class.division)


def test_exponent(setup_data):
    test_runner.test_runner(setup_data, 'exponent', operator_parser_class.exponent)

