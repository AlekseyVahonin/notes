class EmptyValueError(Exception):
    def __init__(self, message="Значение не должно быть пустым"):
        self.message = message
        super().__init__(self.message)