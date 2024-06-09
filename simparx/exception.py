


class PathDoNotExiste(Exception):

    """
        PATH File Do not exist    
    """

    def __init__(self, message = "Path File you have provide does not exist") -> None:
        super().__init__(message)


