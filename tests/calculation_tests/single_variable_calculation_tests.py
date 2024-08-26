import pytest
import json
from milesianpy.calculations import single_variable_calculation
from tests import test_runner

single_variable_calculation_class = single_variable_calculation.SingleVariableCalculation()


@pytest.fixture
def setup_data():
    json_file = open('../test_data/calculation_data/single_variable_calculation_data.json')
    json_data = json.load(json_file)
    yield json_data
    json_file.close()


def test_single_variable_calculation(setup_data):
    test_runner.test_runner(setup_data, 'single_variable_calculation', single_variable_calculation_class.single_variable_calculation)


