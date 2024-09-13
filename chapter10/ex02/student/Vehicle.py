class Vehicle: 
    def __init__(self):
        self._fuel_capacity = 0
        self._max_speed = 0
        self._current_speed = 0 

    def set_speed(self, speed):
        self._current_speed = speed

    def get_speed(self):
        return self._current_speed

    def accelerate(self, mph):
        if self._current_speed + mph < max_speed:
            self._current_speed = self._current_speed + mph
        else: 
            print("This vehicle cannot go that fast.")

    def set_fuel_capacity(self, fuel):
        self._fuel_capacity = fuel

    def get_fuel_capacity(self):
        return self._fuel_capacity

    def set_max_speed(self, max):
        self._max_speed = max 

    def get_max_speed(self):
        return self._max_speed
