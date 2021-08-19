class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.error = message

class TypeError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.error = message

class ContactNotFoundError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.error = message

