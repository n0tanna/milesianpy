valid_characters = ['{', '[', '(', ')', ']', '}', '*', '/', '^', '+', '-', '=', '.']
valid_operators = ['-', '+', '/', '*', '^']
left_bracket = ['{', '[', '(']
right_bracket = [')', ']', '}']


class BasicParser:
    @staticmethod
    def bracket_multiplication_insertion(user_input: list):
        previous_value = ''
        new_user_input = []

        for x in user_input:
            if previous_value.isnumeric() and x in left_bracket:
                new_user_input.append('*')
                new_user_input.append(x)

            elif previous_value in right_bracket and x.isnumeric():
                raise Exception("Formatting Error: missing operator.")

            else:
                previous_value = x
                new_user_input.append(x)

        return new_user_input

    @staticmethod
    def check_bracket_count(user_input: list):
        left_bracket_count = 0
        right_bracket_count = 0

        for x in left_bracket:
            left_bracket_count += user_input.count(x)

        for x in right_bracket:
            right_bracket_count += user_input.count(x)

        if right_bracket_count != left_bracket_count:
            raise Exception("Formatting Error: no closing bracket.")

        if left_bracket_count > 0:
            return True

        return False

    @staticmethod
    def check_if_empty_bracket(user_input: list):
        left_value = ''
        for x in user_input:
            if x in left_bracket:
                left_value = x

            elif x in right_bracket and left_value:
                raise Exception("Formatting Error: no content in bracket.")

            else:
                left_value = ''

        return False

    @staticmethod
    def check_double_operators(user_input: list, passed_valid_operators: list = None):
        previous_value = ''

        if passed_valid_operators is None:
            passed_valid_operators = valid_operators

        for x in user_input:
            if previous_value is x in passed_valid_operators:
                raise Exception("Formatting Error: " + previous_value + " cannot be beside " + x + ".")

            else:
                previous_value = x

        return False

    @staticmethod
    def check_decimals(user_input: list):
        decimal = '.'
        previous_value = ''

        for x in user_input:
            if x is decimal and previous_value is not decimal:
                if previous_value == '' or previous_value in valid_characters:
                    raise Exception("Formatting Error: decimals require numbers on both sides.")

                previous_value = decimal

            elif x is decimal and previous_value is decimal:
                raise Exception("Formatting Error: too many decimals for one number.")

            else:
                if previous_value is decimal and x in valid_characters:
                    raise Exception("Formatting Error: decimals require numbers on both sides.")

                previous_value = x

        if user_input[len(user_input) - 1] is '.':
            raise Exception("Formatting Error: decimals require numbers on both sides.")

        return True

    @staticmethod
    def check_values(user_input: list, passed_valid_characters: list = None):
        if passed_valid_characters is None:
            passed_valid_characters = valid_characters

        for x in user_input:
            if x not in passed_valid_characters and not x.isalnum():
                raise Exception("Formatting Error: Invalid character: " + x + ".")

        return True

    @staticmethod
    def standardize_brackets(user_input: list):
        user_input = list(map(lambda x: x.replace('{', '('), user_input))
        user_input = list(map(lambda x: x.replace('}', ')'), user_input))
        user_input = list(map(lambda x: x.replace('[', '('), user_input))
        user_input = list(map(lambda x: x.replace(']', ')'), user_input))

        return user_input
