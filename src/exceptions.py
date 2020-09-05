class MapExceptions(Exception):

    def __init__(self, error_msg="There was some error. Please try again."):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class InvalidFieldToFileMapException(MapExceptions):
    """"
    Exception thrown when the field Maps do not adhere to the columns inside the xlsx file
    """
    pass


class InvalidFileFormatException(MapExceptions):
    """"
    Only xlsx files are allowed for now
    """
    pass


class FileNotFoundException(MapExceptions):
    """"
    Could not find a file
    """
    pass
