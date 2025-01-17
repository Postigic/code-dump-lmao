import random
from logger import log_event
from utilities import *

class Core:
    def __init__(self):
        self.temperature = 3000
        self.cooling_level = 50
        self.energy_output = 50
        self.pressure = 1.0
        self.energy_efficiency = 90
        self.coolant_supply = 100
        self.structural_integrity = 100
        self.radiation_level = 0.5
        self.max_temperature = 10000
        self.min_temperature = 2000
        self.status_effects = []


    def update_core(self):
        cooling_factor = self.cooling_level * random.uniform(0.9, 1.1)
        energy_factor = self.energy_output * random.uniform(0.8, 1.2)

        self.temperature += energy_factor * 0.05 - cooling_factor * 0.1

        self.pressure = max(1.0, self.temperature / 1000)
        self.radiation_level = (self.energy_output / 100) + (self.temperature / 10000)

        if self.temperature > 7000 or self.temperature < 3000:
            self.energy_efficiency -= 0.5
        if self.pressure > 5:
            self.energy_efficiency -= 0.2

        coolant_drain_factor = (100 - self.cooling_level) * random.uniform(0.05, 0.1)
        self.coolant_supply -= coolant_drain_factor

        self.process_status_effects()

        if random.random() < 0.005:  # normal value is 0.005, set to 0.5 for debugging
            self.random_event()

        self.temperature = max(self.min_temperature, min(self.max_temperature, self.temperature))
        self.coolant_supply = max(0, min(100, self.coolant_supply))
        self.structural_integrity = max(0, min(100, self.structural_integrity))
        self.energy_efficiency = max(0, min(100, self.energy_efficiency))


    def random_event(self):
        event = random.choice([
            "Coolant Impurity: Efficiency of cooling system reduced.",
            "Energy Surge: Output has increased significantly.",
            "System Overload: Failed to fetch core status.",
            "Coolant Leak: Major drop in coolant levels detected.",
            "Pressure Spike: Sudden increase in core pressure, structural integrity at risk."
            # Power Grid Malfunction: Cuts screen off for a few seconds due to the need to switch to backup power (takes time)
            # Connection Latency: Increases delay from command prompt to command execution
            # Radiation: Blurs terminal screen and reduces integrity
        ])
        log_event(f"[WARN]: {event}", ORANGE)

        if event == "Coolant Impurity: Efficiency of cooling system reduced.":
            self.status_effects.append({
                "name": "Coolant Impurity",
                "duration": random.randint(10, 20),
                "effect": lambda core: setattr(core, "cooling_level", max(0, core.cooling_level - 1))
            })
        elif event == "Energy Surge: Output has increased significantly.":
            self.energy_output += random.randint(20, 50)
            self.temperature += random.randint(100, 300)
        elif event == "System Overload: Failed to fetch core status.":
            self.status_effects.append({
                "name": "System Overload",
                "duration": random.randint(3, 7),
                "effect": lambda core: None
            })
        elif event == "Coolant Leak: Major drop in coolant levels detected.":
            self.coolant_supply -= random.randint(10, 30)
        elif event == "Pressure Spike: Sudden increase in core pressure, structural integrity at risk.":
            self.pressure += random.uniform(1.0, 3.0)


    def process_status_effects(self):
        for effect in list(self.status_effects):
            effect["effect"](self)
            effect["duration"] -= 1
            if effect["duration"] <= 0:
                # log_event(f"[INFO]: {effect['name']} effect has worn off.", WHITE)  # debug lol
                self.status_effects.remove(effect)
                

    def get_status(self):
        if any(effect["name"] == "System Overload" for effect in self.status_effects):
            return ["ERROR: Unable to fetch core status due to critical system overload!"]

        status = [
            f"Core Temperature: {self.temperature:.2f}°C",
            f"Cooling Level: {self.cooling_level}%",
            f"Energy Output: {self.energy_output}%",
            f"Pressure: {self.pressure:.2f} bar",
            f"Radiation Level: {self.radiation_level:.2f} mSv/h",
            f"Energy Efficiency: {self.energy_efficiency:.2f}%",
            f"Coolant Supply: {self.coolant_supply:.2f}%",
            f"Structural Integrity: {self.structural_integrity:.2f}%",
        ]

        if self.temperature >= self.max_temperature:
            status.append("WARNING: Core Overheating! Immediate action required!")
        elif self.temperature <= self.min_temperature:
            status.append("WARNING: Core is too cold! Energy output may be inefficient!")

        if self.structural_integrity <= 20:
            status.append("WARNING: Structural Integrity Critical! Risk of failure!")

        if self.coolant_supply == 0:
            status.append("WARNING: Coolant supply depleted! Immediate action required!")
        elif self.coolant_supply <= 10:
            status.append("WARNING: Coolant supply critically low!")

        else:
            status.append("Core is stable.")

        return status