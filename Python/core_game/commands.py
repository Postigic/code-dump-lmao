import random
import sys
from utilities import *
from logger import clear_logs


def validate_int(arg):
    if isinstance(arg, int):
        return arg
    raise TypeError(f"Expected an integer, but got {type(arg).__name__}.")


def adjust_core_property(core, property_name, adjustment, max_value=100, min_value=0):
    current_value = getattr(core, property_name, 0)
    new_value = current_value + adjustment
    clamped_value = clamp(new_value, min_value, max_value)

    setattr(core, property_name, clamped_value)

    if new_value > max_value:
        return f"[WARN]: {property_name.replace('_', ' ').title()} cannot exceed {max_value}%, defaulting to max.", ORANGE
    elif new_value < min_value:
        return f"[WARN]: {property_name.replace('_', ' ').title()} cannot be less than {min_value}%, defaulting to min.", ORANGE
    else:
        return f"[LOGS] {property_name.replace('_', ' ').title()} adjusted by {adjustment}%.", WHITE


def vent_pressure(core, _):
    vent_amount = random.uniform(0.5, 1.5)
    core.pressure -= vent_amount
    return f"[LOGS] Vented {vent_amount:.2f} bar of pressure", WHITE


commands = {
    "inc_cooling": {
        "display": "inc_cooling [int]",
        "description": "Increase cooling by specified amount",
        "handler": lambda core, arg: adjust_core_property(core, "cooling_level", validate_int(arg))
    },
    "dec_cooling": {
        "display": "dec_cooling [int]",
        "description": "Decrease cooling by specified amount",
        "handler": lambda core, arg: adjust_core_property(core, "cooling_level", -validate_int(arg))
    },
    "inc_energy": {
        "display": "inc_energy [int]",
        "description": "Increase energy output by specified amount",
        "handler": lambda core, arg: adjust_core_property(core, "energy_output", validate_int(arg))
    },
    "dec_energy": {
        "display": "dec_energy [int]",
        "description": "Decrease energy output by specified amount",
        "handler": lambda core, arg: adjust_core_property(core, "energy_output", validate_int(-arg))
    },
    "vent_pressure": {
        "display": "vent_pressure",
        "description": "Vents pressure from the core",
        "handler": vent_pressure
    },
    "help": {
        "display": "help [str]",
        "description": "Briefly explains a status term",
        "handler": lambda core, _: ("[INFO] Help placeholder.", WHITE)
    },
    "clear": {
        "display": "clear",
        "description": "Clears the terminal",
        "handler": lambda core, _: ("[INFO] Logs cleared.", WHITE) if not clear_logs() else None
    },
    "exit": {
        "display": "exit",
        "description": "Exits the control interface",
        "handler": lambda core, _: (pygame.quit(), sys.exit(), "")[2]
    },
}
