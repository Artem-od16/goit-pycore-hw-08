from .field import Field


class Phone(Field):
    def __init__(self, value):
        try:
            if not value.isdigit() or len(value) != 10:
                raise ValueError("Phone number must consist of 10 digits")
            super().__init__(value)
        except ValueError as e:
            print(e)
