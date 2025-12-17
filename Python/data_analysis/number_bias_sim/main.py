import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# help me what is this i don't know what i'm doing
BIAS_GROUPS = [
    ("lucky", 0.06, [3, 7, 8]),
    ("memes", 0.07, [21, 42, 67, 69, 13, 100]),
    ("multiples_of_5", 0.10, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]),
    ("middle_band", 0.18, list(range(35, 66))),
    ("predictable_random", 0.12, [37, 41, 43, 47, 53, 59, 61, 38, 48, 57, 63, 79, 86, 6, 8, 9, 17, 73, 97]),
    ("edge_aversion", 0.06, list(range(2, 10)) + list(range(91, 99))),
    ("symmetry", 0.05, [11, 22, 33, 44, 55, 66, 77, 88, 99]),
    ("times_table", 0.06, [12, 24, 36, 48, 60, 72, 84]),
    ("dates", 0.15, list(range(1, 32))),
    ("even_numbers", 0.04, list(range(2, 101, 2))),
    ("sports", 0.03, [23, 24, 34, 99, 13, 7, 10, 3, 4, 5, 6, 1, 25, 22, 8, 12, 77, 30, 11, 14, 9]),
    ("ages", 0.02, [16, 18, 21, 25, 30]),
    ("prime_bias", 0.08, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
    ("avoid_obvious", 0.04, [n for n in range(1, 101) if n not in {1, 2, 3, 10, 20, 25, 50, 75, 100}]),
    ("last_digit_bias", 0.06, [n for n in range(1,101) if str(n)[-1] in "3570"]),
    ("digit_sum_bias", 0.03, [n for n in range(1,101) if sum(map(int,str(n))) in (5,6,7,9)]),
    ("cool_sounding", 0.02, [7, 12, 24, 36, 64, 72, 84]),
    ("time_numbers", 0.05, [7, 12, 24, 15, 30, 45, 60]),
    ("true_random", 0.12, None)
]

def human_biased_number() -> int:
    total_weight = sum(weight for _, weight, _ in BIAS_GROUPS)
    r = random.random() * total_weight
    cumulative = 0

    # no clue what this does lmao don't ask me
    for name, weight, pool in BIAS_GROUPS:
        cumulative += weight

        if r < cumulative:
            if pool is None:
                return random.randint(1, 100)
            
            return random.choice(pool)

def simulate_trial() -> tuple[list[int], list[int], float]:
    numbers = [human_biased_number() for _ in range(100)]
    mean = sum(numbers) / 100
    safe_numbers = [n for n in numbers if abs(n - mean) >= 5]

    return numbers, safe_numbers, mean

def run_simulation(trials: int = 10000) -> tuple[Counter, Counter, list]:
    select_count = Counter()
    safe_count = Counter()
    means = []

    for _ in range(trials):
        numbers, safe_numbers, trial_mean = simulate_trial()
        select_count.update(numbers)
        safe_count.update(safe_numbers)
        means.append(trial_mean)

    return select_count, safe_count, means

if __name__ == "__main__":
    trials = 10000
    select_count, safe_count, means = run_simulation(trials)

    # what do the numbers mean mason?
    print("Number\tSelected\tSafe\tP(Safe|Selected)")
    for n in range(1, 101):
        selected = select_count[n]
        safe = safe_count[n]
        prob_safe = safe / selected if selected else 0
        print(f"{n}\t{selected}\t{safe}\t{prob_safe:.4f}")

    print("\nTotal Selected\tTotal Safe")
    print(sum(select_count.values()), sum(safe_count.values()))

    numbers = list(range(1, 101))
    select_freq = [select_count[n] for n in numbers]
    safe_freq = [safe_count[n] for n in numbers]

    # honestly the chances that a number is selected 0 times is astronomically low (i think) but just in case y'know?
    prob_safe = [safe_count[n] / select_count[n] if select_count[n] else 0 for n in numbers]

    fig, axes = plt.subplots(3, 1, figsize=(10, 15))

    window = 5
    select_ma = np.convolve(select_freq, np.ones(window)/window, mode="same")
    safe_ma = np.convolve(safe_freq, np.ones(window)/window, mode="same")

    axes[0].bar(numbers, select_freq, color="skyblue", label="Selected")
    axes[0].bar(numbers, safe_freq, color="lightcoral", label="Safe (≥5 from Mean)")
    axes[0].plot(numbers, select_ma, color="blue", linewidth=2, label="Selected MA (5)")
    axes[0].plot(numbers, safe_ma, color="red", linewidth=2, label="Safe MA (5)")
    axes[0].set_title("Selection vs Safe Frequency")
    axes[0].set_ylabel("Count")
    axes[0].set_xticks(range(0, 101, 5))
    axes[0].legend()
    axes[0].grid(axis="y", linestyle="--", alpha=0.4)

    axes[1].plot(numbers, prob_safe, color="green")
    axes[1].set_title("Probability of Being Safe Given Selection")
    axes[1].set_xticks(range(0, 101, 5))
    axes[1].set_ylabel("P(safe | selected)")
    axes[1].set_ylim(0, 1)
    axes[1].grid(axis="y", linestyle="--", alpha=0.4)

    axes[2].hist(means, bins=40, color="slategray")
    axes[2].set_title("Distribution of Trial Means")
    axes[2].set_ylabel("Frequency")
    axes[2].set_xticks(range(0, 101, 5))
    axes[2].grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()
