class Lamp:
    def __init__(self, watt):
        self.watt = watt


class Dimmer:
    def __init__(self, min_power: int, max_power: int):
        self._min_power = min_power
        self._max_power = max_power
        self.lamps = []
        self._power = 0

    def add_lamp(self, lamp: Lamp):
        self.lamps.append(lamp)

    def power(self, power: int):
        self._power = power

    @property
    def consumption(self):
        return sum([lamp.watt / 100 * self._power for lamp in self.lamps])
