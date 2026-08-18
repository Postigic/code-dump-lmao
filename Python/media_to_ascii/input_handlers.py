from utils import *

# stole this from an unpublished project i have

def prompt_int(prompt: str, default: int) -> int:
    while True:
        raw = input(f"{prompt} [{default}]: ").strip()

        if raw == "":
            return default
        
        try:
            val = int(raw)
            if val < 1:
                raise ValueError
            return val
        except ValueError:
            print(f"{RED}Please enter a positive integer.{RESET}")

def prompt_float(prompt: str, default: float) -> float:
    while True:
        raw = input(f"{prompt} [{default}]: ").strip()

        if raw == "":
            return default
        
        try:
            val = float(raw)
            if val < 0:
                raise ValueError
            return val
        except ValueError:
            print(f"{RED}Please enter a non-negative number.{RESET}")

def prompt_bool(prompt: str, default: bool) -> bool:
    hint = "Y/n" if default else "y/N"
    
    while True:
        raw = input(f"{prompt} [{hint}]: ").strip().lower()

        if raw == "":
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        
        print(f"{RED}Please enter Y or N.{RESET}")
