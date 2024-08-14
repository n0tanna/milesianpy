import milesianpy.parsers.number_parser as number_parser
import milesianpy.parsers.basic_parser as basic_parser
import milesianpy.calculations.common_functions as common_functions


class SingleVariableCalculation:

    @staticmethod
    def single_variable_calculation(user_input: list):
        number_class = number_parser.NumberParser()
        basic_class = basic_parser.BasicParser()
        common_class = common_functions.CommonFunctions()

        has_brackets = basic_class.check_bracket_count(user_input)
