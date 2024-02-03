class Immutable:
    def new(self, value):
        self.value = value

    def get_value(self) -> object:
        return self.value

    def __setattr__(self, attr, value):
        if hasattr(self, 'value'):
            raise AttributeError("Cannot modify attribute 'value'.")
        else:
            object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        if hasattr(self, 'value'):
            raise AttributeError("Cannot delete attribute 'value'.")
        else:
            object.__delattr__(self, attr)