class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.error = error

class TypeError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.error = error
