class OperatorError(Exception):
    """ Exception raised for errors with brackets input by the user.

    Attributes:
        message -- explanation of the error.
    """

    def __init__(self, message="Operators are not in the proper format."):
        self.message = message
        super().__init__(self.message)

