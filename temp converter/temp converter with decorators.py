FAR_ZERO = 32.00
FAR_CONSTANT = 1.8


class Temp:
    def __init__(self, temperature, unit='C'):
        if unit == 'C':
            self._cent = temperature
        elif unit == 'F':
            self.far()

    def __repr__(self):
        return 'Temp({self._cent},"C")'

    def __str__(self):
        return f'{self._cent}\N{DEGREE CELSIUS}'

    @property
    def cent(self):
        return self._cent

    @cent.setter
    def cent(self, value):
        self._cent = value

    @property
    def far(self):
        return self._cent * FAR_CONSTANT + FAR_ZERO

    @far.setter
    def far(self, value):
        self._cent = (value - FAR_ZERO) / FAR_CONSTANT

