# utils/error_handlers.py

class CustomError(Exception):
    """A custom exception for handling errors."""
    def __init__(self, message="An error occured."):
        self.message = message
        super().__init__(self.message)