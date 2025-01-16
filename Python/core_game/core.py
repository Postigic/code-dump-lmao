import random
from logger import log_event
from utilities import *

class Core:
    def __init__(self):
        self.temperature = 3000
        self.cooling_level = 50
        self.energy_output = 50
        self.max_temperature = 10000
        self.min_temperature = 2000


    def update_core(self):
        self.temperature += (self.energy_output * 0.1) - (self.cooling_level * 0.05)

        if random.random() < 0.01:
            self.random_event()

        self.temperature = max(self.min_temperature, min(self.max_temperature, self.temperature))


    def random_event(self):
        event = random.choice(["Cooling failure!", "Energy surge!", "System overload!"])
        log_event(f"EVENT: {event}", PURPLE)
        if event == "Cooling failure!":
            self.cooling_level -= random.randint(5, 15)
        elif event == "Energy surge!":
            self.energy_output += random.randint(5, 15)
        elif event == "System overload!":
            self.temperature += random.randint(5, 15)


    def get_status(self):
        status = [
            f"Core Temperature: {self.temperature:.2f}°C",
            f"Cooling Level: {self.cooling_level}%",
            f"Energy Output: {self.energy_output}%",
        ]
        if self.temperature >= self.max_temperature:
            status.append("WARNING: Core Overheating! Immediate action required!")
        elif self.temperature <= self.min_temperature:
            status.append("WARNING: Core is too cold! Energy output may be inefficient!")
        else:
            status.append("Core is stable.")
        return status