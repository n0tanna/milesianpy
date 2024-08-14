import milesianpy.common_operators as common_operators
import milesianpy.error_handling.operator_error as operator_error
import milesianpy.error_handling.bracket_error as bracket_error
import milesianpy.error_handling.decimal_error as decimal_error
import milesianpy.error_handling.invalid_character_error as invalid_character_error


class BasicParser:
    @staticmethod
    def bracket_multiplication_insertion(user_input: list):
        previous_value = ''
        new_user_input = []
        operator_error_class = operator_error.OperatorError

        for x in user_input:
            if previous_value.isnumeric() and x in common_operators.CommonOperators.LEFT_BRACKET.value:
                new_user_input.append('*')
                new_user_input.append(x)

            elif previous_value in common_operators.CommonOperators.RIGHT_BRACKET.value and x.isnumeric():
                raise operator_error_class("Missing operator.")

            else:
                previous_value = x
                new_user_input.append(x)

        return new_user_input

    @staticmethod
    def check_bracket_count(user_input: list):
        left_bracket_count = 0
        right_bracket_count = 0
        bracket_error_class = bracket_error.BracketError

        for x in common_operators.CommonOperators.LEFT_BRACKET.value:
            left_bracket_count += user_input.count(x)

        for x in common_operators.CommonOperators.RIGHT_BRACKET.value:
            right_bracket_count += user_input.count(x)

        if right_bracket_count != left_bracket_count:
            raise bracket_error_class("No closing bracket.")

        if left_bracket_count > 0:
            return True

        return False

    @staticmethod
    def check_if_empty_bracket(user_input: list):
        left_value = ''
        bracket_error_class = bracket_error.BracketError

        for x in user_input:
            if x in common_operators.CommonOperators.LEFT_BRACKET.value:
                left_value = x

            elif x in common_operators.CommonOperators.RIGHT_BRACKET.value and left_value:
                raise bracket_error_class("No content in bracket.")

            else:
                left_value = ''

        return False

    @staticmethod
    def check_double_operators(user_input: list, passed_valid_operators: list = None):
        previous_value = ''
        operator_error_class = operator_error.OperatorError

        if passed_valid_operators is None:
            passed_valid_operators = common_operators.CommonOperators.VALID_OPERATORS.value

        for x in user_input:
            if previous_value is x in passed_valid_operators:
                raise operator_error_class(previous_value + " cannot be beside " + x + ".")

            else:
                previous_value = x

        return False

    @staticmethod
    def check_decimals(user_input: list):
        decimal = '.'
        previous_value = ''
        decimal_error_class = decimal_error.DecimalError

        for x in user_input:
            if x is decimal and previous_value is not decimal:
                if previous_value == '' or previous_value in common_operators.CommonOperators.VALID_CHARACTERS.value:
                    raise decimal_error_class("Decimals require numbers on both sides.")

                previous_value = decimal

            elif x is decimal and previous_value is decimal:
                raise decimal_error_class("Too many decimals for one number.")

            else:
                if previous_value is decimal and x in common_operators.CommonOperators.VALID_CHARACTERS.value:
                    raise decimal_error_class("Decimals require numbers on both sides.")

                previous_value = x

        if user_input[len(user_input) - 1] is '.':
            raise decimal_error_class("Decimals require numbers on both sides.")

        return True

    @staticmethod
    def check_values(user_input: list, passed_valid_characters: list = None):
        invalid_character_error_class = invalid_character_error.InvalidCharacterError

        if passed_valid_characters is None:
            passed_valid_characters = common_operators.CommonOperators.VALID_CHARACTERS.value

        for x in user_input:
            if x not in passed_valid_characters and not x.isalnum():
                raise invalid_character_error_class("Invalid character: " + x + ".")

        return True

    @staticmethod
    def standardize_brackets(user_input: list):
        user_input = list(map(lambda x: x.replace('{', '('), user_input))
        user_input = list(map(lambda x: x.replace('}', ')'), user_input))
        user_input = list(map(lambda x: x.replace('[', '('), user_input))
        user_input = list(map(lambda x: x.replace(']', ')'), user_input))

        return user_input

    @staticmethod
    def has_variables(user_input: list):
        variable_list = []
        for x in user_input:
            if x.isalpha():
                if x not in variable_list:
                    variable_list.append(x)

        if len(variable_list) == 0:
            return 0

        else:
            return variable_list


