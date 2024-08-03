from parsers import operator_parser
from parsers import number_parser
from parsers import basic_parser
import common_operators


class NoVariableCalculation:
    @staticmethod
    def no_variable_basic_calculation(user_input: list):
        number_class = number_parser.NumberParser()
        basic_class = basic_parser.BasicParser()

        has_brackets = basic_class.check_bracket_count(user_input)

        if has_brackets:
            basic_class = basic_parser.BasicParser()
            user_input = basic_class.standardize_brackets(user_input)
            user_input = basic_class.bracket_multiplication_insertion(user_input)
            user_input = number_class.convert_to_nums(user_input)

            right_bracket_index = user_input.index(')')
            left_bracket_index = NoVariableCalculation.final_instance(user_input, '(')

            if right_bracket_index < left_bracket_index:
                response = NoVariableCalculation.multiple_nested_brackets(user_input)

            else:
                response = NoVariableCalculation.singular_nested_brackets(user_input)
                response = NoVariableCalculation.calculate_values(user_input)

        else:
            user_input = number_class.convert_to_nums(user_input)
            response = NoVariableCalculation.calculate_values(user_input)

        return response

    @classmethod
    def multiple_nested_brackets(cls, user_input: list):
        left_bracket_count = user_input.count('(')

        while left_bracket_count > 0:
            right_bracket_index = user_input.index(')')

            spliced_list = user_input[:right_bracket_index + 1]
            left_bracket_index = NoVariableCalculation.final_instance(spliced_list, '(')
            spliced_list = spliced_list[left_bracket_index:]

            calculated_value = NoVariableCalculation.singular_nested_brackets(spliced_list)
            user_input[right_bracket_index] = calculated_value
            del user_input[left_bracket_index: right_bracket_index]
            left_bracket_count = user_input.count('(')

        user_input = NoVariableCalculation.calculate_values(user_input)
        return user_input

    @classmethod
    def singular_nested_brackets(cls, user_input: list):
        left_bracket_count = user_input.count('(')
        calculated_value = 0

        while left_bracket_count > 0:
            holder = NoVariableCalculation.bracket_recursion(user_input)
            left_bracket_count_holder = holder.count('(')

            if left_bracket_count_holder == 0:
                calculated_value = NoVariableCalculation.calculate_values(holder)

                left_value = NoVariableCalculation.final_instance(user_input, '(')

                right_value = user_input.index(')')

                del user_input[left_value + 1:right_value + 1]
                user_input[left_value] = calculated_value

            left_bracket_count = user_input.count('(')

        return calculated_value

    @classmethod
    def calculate_values(cls, calculate_values: list):
        iterator = 0
        calculated_sum = calculate_values[0]
        operator = operator_parser.OperatorParser()

        while len(calculate_values) > iterator:
            if calculate_values[iterator] in common_operators.CommonOperators.VALID_OPERATORS.value:
                if calculate_values[iterator] == '+':
                    calculated_sum = operator.addition([calculated_sum, calculate_values[iterator + 1]])

                elif calculate_values[iterator] == '-':
                    calculated_sum = operator.subtraction([calculated_sum, calculate_values[iterator + 1]])

                elif calculate_values[iterator] == '*':
                    calculated_sum = operator.multiplication([calculated_sum, calculate_values[iterator + 1]])

                elif calculate_values[iterator] == '/':
                    calculated_sum = operator.division([calculated_sum, calculate_values[iterator + 1]])

                elif calculate_values[iterator] == '^':
                    calculated_sum = operator.exponent([calculated_sum, calculate_values[iterator + 1]])

                iterator += 1

            else:
                iterator += 1

        return calculated_sum

    @classmethod
    def bracket_recursion(cls, user_input: list):
        index = NoVariableCalculation.final_instance(user_input, '(')
        left_bracket_index = index
        right_bracket_index = user_input.index(')')

        return user_input[left_bracket_index + 1: right_bracket_index]

    @classmethod
    def final_instance(cls, passed_list: list, value: str):
        index = 0
        for i in range(len(passed_list) - 1, 0, -1):
            if passed_list[i] == value:
                index = i
                break

        return index
