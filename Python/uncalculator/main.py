from terminal_colours import *
from input_handler import *
from domains import REGISTRY
from utils import format

def main():
    print(f"{CYAN}{'-'*40}\nUncalculator\n{'-'*40}{RESET}\n")

    num = prompt_number()
    domain = prompt_domain()
    seed = prompt_seed()

    random.seed(seed)

    expression = REGISTRY[domain].generate(num)

    print(f"\n{GREEN}{'-' * 40}\n{expression} = {format(num)}\n{'-' * 40}{RESET}")

if __name__ == "__main__":
    main()

# kinda empty here huh?
