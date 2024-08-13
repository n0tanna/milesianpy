class DecimalError(Exception):
    """ Exception raised for errors with brackets input by the user.

    Attributes:
        message -- explanation of the error.
    """

    def __init__(self, message="Decimals are not in the proper decimal format."):
        self.message = message
        super().__init__(self.message)
