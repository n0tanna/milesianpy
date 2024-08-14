import milesianpy.parsers.number_parser as number_parser
import milesianpy.parsers.basic_parser as basic_parser
import milesianpy.calculations.common_functions as common_functions


class NoVariableCalculation:
    @staticmethod
    def no_variable_basic_calculation(user_input: list):
        number_class = number_parser.NumberParser()
        basic_class = basic_parser.BasicParser()
        common_class = common_functions.CommonFunctions()

        has_brackets = basic_class.check_bracket_count(user_input)

        if has_brackets:
            user_input = basic_class.standardize_brackets(user_input)
            user_input = basic_class.bracket_multiplication_insertion(user_input)
            user_input = number_class.convert_to_nums(user_input)

            right_bracket_index = user_input.index(')')
            left_bracket_index = common_class.final_instance(user_input, '(')

            if right_bracket_index < left_bracket_index:
                response = common_class.multiple_nested_brackets(user_input)

            else:
                response = common_class.singular_nested_brackets(user_input)
                response = common_class.calculate_values(user_input)

        else:
            user_input = number_class.convert_to_nums(user_input)
            response = common_class.no_brackets_bedmas(user_input)

        return response

