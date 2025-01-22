import random
from logger import log_event
from utilities import *


class Core:
    pass


class QTEC:  # scrapping this for now because it's too difficult to think of how it would work theoretically (sorry for being dumb sigh..... what can i say i'm just a chatgpt kinda guy y'know? nananananananana)
    TEMPERATURE_THRESHOLDS ={
        "critical": 8000,
        "danger": 7000,
        "stall": 3500,
    }


    def __init__(self):
        self.temperature = 4000
        self.cooling_level = 50
        self.energy_output = 50
        self.pressure = 1.5
        self.energy_efficiency = 90
        self.structural_integrity = 100
        self.radiation_level = 0.5
        self.stability_factor = 1.0
        self.tunneling_rate = 0.05
        self.containment_field_strength = 100
        self.quantum_coherence = 1.0
        self.quantum_state = "Stable"
        self.status_effects = []


    def update_core(self):
        self.energy_efficiency = clamp(self.energy_efficiency, 0, 100)
        self.containment_field_strength = clamp(self.containment_field_strength, 0, 100)
        self.structural_integrity = clamp(self.structural_integrity, 0, 100)

        cooling_factor = self.cooling_level * random.uniform(0.9, 1.1)
        energy_factor = self.energy_output * random.uniform(0.8, 1.2)

        self.temperature += energy_factor * 0.3 - cooling_factor * 0.5 + random.uniform(-10, 50)
        self.pressure += (self.temperature - 3000) * 0.00005 + random.uniform(-0.1, 0.1)
        self.radiation_level = (self.energy_output / 100) + (self.temperature / 10000)
        self.tunneling_rate += random.uniform(-0.02, 0.02) + (self.temperature / QTEC.TEMPERATURE_THRESHOLDS["critical"]) * 0.02
        self.quantum_state = self.determine_quantum_state()

        if self.temperature > QTEC.TEMPERATURE_THRESHOLDS["danger"]:
            self.containment_field_strength -= (self.temperature - QTEC.TEMPERATURE_THRESHOLDS["danger"]) * 0.001

        self.apply_temperature_penalties()
        self.apply_quantum_penalties()
        self.process_status_effects()

        if random.random() < 0.005:  # normal value is 0.005, set to 0.5 for debugging
            self.random_event()

        if self.temperature > 8000:
            self.energy_efficiency -= 0.2
        elif self.temperature < 3000:
            self.tunneling_rate -= random.uniform(0.02, 0.05)
            self.energy_efficiency -= 0.1

        if self.pressure > 5:
            self.energy_efficiency -= 0.2
        elif self.pressure < 1:
            self.energy_efficiency -= 0.1

        self.quantum_coherence = max(0.0, self.quantum_coherence - (self.energy_output / 1000) * 0.01)

        if self.quantum_coherence < 0.5:
            self.stability_factor -= random.uniform(0.02, 0.05)

        if self.quantum_state == "Chaotic":
            self.tunneling_rate += random.uniform(0.1, 0.3)
            self.energy_efficiency -= 0.3

        if self.containment_field_strength < 50:
            self.structural_integrity -= 0.05
            self.energy_efficiency -= 0.1
        
        self.tunneling_rate = max(0, self.tunneling_rate + random.uniform(-0.02, 0.02))
        self.stability_factor = max(0.1, self.stability_factor - random.uniform(0.001, 0.01))

        self.process_status_effects()


    def determine_quantum_state(self):
        if self.temperature > QTEC.TEMPERATURE_THRESHOLDS["danger"]:
            return "Chaotic"
        elif self.quantum_coherence < 0.5:
            return "Fluctuating"
        else:
            return "Stable"


    def apply_temperature_penalties(self):
        if self.temperature > QTEC.TEMPERATURE_THRESHOLDS["critical"]:
            self.energy_efficiency -= 0.2
        elif self.temperature < 3000:
            self.tunneling_rate -= random.uniform(0.02, 0.05)
            self.energy_efficiency -= 0.1

        if self.pressure > 5:
            self.energy_efficiency -= 0.2
        elif self.pressure < 1:
            self.energy_efficiency -= 0.1


    def apply_quantum_penalties(self):
        self.quantum_coherence = max(0.0, self.quantum_coherence - (self.energy_output / 1000) * 0.01)

        if self.quantum_coherence < 0.5:
            self.stability_factor -= random.uniform(0.02, 0.05)

        if self.quantum_state == "Chaotic":
            self.tunneling_rate += random.uniform(0.1, 0.3)
            self.energy_efficiency -= 0.3

        if self.containment_field_strength < 50:
            self.structural_integrity -= 0.05
            self.energy_efficiency -= 0.1


    def random_event(self):
        events = [
            {"name": "Coolant Impurity", "description": "Efficiency of cooling system reduced due to impurities in the coolant supply.", "effect": lambda: setattr(self, "cooling_level", max(0, self.cooling_level - 1))},
            {"name": "Energy Surge", "description": "Quantum feedback loop overload results in a sudden spike in energy output.", "effect": lambda: self.increase_energy_output()},
            {"name": "Coherence Loss", "description": "Quantum coherence field destabilizes, halting tunneling events.", "effect": lambda: self.reduce_coherence()},
            {"name": "Energy Drain", "description": "Particles tunneled into vacuum states, reducing energy output.", "effect": lambda: setattr(self, "energy_output", self.energy_output - random.randint(10, 30))},
            {"name": "Pressure Spike", "description": "Sudden increase in core pressure, risking structural integrity.", "effect": lambda: setattr(self, "pressure", self.pressure + random.uniform(1.0, 3.0))},
            {"name": "Tunneling Instability", "description": "Quantum states become unstable, affecting stability factor.", "effect": lambda: setattr(self, "stability_factor", max(0, self.stability_factor - 0.05))},
            {"name": "Radiation Surge", "description": "High-energy tunneling events increase radiation levels significantly.", "effect": lambda: setattr(self, "radiation_level", self.radiation_level + random.uniform(0.5, 1.0))},
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
        self.containment_field_strength -= random.uniform(0.5, 2.0)


    def reduce_coherence(self):
        self.stability_factor -= 0.05
        self.quantum_coherence = max(0.1, self.quantum_coherence - 0.2)


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
            f"Quantum Coherence: {self.quantum_coherence:.2f}",
            f"Quantum Stability: {self.stability_factor:.2f}",
            f"Quantum State: {self.quantum_state}",
            f"Pressure: {self.pressure:.2f} bar",
            f"Radiation Level: {self.radiation_level:.2f} mSv/h",
            f"Energy Output: {self.energy_output}%",
            f"Energy Efficiency: {self.energy_efficiency:.2f}%",
            f"Containment Field Strength: {self.containment_field_strength:.2f}%",
            f"Structural Integrity: {self.structural_integrity:.2f}%",
        ]

        if self.temperature >= QTEC.TEMPERATURE_THRESHOLDS["critical"]:
            status.append("WARNING: Core is overheating! Immediate action required!")
            # meltdown begins here
        elif self.temperature >= QTEC.TEMPERATURE_THRESHOLDS["danger"]:
            status.append("WARNING: Core is dangerously hot! Immediate action required!")
        elif self.temperature <= QTEC.TEMPERATURE_THRESHOLDS["stall"]:
            status.append("WARNING: Core is too cold! Immediate action required!")
            # stall begins here

        if self.structural_integrity <= 20:
            status.append("WARNING: Structural Integrity is critically low! Immediate action required!")

        if self.stability_factor < 0.5:
            status.append("WARNING: Quantum stability factor low! Immediate action required!")

        if self.containment_field_strength < 30:
            status.append("WARNING: Containment field critically low! Immediate action required!")


        else:
            status.append("INFO: Core is stable.")

        return status
    

    def get_energy_quota(self):
        quota = [
            "placeholder TW",
            "placeholder%",
        ]

        return quota