import pytest
import json
import number_parser
from tests import test_runner

number_parser_class = number_parser.NumberParser()


@pytest.fixture
def setup_data():
    json_file = open('../test_data/parsing_data/number_parser_testing_data.json')
    json_data = json.load(json_file)
    yield json_data
    json_file.close()


def test_convert_to_nums(setup_data):
    test_runner.test_runner(setup_data, 'convert_to_nums', number_parser_class.convert_to_nums)


def test_is_negative(setup_data):
    test_runner.test_runner(setup_data, 'is_negative', number_parser_class.is_negative)
