import milesianpy.parsers.number_parser as number_parser
import milesianpy.parsers.basic_parser as basic_parser
import milesianpy.parsers.variable_parser as variable_parser
import milesianpy.calculations.common_functions as common_functions


class SingleVariableCalculation:

    @staticmethod
    def single_variable_calculation(user_input: list):
        number_class = number_parser.NumberParser()
        basic_class = basic_parser.BasicParser()
        variable_class = variable_parser.VariableParser()
        common_class = common_functions.CommonFunctions()

        user_input = basic_class.multiplication_insertion(user_input)
        variables = variable_class.has_variables(user_input)
        user_input = number_class.convert_to_nums(user_input)
        user_input = variable_class.has_equals_sign(user_input)

        

        print(user_input)


