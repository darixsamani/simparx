


class PathDoNotExiste(Exception):

    """
        File Do not exist    
    """

    def __init__(self, message = "File you have between does not exist") -> None:
        super().__init__(message)


