
class VariableParser:
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
            return sorted(variable_list)

    @staticmethod
    def has_equals_sign(user_input: list):
        has_equals = False
        right_side = []
        left_side = []
        for x in user_input:
            if x == '=':
                has_equals = True

            else:
                if has_equals is True:
                    right_side.append(x)

                else:
                    left_side.append(x)

        return [left_side, right_side]

    @staticmethod
    def isolate_variables(user_input: list, variables: list):
        print("")

