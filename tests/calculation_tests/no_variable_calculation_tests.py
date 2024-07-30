import pytest
import json
from calculations import no_variable_calculation
from tests import test_runner

no_variable_calculation_class = no_variable_calculation.NoVariableCalculation()


@pytest.fixture
def setup_data():
    json_file = open('../test_data/calculation_data/no_variable_calculation_data.json')
    json_data = json.load(json_file)
    yield json_data
    json_file.close()


def test_convert_to_nums(setup_data):
    test_runner.test_runner(setup_data, 'no_variable_basic_calculation', no_variable_calculation_class.no_variable_basic_calculation)



