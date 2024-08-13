class InvalidCharacterError(Exception):
    """ Exception raised for errors with brackets input by the user.

    Attributes:
        message -- explanation of the error.
    """

    def __init__(self, message="Wrong characters have been input."):
        self.message = message
        super().__init__(self.message)
