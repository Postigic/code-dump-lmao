import math
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from pathlib import Path


def benford_distribution():
    return {d: math.log10(1 + 1/d) for d in range(1, 10)}


def extract_first_digits(numbers):
    first_digits = [int(str(abs(num))[0]) for num in numbers if num != 0]
    return first_digits


def calculate_frequencies(digits):
    counts = Counter(digits)
    total = sum(counts.values())
    return {d: counts[d] / total for d in range(1, 10)}


def plot_results(observed, expected):
    digits = range(1, 10)
    plt.bar(digits, [observed.get(d, 0) for d in digits],
            alpha=0.5, label='Observed', color='blue')
    plt.plot(digits, [expected[d] for d in digits],
             marker='o', label='Expected (Benford)', color='red')
    plt.xlabel('First Digit')
    plt.ylabel('Frequency')
    plt.title('Benford\'s Law Analysis')
    plt.legend()
    plt.show()


def main():
    current_dir = Path(__file__).parent

    dataset = pd.read_csv(current_dir / "dataset.csv")
    column_data = dataset["Adult_mortality"]

    first_digits = extract_first_digits(column_data)
    observed = calculate_frequencies(first_digits)
    expected = benford_distribution()

    plot_results(observed, expected)


if __name__ == "__main__":
        main()
