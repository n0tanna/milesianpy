import pytest
import json
from parsers import calculation_parser
from tests import test_runner

calculation_parser_class = calculation_parser.CalculationParser()

@pytest.fixture
def setup_data():
    json_file = open('../test_data/calculation_parser_testing_data.json')
    json_data = json.load(json_file)
    yield json_data
    json_file.close()


def test_convert_to_nums(setup_data):
    test_runner.test_runner(setup_data, 'no_variable_basic_calculation', calculation_parser_class.no_variable_basic_calculation)



