import random
from terminal_colours import *
from domains import REGISTRY

def prompt_number() -> float:
    while True:
        num = input("Enter an integer: ").strip()

        try:
            num = int(num)
            if num == 0:
                print(f"{RED}Please enter a non-zero integer.{RESET}")
            else:
                return num
        except ValueError:
            print(f"{RED}Invalid input. Please enter an integer.{RESET}")

def prompt_domain() -> str:
    names = list(REGISTRY.keys())

    print("\nAvailable domains:")
    for i, name in enumerate(names, 1):
        print(f"    {i}. {name}")

    while True:
        entry = input("Select a domain: ").strip().lower()

        try:
            idx = int(entry) - 1

            if 0 <= idx < len(names):
                return names[idx]
            else:
                print(f"{RED}Invalid selection.{RESET}")
        except ValueError:
            # allow selection by name implicitly for convenience
            if entry in names:
                return entry
            else:
                print(f"{RED}Unrecognised input.{RESET}")

# you need my what now?
def prompt_seed() -> int:
    seed = input("\nEnter a seed (leave blank for random): ").strip()

    if seed == "":
        seed = random.randint(0, 2**32 - 1)
        print(f"Using seed {seed}")
    else:
        try:
            seed = int(seed)
        except ValueError:
            print(f"{RED}Invalid seed, generating random seed.{RESET}")
            seed = random.randint(0, 2**32 - 1)
            print(f"Using seed {seed}")

    return seed
