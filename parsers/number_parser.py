from decimal import Decimal

valid_characters = ['{', '[', '(', ')', ']', '}', '*', '/', '^', '+', '-', '=']
valid_operators = ['*', '/', '^', '+', '-', '=']
left_bracket = ['{', '[', '(']
right_bracket = [')', ']', '}']


class NumberParser:
    @staticmethod
    def convert_to_nums(user_input: list):
        converted_equation = []
        valid_num = ""

        for x in user_input:
            if x in valid_characters:
                if valid_num:
                    converted_equation.append(float(valid_num))
                    valid_num = ""

                converted_equation.append(x)

            elif x.isnumeric():
                valid_num += x

            elif x == ".":
                valid_num += x

        if valid_num:
            converted_equation.append(float(valid_num))

        return converted_equation






