import pytest
import json
import milesianpy.parsers.variable_parser as variable_parser
from tests import test_runner

variable_parser_class = variable_parser.VariableParser()


@pytest.fixture
def setup_data():
    json_file = open('../test_data/parsing_data/variable_parser_testing_data.json')
    json_data = json.load(json_file)
    yield json_data
    json_file.close()


def test_has_variable(setup_data):
    test_runner.test_runner(setup_data, 'has_variables', variable_parser_class.has_variables)


def test_has_equals_sign(setup_data):
    test_runner.test_runner(setup_data, 'has_equals_sign', variable_parser_class.has_equals_sign)