from utilities import *

def increase_cooling(core, arg):
    if core.cooling_level + arg > 100:
        core.cooling_level = 100
        return "[WARN]: Cooling level cannot exceed 100%, defaulting to max.", ORANGE
    else:
        core.cooling_level += arg
        return f"[LOGS] Cooling level increased by {arg}%", WHITE


def decrease_cooling(core, arg):
    if core.cooling_level - arg < 0:
        core.cooling_level = 0
        return "[WARN]: Cooling level cannot be negative, defaulting to min.", ORANGE
    else:
        core.cooling_level -= arg
        return f"[LOGS] Cooling level decreased by {arg}%", WHITE


def increase_energy(core, arg):
    if core.energy_output + arg > 100:
        core.energy_output = 100
        return "[WARN]: Energy output cannot exceed 100%, defaulting to max.", ORANGE
    else:
        core.energy_output += arg
        return f"[LOGS] Energy output increased by {arg}%", WHITE
    

def decrease_energy(core, arg):
    if core.energy_output - arg < 0:
        core.energy_output = 0
        return "[WARN]: Energy output cannot be negative, defaulting to min.", ORANGE
    else:
        core.energy_output -= arg
        return f"[LOGS] Energy output decreased by {arg}%", WHITE


commands = {
    "inc_cooling": {
        "display": "inc_cooling [int]",
        "description": "Increase cooling",
        "handler": increase_cooling
    },
    "dec_cooling": {
        "display": "dec_cooling [int]",
        "description": "Decrease cooling",
        "handler": decrease_cooling
    },
    "inc_energy": {
        "display": "inc_energy [int]",
        "description": "Increase energy output",
        "handler": increase_energy
    },
    "dec_energy": {
        "display": "dec_energy [int]",
        "description": "Decrease energy output",
        "handler": decrease_energy
    },
    "clear": {
        "display": "clear",
        "description": "Clear the terminal",
        "handler": lambda core, _: "clear"
    },
    "exit": {
        "display": "exit",
        "description": "Exit the control interface",
        "handler": lambda core, _: "exit"
    },
}