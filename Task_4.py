class Kilograms:
    MAX_VALUE = 1000  # Maximum allowed value for kilograms

    def __init__(self, value):
        if value < 0:
            raise ValueError("Kilograms value cannot be negative")
        if value >= Kilograms.MAX_VALUE:
            raise ValueError("Kilograms value exceeds the maximum limit")
        self.value = value

    def to_pounds(self) -> object:
        pounds = self.value * 2.20462
        return Pounds(pounds)

    def increase(self, value):
        new_value = self.value + value
        if new_value < 0:
            raise ValueError("Kilograms value cannot be negative")
        if new_value >= Kilograms.MAX_VALUE:
            raise ValueError("Kilograms value exceeds the maximum limit")
        self.value = new_value

    def __repr__(self) -> str:
        return f"Kilograms: {self.value} kg, {self.value * 1000} g"


class Pounds:
    MAX_VALUE = 14  # Maximum allowed value for pounds

    def __init__(self, value):
        if value < 0:
            raise ValueError("Pounds value cannot be negative")
        if value >= Pounds.MAX_VALUE:
            raise ValueError("Pounds value exceeds the maximum limit")
        self.value = value

    def to_kilograms(self) -> object:
        kilograms = self.value * 0.453592
        return Kilograms(kilograms)

    def increase(self, value):
        new_value = self.value + value
        if new_value < 0:
            raise ValueError("Pounds value cannot be negative")
        if new_value >= Pounds.MAX_VALUE:
            raise ValueError("Pounds value exceeds the maximum limit")
        self.value = new_value

    def __repr__(self) -> str:
        return f"Pounds: {self.value} lb, {self.value * 16} onces"