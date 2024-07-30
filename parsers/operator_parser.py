class OperatorParser:
    @staticmethod
    def addition(equation: list):
        return equation[0] + equation[1]

    @staticmethod
    def subtraction(equation: list):
        return equation[0] - equation[1]

    @staticmethod
    def multiplication(equation: list):
        return equation[0] * equation[1]

    @staticmethod
    def division(equation: list):
        return equation[0] / equation[1]

    @staticmethod
    def exponent(equation: list):
        index = 0
        outcome = equation[0]

        while equation[1] - 1 > index:
            outcome *= equation[0]
            index += 1

        return outcome
