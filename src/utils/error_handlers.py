# utils/error_handlers.py

class CustomError(Exception):
    """A custom exception for handling errors."""
    def __init__(self, message="An error occured."):
        self.message = message
        super().__init__(self.message)
    

class FileFormatError(CustomError):
    """ Raised when there's an issue with file format."""
    def __init__(self, message="Invalid file format."):
        super().__init__(message)
    

class UploadError(CustomError):
    """Raised when an error occurs during upload."""
    def __init__(self, message="Failed to upload the file."):
        super().__init__(message)


class VideoProcessingError(CustomError):
    """Raised for issues related to video processing."""
    def __init__(self, message="Error occurred during video processing."):
        super().__init__(message)


class ConfigurationError(CustomError):
    """Raised for issues related to configuration."""
    def __init__(self, message="Invalid configuration or settings."):
        super().__init__(message)

