import pytest


def test_runner(setup_data, function_name, passed_function):
    for x in setup_data[function_name]:
        test_data = x['test_data']
        if x['test_result']['exception'] is False:
            response = []

            if len(test_data) is 2:
                response = passed_function(test_data[0], test_data[1])

            elif len(test_data) is 1:
                response = passed_function(test_data[0])

            assert response == x['test_result']['result']

        elif x['test_result']['exception'] is True:
            with pytest.raises(Exception) as error:
                passed_function(test_data[0])
            assert str(error.value) == x['test_result']['result']
