class MapExceptions(Exception):

    def __init__(self, error_msg="There was some error. Please try again."):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class InvalidFieldToFileMapException(Exception):
    """"
    Exception thrown when the field Maps do not adhere to the columns inside the xlsx file
    """
    def __init__(self, error_msg="InvalidFieldToFileMapException: There was some error. Please try again."):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class InvalidFileFormatException(Exception):
    """"
    Only xlsx files are allowed for now
    """

    def __init__(self, error_msg="InvalidFileFormatException: There was some error. Please try again."):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class FileNotFoundException(Exception):
    """"
    Could not find a file
    """

    def __init__(self, error_msg="FileNotFoundException: There was some error. Please try again."):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg
