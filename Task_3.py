class DataComparator:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other) -> bool:
        if isinstance(other, DataComparator):
            return self.data == other.data
        if isinstance(self.data, str) and isinstance(other, str):
            return len(self.data) == len(other)
        if isinstance(self.data, int) and isinstance(other, int):
            return len(str(self.data)) == len(str(other))
        if isinstance(self.data, list) and isinstance(other, list):
            return len(self.data) == len(other)
        if isinstance(self.data, dict) and isinstance(other, dict):
            return sum(self.data.keys()) + sum(self.data.values()) == sum(other.keys()) + sum(other.values())
        return NotImplemented

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        if isinstance(other, DataComparator):
            return self.data < other.data
        return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, DataComparator):
            return self.data <= other.data
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, DataComparator):
            return self.data > other.data
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, DataComparator):
            return self.data >= other.data
        return NotImplemented