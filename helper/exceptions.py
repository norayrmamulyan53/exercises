# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class IncludesStringError(Error):
    """Raised when the input value couldn't find in file"""
    pass
