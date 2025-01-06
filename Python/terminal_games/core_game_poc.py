import random
import time

style = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "RESET": "\033[0m"
}


class Core:
    def __init__(self):
        self.temperature = 50
        self.cooling_level = 50
        self.energy_output = 50
        self.max_temperature = 100
        self.min_temperature = 0

    def update_core(self):
        self.temperature += (self.energy_output * 0.1) - (self.cooling_level * 0.05)

        if random.random() < 0.1:
            self.random_event()

        self.temperature = max(self.min_temperature, min(self.max_temperature, self.temperature))

    def random_event(self):
        event = random.choice(["Cooling failure!", "Energy surge!", "System overload!"])
        print(style["MAGENTA"] + f"EVENT: {event}" + style["RESET"])
        if event == "Cooling failure!":
            self.cooling_level -= random.randint(5, 15)
        elif event == "Energy surge!":
            self.energy_output += random.randint(5, 15)
        elif event == "System overload!":
            self.temperature += random.randint(5, 15)

    def display_status(self):
        print(style["CYAN"] + f"Core Temperature: {self.temperature:.2f}°C")
        print(f"Cooling Level: {self.cooling_level}%")
        print(f"Energy Output: {self.energy_output}%" + style["RESET"])
        print("-" * 30)

    def check_core_status(self):
        if self.temperature >= self.max_temperature:
            print(style["RED"] + "WARNING: Core Overheating! Immediate action required!" + style["RESET"])
        elif self.temperature <= self.min_temperature:
            print(style["RED"] + "WARNING: Core is too cold! Energy output may be inefficient!" + style["RESET"])
        else:
            print(style["GREEN"] + "Core is stable." + style["RESET"])

def manage_core(core):
    while True:
        core.display_status()
        core.check_core_status()

        print(style["YELLOW"] + "\nChoose an action:")
        print("1. Increase Cooling")
        print("2. Decrease Cooling")
        print("3. Increase Energy Output")
        print("4. Decrease Energy Output")
        print("5. Quit\n" + style["RESET"])

        choice = input("Enter choice (1-5): ")
        print()

        if choice == "1":
            core.cooling_level = min(100, core.cooling_level + 10)
        elif choice == "2":
            core.cooling_level = max(0, core.cooling_level - 10)
        elif choice == "3":
            core.energy_output = min(100, core.energy_output + 10)
        elif choice == "4":
            core.energy_output = max(0, core.energy_output - 10)
        elif choice == "5":
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Try again.")

        core.update_core()
        time.sleep(1)

if __name__ == "__main__":
    core = Core()
    manage_core(core)

# chatgpt generated poc, may or may not expand and add more in the future.... will consider it :)