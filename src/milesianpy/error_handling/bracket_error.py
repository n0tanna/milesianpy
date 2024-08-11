class BracketError(Exception):
    """ Exception raised for errors with brackets input by the user.

    Attributes:
        message -- explanation of the error.
    """

    def __init__(self, message="Brackets are not in the proper format."):
        self.message = message
        super().__init__(self.message)
