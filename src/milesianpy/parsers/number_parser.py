import milesianpy.common_operators as common_operators


class NumberParser:
    @staticmethod
    def convert_to_nums(user_input: list):
        converted_equation = []
        valid_num = ""

        for x in user_input:
            if x in common_operators.CommonOperators.VALID_CHARACTERS_NO_DECIMALS.value:
                if valid_num:
                    converted_equation.append(float(valid_num))
                    valid_num = ""

                converted_equation.append(x)

            elif x.isnumeric():
                valid_num += x

            elif x == ".":
                valid_num += x

            elif x.isalpha():
                converted_equation.append(x)

        if valid_num:
            converted_equation.append(float(valid_num))

        converted_equation = NumberParser.is_negative(converted_equation)

        return converted_equation

    @classmethod
    def is_negative(cls, user_input: list):
        iterator = 0

        while len(user_input) > iterator:
            if user_input[iterator] == '-':
                if type(user_input[iterator - 1]) is not float and type(user_input[iterator + 1]) is float:
                    user_input[iterator + 1] = user_input[iterator + 1] * -1
                    del user_input[iterator]

            iterator += 1

        return user_input











