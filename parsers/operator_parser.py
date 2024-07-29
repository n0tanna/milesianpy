class OperatorParser:
    @staticmethod
    def addition(left_value: float, right_value: float):
        return left_value + right_value

    @staticmethod
    def subtraction(left_value: float, right_value: float):
        return left_value - right_value

    @staticmethod
    def multiplication(left_value: float, right_value: float):
        return left_value * right_value

    @staticmethod
    def divide(left_value: float, right_value: float):
        return left_value / right_value

    @staticmethod
    def exponent(left_value: float, right_value: float):
        index = 0
        outcome = left_value

        while right_value - 1 > index:
            outcome *= left_value
            index += 1

        return outcome
