import pytest


def test_runner(setup_data, function_name, passed_function):
    for x in setup_data[function_name]:
        equation = x['test_data']
        if x['test_result']['exception'] is False:
            response = passed_function(equation)
            assert response == x['test_result']['result']

        elif x['test_result']['exception'] is True:
            with pytest.raises(Exception) as error:
                passed_function(equation)
            assert str(error.value) == x['test_result']['result']
