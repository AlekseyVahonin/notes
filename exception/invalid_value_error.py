class InvalidValueError(Exception):
    def __init__(self, message="Недопустимое значение, необходимо ввести целое число"):
        self.message = message
        super().__init__(self.message)