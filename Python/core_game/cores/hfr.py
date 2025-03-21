import random
import sys
from logger import log_event, clear_logs
from utilities import *


def validate_int(arg):
    if isinstance(arg, int):
        return arg
    raise TypeError(f"Expected an integer, but got {type(arg).__name__}.")


class HFR:  # Hyperion Fusion Reactor
    TEMPERATURE_THRESHOLDS = {
        "meltdown": 800_000_000,
        "critical": 500_000_000,
        "danger": 300_000_000,
        "optimal": 100_000_000,
        "stall": 50_000_000,
    }


    PRESSURE_THRESHOLDS = {
        "meltdown": 15000,
        "critical": 5000,
        "danger": 3000,
        "optimal": 500,
        "stall": 100,
    }


    def __init__(self):
        self.commands = self.generate_commands()
        self.temperature = 150_000_000
        self.cooling_level = 50
        self.energy_output = 50
        self.pressure = 500.0
        self.magnetic_field_strength = 100
        self.structural_integrity = 100
        self.radiation_level = 0.5
        self.energy_buffer = 0.0
        self.status_effects = []

    
    def generate_commands(self):
        return {
            "inc_cooling": {
                "display": "inc_cooling [int]",
                "description": "Increase cooling by specified amount",
                "handler": lambda arg: self.adjust_property("cooling_level", validate_int(arg))
            },
            "dec_cooling": {
                "display": "dec_cooling [int]",
                "description": "Decrease cooling by specified amount",
                "handler": lambda arg: self.adjust_property("cooling_level", validate_int(-arg))
            },
                "inc_energy": {
                "display": "inc_energy [int]",
                "description": "Increase energy output by specified amount",
                "handler": lambda arg: self.adjust_property("energy_output", validate_int(arg))
            },
            "dec_energy": {
                "display": "dec_energy [int]",
                "description": "Decrease energy output by specified amount",
                "handler": lambda arg: self.adjust_property("energy_output", validate_int(-arg))
            },
            "vent_pressure": {
                "display": "vent_pressure",
                "description": "Vent excess pressure from the core",
                "handler": lambda _: self.vent_pressure()
            },
            "stabilize_field": {
                "display": "stabilize_field",
                "description": "Reinforce magnetic containment field",
                "handler": lambda _: self.reinforce_magnetic_field()
            },
            "help": {
                "display": "help [str]",
                "description": "Briefly explains a status term",
                "handler": lambda _: ("[INFO] Help placeholder.", WHITE)
            },
            "clear": {
                "display": "clear",
                "description": "Clears the terminal",
                "handler": lambda _: ("[INFO] Logs cleared.", WHITE) if not clear_logs() else None
            },
            "exit": {
                "display": "exit",
                "description": "Exits the control interface",
                "handler": lambda _: (pygame.quit(), sys.exit(), "")[2]
            },
        }
    

    def adjust_property(self, property_name, adjustment, max_value=100, min_value=0):
        current_value = getattr(self, property_name, 0)
        new_value = current_value + adjustment
        clamped_value = clamp(new_value, min_value, max_value)

        setattr(self, property_name, clamped_value)

        if new_value > max_value:
            return f"[WARN]: {property_name.replace('_', ' ').title()} cannot exceed {max_value}%, defaulting to max.", ORANGE
        elif new_value < min_value:
            return f"[WARN]: {property_name.replace('_', ' ').title()} cannot be less than {min_value}%, defaulting to min.", ORANGE
        else:
            return f"[LOGS] {property_name.replace('_', ' ').title()} adjusted by {adjustment}%.", WHITE


    def vent_pressure(self):
        vent_amount = random.uniform(2, 5)
        self.pressure -= vent_amount
        return f"[LOGS] Vented {vent_amount:.2f} bar of pressure", WHITE
    

    def reinforce_magnetic_field(self):
        self.magnetic_field_strength = min(100, self.magnetic_field_strength + 10)
        return f"[LOGS] Magnetic containment field reinforced by 10%.", WHITE


    def update_energy_buffer(self):
        generated = self.energy_output * random.uniform(0.8, 1.2)
        self.energy_buffer += generated * 0.1
        self.energy_buffer *= 0.99


    def update_temperature(self):
        heat_from_buffer = self.energy_buffer * 2
        cooling_effect = ((self.cooling_level / 100) ** 1.5) * 2_000_000
        fluctuation = random.uniform(-2_000_000, 5_000_000)
        self.temperature += heat_from_buffer - cooling_effect + fluctuation


    def update_pressure(self):
        base_pressure = (self.temperature / 100_000_000) ** 1.1 * 300
        pressure_drop = (self.cooling_level / 100) * 150
        self.pressure += base_pressure - pressure_drop
        self.pressure = max(0, self.pressure)


    def update_radiation(self):
        self.radiation_level += (self.energy_output / 1000)
        if self.magnetic_field_strength < 80:
            self.radiation_level += (80 - self.magnetic_field_strength) * 0.02


    def update_magnetic_field(self):
        if self.temperature > HFR.TEMPERATURE_THRESHOLDS["danger"]:
            degradation = (self.temperature - HFR.TEMPERATURE_THRESHOLDS["danger"]) * 0.00005
            self.magnetic_field_strength = max(0, self.magnetic_field_strength - degradation)
        elif self.magnetic_field_strength < 100:
            self.magnetic_field_strength = min(100, self.magnetic_field_strength + 0.5)


    def update_structural_integrity(self):
        if self.pressure > HFR.PRESSURE_THRESHOLDS["critical"]:
            self.structural_integrity -= (self.pressure - HFR.PRESSURE_THRESHOLDS["critical"]) * 0.01
        if self.radiation_level > 1.0:
            self.structural_integrity -= (self.radiation_level - 1.0) * 0.01
        self.structural_integrity = max(0, self.structural_integrity)


    def update_core(self):
        self.update_energy_buffer()
        self.update_temperature()
        self.update_pressure()
        self.update_radiation()
        self.update_magnetic_field()
        self.update_structural_integrity()

        if random.random() < 0.01:
            self.random_event()

        self.temperature = max(0, self.temperature)
        self.pressure = max(0, self.pressure)
        self.radiation_level = max(0, self.radiation_level)
        self.magnetic_field_strength = max(0, self.magnetic_field_strength)
        self.structural_integrity = max(0, self.structural_integrity)


    def random_event(self):
        events = [
            {"name": "Plasma Disruption", "description": "Plasma instability detected. Temperature spike imminent.", "effect": lambda: setattr(self, "temperature", self.temperature + random.randint(2000, 5000))},
            {"name": "Magnetic Field Failure", "description": "Magnetic containment weakening. Plasma escape imminent.", "effect": lambda: setattr(self, "magnetic_field_strength", max(0, self.magnetic_field_strength - 20))},
            {"name": "Coolant Malfunction", "description": "Coolant system failure detected. Cooling efficiency compromised.", "effect": lambda: setattr(self, "cooling_level", max(0, self.cooling_level - 10))},
            {"name": "Pressure Surge", "description": "Pressure surge detected. Reactor core under stress.", "effect": lambda: setattr(self, "pressure", self.pressure + random.uniform(1.0, 3.0))},
            # System Overload: Fails to fetch core status for a random interval of time
            # Power Grid Malfunction: Cuts screen off for a few seconds due to the need to switch to backup power (takes time)
            # Connection Latency: Increases delay from command prompt to command execution
            # Radiation: Blurs terminal screen and reduces integrity
        ]
        event = random.choice(events)
        log_event(f"[WARN] {event['name']}: {event['description']}", ORANGE)
        event["effect"]()


    def increase_energy_output(self):
        self.pressure += random.uniform(0.5, 1.5)
        self.energy_output += random.randint(20, 50)


    def process_status_effects(self):
        for effect in list(self.status_effects):
            effect["effect"](self)
            effect["duration"] -= 1
            if effect["duration"] <= 0:
                # log_event(f"[INFO]: {effect['name']} effect has worn off.", WHITE)  # debug lol
                self.status_effects.remove(effect)
                

    def get_status(self):
        status = [
            f"Core Temperature: {self.temperature:.2f} K",
            f"Cooling Level: {self.cooling_level}%",
            f"Pressure: {self.pressure:.2f} bar",
            f"Magnetic Field Strength: {self.magnetic_field_strength:.2f}%",
            f"Radiation Level: {self.radiation_level:.2f} mSv/h",
            f"Energy Output: {self.energy_output}%",
            f"Structural Integrity: {self.structural_integrity:.2f}%",
            f"Energy Buffer: {self.energy_buffer:.2f}",
        ]

        if self.temperature >= HFR.TEMPERATURE_THRESHOLDS["meltdown"]:
            pass
            # meltdown begins here
        elif self.temperature >= HFR.TEMPERATURE_THRESHOLDS["critical"]:
            pass
            # critical begins here
        elif self.temperature >= HFR.TEMPERATURE_THRESHOLDS["danger"]:
            pass
        elif self.temperature <= HFR.TEMPERATURE_THRESHOLDS["stall"]:
            pass
            # stall begins here

        if self.pressure >= HFR.PRESSURE_THRESHOLDS["critical"]:
            status.append("WARNING: Reactor pressure critical! Immediate action required!")
        elif self.pressure <= HFR.PRESSURE_THRESHOLDS["stall"]:
            status.append("WARNING: Reactor pressure too low! Immediate action required!")

        if self.magnetic_field_strength <= 30:
            status.append("WARNING: Magnetic containment field critically weak! Immediate action required!")

        if self.structural_integrity <= 20:
            status.append("WARNING: Structural Integrity is critically low! Immediate action required!")

        else:
            status.append("INFO: Core is stable.")

        return status
    

    def get_energy_quota(self):
        quota = [
            "placeholder TW",
            "placeholder%",
        ]

        return quota