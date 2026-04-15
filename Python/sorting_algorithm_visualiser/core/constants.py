import random
from core.algorithms.bubble_sort import bubble_sort, optimised_bubble_sort
from core.algorithms.insertion_sort import insertion_sort, binary_insertion_sort
from core.algorithms.selection_sort import selection_sort
from core.algorithms.merge_sort import merge_sort, bottom_up_merge_sort
from core.algorithms.quick_sort import quick_sort, randomised_quick_sort, median_of_three_quick_sort, dual_pivot_quick_sort, three_way_quick_sort
from core.algorithms.bogo_sort import bogo_sort
from core.algorithms.stalin_sort import stalin_sort
from core.algorithms.thanos_sort import thanos_sort
from core.algorithms.miracle_sort import miracle_sort
from core.algorithms.heap_sort import heap_sort
from core.algorithms.counting_sort import counting_sort, stable_counting_sort
from core.algorithms.lsd_radix_sort import lsd_radix_sort
from core.algorithms.msd_radix_sort import msd_radix_sort
from core.algorithms.cocktail_sort import cocktail_sort, optimised_cocktail_sort
from core.algorithms.shell_sort import shell_sort
from core.algorithms.cycle_sort import cycle_sort
from core.algorithms.pancake_sort import pancake_sort
from core.algorithms.gnome_sort import gnome_sort
from core.algorithms.timsort import timsort
from core.algorithms.stooge_sort import stooge_sort
from core.algorithms.slow_sort import slow_sort
from core.algorithms.comb_sort import comb_sort, comb_sort_11
from core.algorithms.bogobogo_sort import bogobogo_sort
from core.algorithms.intelligent_design_sort import intelligent_design_sort
from core.algorithms.bozo_sort import bozo_sort
from core.algorithms.quantum_bogo_sort import quantum_bogo_sort
from core.algorithms.tournament_sort import tournament_sort
from core.algorithms.introspective_sort import introspective_sort

def _nearly_sorted(n):
    base = list(range(1, n+1))

    for _ in range(max(1, n // 10)):
        i, j = random.sample(range(n), 2)
        base[i], base[j] = base[j], base[i]
    
    return base

def _few_unique(n):
    buckets = max(2, n // 8)
    values = random.sample(range(1, n + 1), buckets)
    
    return [random.choice(values) for _ in range(n)]

def _mountain(n):
    half = n // 2
    up = [int((i / half) * n) + 1 for i in range(half)]
    down = up[::-1]
    
    return (up + down)[:n]

def _single_swap(n):
    base = list(range(1, n+1))
    i, j = random.sample(range(n), 2)
    base[i], base[j] = base[j], base[i]
    
    return base

def _median_of_three_killer(n):
    # McIlroy's algorithm (pretty cooolll i think?)
    arr = list(range(1, n + 1))
    candidate = [0] * n
    k = n // 2

    for i in range(n):
        if i % 2 == 0:
            candidate[i] = i
        else:
            candidate[i] = k + (i // 2)

    for i in range(0, n - 1, 2):
        arr[candidate[i]], arr[candidate[i + 1]] = arr[candidate[i + 1]], arr[candidate[i]]

    return arr

def _sawtooth(n):
    teeth = max(2, n // 8)
    return [((i % teeth) + 1) * (n // teeth) for i in range(n)]

def _pipe_organ(n):
    half = n // 2
    down = [int(((half - i) / half) * n) + 1 for i in range(half)]
    up = [int(((i) / half) * n) + 1 for i in range(half)]
    
    return (down + up)[:n]

def _alternating(n):
    lo, hi = 1, n
    arr = []
    
    for i in range(n):
        if i % 2 == 0:
            arr.append(hi)
            hi -= 1
        else:
            arr.append(lo)
            lo += 1
    
    return arr

def _sine_wave(n):
    import math

    return [int((math.sin(i / n * 2 * math.pi) + 1) / 2 * (n - 1)) + 1 for i in range(n)]

def _shifted(n):
    split = n // 3
    base = list(range(1, n + 1))

    return base[split:] + base[:split]

SIZES = ["4", "8", "16", "32", "64", "96", "128", "256", "512"]

MAX_SIZE = int(SIZES[-1])

DATASETS = [
    {"name": "Random", "fn": lambda n: random.sample(range(1, n+1), n)},
    {"name": "Reversed", "fn": lambda n: list(range(n, 0, -1))},
    {"name": "Sorted", "fn": lambda n: list(range(1, n+1))},
    {"name": "Nearly Sorted", "fn": _nearly_sorted},
    {"name": "Few Unique", "fn": _few_unique},
    {"name": "Mountain", "fn": _mountain},
    {"name": "Single Swap", "fn": _single_swap},
    {"name": "Median of Three Killer", "fn": _median_of_three_killer},
    {"name": "Sawtooth", "fn": _sawtooth},
    {"name": "Pipe Organ", "fn": _pipe_organ},
    {"name": "Alternating", "fn": _alternating},
    {"name": "Sine Wave", "fn": _sine_wave},
    {"name": "Shifted", "fn": _shifted}
]

DATASETS.sort(key=lambda d: d["name"])

DATASET_MAP  = {d["name"]: d["fn"] for d in DATASETS}
DATASET_NAMES = [d["name"] for d in DATASETS]

# what the hell
ALGOS = [
    {
        "name": "Bogo Sort",
        "fn": bogo_sort,
        "time_worst": "Unbounded",
        "time_avg": "O(n * n!)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Randomly shuffles the array until it happens to be sorted. Completely unusable in practice: even a 15-element array has 15! ~= 1.3 trillion possible orderings to stumble through. Exists purely as a joke and a reference point for how bad a sorting algorithm can theoretically be."
    },
    {
        "name": "Bubble Sort",
        "fn": bubble_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n²)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Repeatedly steps through the array comparing and swapping adjacent elements. One of the simplest sorting algorithms to understand and implement, but one of the least efficient; always O(n²) comparisons with no early exit. Outperformed by insertion sort in almost every scenario, even on small arrays. Used almost exclusively for teaching purposes."
    },
    {
        "name": "Insertion Sort",
        "fn": insertion_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Builds a sorted region one element at a time by taking each new element and shifting it leftward into its correct position. Excellent on small arrays and nearly sorted data, where it approaches O(n) and outperforms more complex algorithms. Used as a subroutine in Timsort and Shell sort precisely for this reason. Degrades to O(n²) on large random or reverse-sorted input."
    },
    {
        "name": "Binary Insertion Sort",
        "fn": binary_insertion_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n log n)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Insertion sort that uses binary search to find the correct position for each element rather than scanning linearly. Reduces comparisons from O(n²) to O(n log n), but element shifts remain O(n²) since each insertion still requires moving everything in between. A practical improvement when comparisons are expensive relative to moves: for example when comparing large structs by a key. Outperformed by Timsort on nearly sorted data but useful in constrained contexts."
    },
    {
        "name": "Merge Sort",
        "fn": merge_sort,
        "time_worst": "O(n log n)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(n)",
        "stable": True,
        "inplace": False,
        "desc": "Recursively splits the array in half, sorts each half, then merges them back together. Guarantees O(n log n) in all cases and is stable, making it the preferred choice when predictability and order preservation matter. Particularly well suited to linked lists and external sorting where random access is expensive. The main drawback is O(n) auxiliary space."
    },
    {
        "name": "Bottom-up Merge Sort",
        "fn": bottom_up_merge_sort,
        "time_worst": "O(n log n)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(n)",
        "stable": True,
        "inplace": False,
        "desc": "An iterative merge sort that starts with runs of size 1 and repeatedly merges adjacent pairs, doubling the run size each pass until the array is sorted. Avoids recursion entirely, eliminating call stack overhead and making it straightforward to implement without worrying about stack depth. The merge phase of Timsort works on the same principle. Produces the same result as top-down merge sort with identical complexity but a visually distinct pattern; runs doubling in size left to right rather than a recursive halving."
    },
    {
        "name": "Miracle Sort",
        "fn": miracle_sort,
        "time_worst": "Unbounded",
        "time_avg": "Unbounded",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": None,
        "inplace": True,
        "desc": "Checks if the array is sorted and if not, simply waits. Relies on cosmic radiation flipping bits in memory until they happen to form a sorted array. Will never terminate on any real hardware. The joke is that it requires no code beyond the check; the sorting is outsourced to the universe."
    },
    {
        "name": "Selection Sort",
        "fn": selection_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n²)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Repeatedly scans the unsorted portion for the minimum element and swaps it into place. Always O(n²) with no best case improvement possible, making it strictly worse than insertion sort for most purposes. Its one genuine advantage is minimising writes; it performs at most n-1 swaps total, which can matter on flash storage or other write-sensitive memory."
    },
    {
        "name": "Stalin Sort",
        "fn": stalin_sort,
        "time_worst": "O(n)",
        "time_avg": "O(n)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Removes any out-of-order element rather than moving it, leaving a sorted subsequence of the original. O(n) in a single pass. Not a real sorting algorithm since it destroys data, but technically produces a sorted result. The name and premise are a dark joke about eliminating problems rather than solving them."
    },
    {
        "name": "Thanos Sort",
        "fn": thanos_sort,
        "time_worst": "O(n log n)",
        "time_avg": "O(n log n)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": None,
        "inplace": True,
        "desc": "Repeatedly deletes a random half of the array until what remains happens to be sorted. Guaranteed to terminate as at most O(log n) halvings the array shrinks to a single element, which is trivially sorted. Each halving requires an O(n) sorted check, giving O(n log n) total. Like Stalin sort, it produces a sorted result by destroying data rather than rearranging it. A joke on Thanos's approach to overpopulation."
    },
    {
        "name": "Quick Sort",
        "fn": quick_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "Selects a pivot, partitions the array into elements less than and greater than the pivot, then recurses on each side. Very fast in practice due to excellent cache locality and the most widely used sorting algorithm in standard libraries. This implementation uses the last element as the pivot, which hits O(n²) on already sorted input; a known weakness of naive pivot selection."
    },
    {
        "name": "Randomised Quick Sort",
        "fn": randomised_quick_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "Quick sort with a randomly chosen pivot rather than always using the last element. The randomisation makes the O(n²) worst case statistically negligible; no input pattern can reliably trigger it. Retains all the cache efficiency of standard quick sort while eliminating its predictable failure mode. A simple but significant improvement over the naive version."
    },
    {
        "name": "Median-of-Three Quick Sort",
        "fn": median_of_three_quick_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "Quick sort that selects its pivot as the median of the first, middle, and last elements. Eliminates the worst case on already sorted or reverse-sorted input without any randomness, and tends to produce more balanced partitions than random pivot selection. The approach used by most real implementations including GCC's introsort. Slightly more cache-friendly than randomised quick sort since it reads three fixed positions rather than a random one."
    },
    {
        "name": "Heap Sort",
        "fn": heap_sort,
        "time_worst": "O(n log n)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Builds a max-heap from the array, then repeatedly extracts the maximum into its final sorted position. Guarantees O(n log n) in all cases with O(1) auxiliary space; theoretically optimal on both counts. In practice it is slower than quick sort due to poor cache locality from jumping around the heap. Useful when guaranteed performance and minimal memory use are both required."
    },
    {
        "name": "Counting Sort",
        "fn": counting_sort,
        "time_worst": "O(n + k)",
        "time_avg": "O(n + k)",
        "time_best": "O(n + k)",
        "aux": "O(k)",
        "stable": False,
        "inplace": False,
        "desc": "Counts occurrences of each value and reconstructs the sorted array by writing each value back the appropriate number of times. Only practical when the value range k is bounded and known in advance. Non-comparison based, so it sidesteps the O(n log n) lower bound entirely and runs in O(n + k). This implementation uses value reconstruction rather than the stable prefix-sum pattern, so it does not preserve the relative order of equal elements."
    },
    {
        "name": "Stable Counting Sort",
        "fn": stable_counting_sort,
        "time_worst": "O(n + k)",
        "time_avg": "O(n + k)",
        "time_best": "O(n + k)",
        "aux": "O(n + k)",
        "stable": True,
        "inplace": False,
        "desc": "Counting sort using the prefix-sum pattern; counts are accumulated into cumulative totals, then elements are placed into an output array by iterating the input in reverse. The reverse iteration is what preserves relative order of equal elements, making it stable. This is the canonical implementation used as the inner sort in LSD radix sort, where stability across passes is required for correctness."
    },
    {
        "name": "LSD Radix Sort",
        "fn": lsd_radix_sort,
        "time_worst": "O(d(n + k))",
        "time_avg": "O(d(n + k))",
        "time_best": "O(d(n + k))",
        "aux": "O(n + k)",
        "stable": True,
        "inplace": False,
        "desc": "Sorts integers digit by digit from least to most significant, using a stable sort at each pass. Non-comparison based and very fast for fixed-length integers or strings with a bounded digit count. Less cache-friendly than comparison sorts and requires O(n + k) auxiliary space per pass. Preferred over MSD for uniform-length keys."
    },
    {
        "name": "MSD Radix Sort",
        "fn": msd_radix_sort,
        "time_worst": "O(d(n + k))",
        "time_avg": "O(d(n + k))",
        "time_best": "O(d(n + k))",
        "aux": "O(n + k)",
        "stable": True,
        "inplace": False,
        "desc": "Sorts digit by digit from most to least significant, recursing into each bucket. Single-element buckets are skipped. Can be faster than LSD for variable-length keys since it can short-circuit on buckets that are already uniform. More complex to implement correctly than LSD. Same asymptotic complexity but different practical characteristics."
    },
    {
        "name": "Cocktail Sort",
        "fn": cocktail_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n²)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "A bidirectional variant of bubble sort that alternates between forward and backward passes. The backward pass handles turtles; small elements near the end of the array that take many passes to bubble leftward in standard bubble sort. Slightly better in practice than bubble sort but same O(n²) worst case, and still outperformed by insertion sort."
    },
    {
        "name": "Optimised Bubble Sort",
        "fn": optimised_bubble_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Bubble sort with an early exit when a full pass completes with no swaps, indicating the array is already sorted. Gives O(n) best case on already-sorted input and performs well on nearly sorted data. Still degrades to O(n²) on random or reverse-sorted arrays. The early exit is the minimum optimisation needed to make bubble sort not entirely useless."
    },
    {
        "name": "Optimised Cocktail Sort",
        "fn": optimised_cocktail_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Cocktail sort with the same early-exit optimisation as optimised bubble sort; terminates as soon as a full bidirectional pass produces no swaps. O(n) on sorted input. Handles nearly sorted data better than optimised bubble sort due to the bidirectional passes reducing turtle movement. Still O(n²) in the general case."
    },
    {
        "name": "Shell Sort",
        "fn": shell_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n log² n)",
        "time_best": "O(n log n)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Insertion sort generalised to compare elements at a shrinking gap distance, performing a final gap-1 pass to finish. The large initial gaps move elements close to their final positions quickly, making the last insertion sort pass cheap. This implementation uses simple halving for the gap sequence, giving O(n²) worst case; better sequences like Ciura's improve this significantly in practice. A good middle ground that is simple to implement and faster than pure insertion sort on larger inputs."
    },
    {
        "name": "Cycle Sort",
        "fn": cycle_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n²)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Based on the cycle structure of permutations; each element is moved directly to its final position in a cycle, then the next cycle begins. Minimises array writes to at most n-1, making it uniquely suited to memory where writes are expensive or have limited endurance such as flash storage. Despite minimising writes, it is slow in practice due to O(n²) comparisons. Rarely seen outside of specialised embedded or hardware contexts."
    },
    {
        "name": "Pancake Sort",
        "fn": pancake_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Sorts using only prefix reversals, flipping the first k elements of the array. Each step finds the current maximum, flips it to the front, then flips it to its final position. A mathematical curiosity with roots in combinatorics and the burnt pancake problem. No practical sorting application; primarily studied for the minimum number of flips required to sort a sequence."
    },
    {
        "name": "Gnome Sort",
        "fn": gnome_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n²)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Walks forward through the array and on finding an out-of-order element swaps it backward one position at a time until it is in the right place, then resumes walking forward. Functionally identical to insertion sort but arrives at the same result through a different mechanical process. Simpler to implement than insertion sort but slower in practice due to the single-step backward movement. Named after a Dutch garden gnome sorting flower pots by size."
    },
    {
        "name": "Timsort",
        "fn": timsort,
        "time_worst": "O(n log n)",
        "time_avg": "O(n log n)",
        "time_best": "O(n)",
        "aux": "O(n)",
        "stable": True,
        "inplace": False,
        "desc": "A hybrid of insertion sort and merge sort developed by Tim Peters, used as the built-in sort in Python and for objects in Java (Java uses dual-pivot quicksort for primitive arrays). Detects and exploits existing runs of sorted or reverse-sorted data in the input, sorting small runs with insertion sort and merging them with a merge sort variant. Achieves O(n) on already sorted or nearly sorted input and consistently outperforms pure merge sort on real-world data. The gold standard for general-purpose stable sorting of in-memory data."
    },
    {
        "name": "Stooge Sort",
        "fn": stooge_sort,
        "time_worst": "O(n^(log 3 / log 1.5))",
        "time_avg": "O(n^(log 3 / log 1.5))",
        "time_best": "O(n^(log 3 / log 1.5))",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "Recursively sorts the first two-thirds of the array, then the last two-thirds, then the first two-thirds again. Named after the Three Stooges. The three overlapping recursive calls are provably inefficient at approximately O(n^2.71), making it slower than bubble sort and every other quadratic algorithm. Exists as a theoretical example of a correctly sorting algorithm that is nonetheless worse than naive approaches."
    },
    {
        "name": "Slow Sort",
        "fn": slow_sort,
        "time_worst": "O(n^(log n / 2))",
        "time_avg": "O(n^(log n / 2))",
        "time_best": "O(n^(log n / 2))",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "Based on the multiply-and-surrender paradigm, deliberately the opposite of divide and conquer. Recursively sorts both halves, promotes the maximum to the end, then recursively sorts everything except the last element, including re-sorting already partially sorted regions. The redundant overlap makes it superpolynomial. Designed specifically as a joke to be provably non-optimal while still being a correct sorting algorithm."
    },
    {
        "name": "Comb Sort",
        "fn": comb_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n² / 2^p)",
        "time_best": "O(n log n)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Bubble sort generalised to compare elements at a gap distance, shrinking the gap by a factor of 1.3 each pass until it reaches 1 and finishes like a regular bubble sort. The large initial gaps eliminate turtles; small elements near the end that make bubble sort slow, early in the process. A practical improvement over bubble sort for the same reason shell sort improves on insertion sort."
    },
    {
        "name": "Comb Sort 11",
        "fn": comb_sort_11,
        "time_worst": "O(n²)",
        "time_avg": "O(n² / 2^p)",
        "time_best": "O(n log n)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Comb sort with an empirical adjustment that skips gap values of 9 and 10, jumping straight to 11. These gap sizes are known to leave turtles unresolved and perform poorly in practice. The skip improves average performance measurably. The name refers to 11 being the smallest gap size this variant will actually use."
    },
    {
        "name": "Intelligent Design Sort",
        "fn": intelligent_design_sort,
        "time_worst": "O(1)",
        "time_avg": "O(1)",
        "time_best": "O(1)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Asserts that the array is already sorted, on the grounds that the probability of any particular arrangement arising by chance is 1/n! which for large n is so vanishingly small that it cannot have occurred randomly. The current order must therefore be the result of intentional design by an omniscient being who, by definition, chose optimally. Returns immediately. Any attempt to re-sort the output is theologically incoherent. The implementation is a no-op; the proof of correctness is left as an exercise in faith."
    },
    {
        "name": "Bogobogo Sort",
        "fn": bogobogo_sort,
        "time_worst": "Unbounded",
        "time_avg": "O((n!^n))",
        "time_best": "O(n)",
        "aux": "O(n)",
        "stable": False,
        "inplace": False,
        "desc": "A recursive descent into madness built on bogosort. To sort k elements, it randomly shuffles them, recursively bogobogosorts the first k-1, then checks if all k are now in order, restarting the whole process if not. Each level depends on the level below completing first, multiplying an already incomprehensible runtime at every step. Even small arrays are effectively impossible to sort in any reasonable timeframe. Not a joke about bad sorting; a joke about what happens when you recurse a joke."
    },
    {
        "name": "Bozo Sort",
        "fn": bozo_sort,
        "time_worst": "Unbounded",
        "time_avg": "O(n * n!)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": False,
        "inplace": True,
        "desc": "Picks two random positions and swaps them, then checks if the array is sorted. Repeats until it is. Often conflated with bogosort but mechanically distinct. Bogosort reshuffles the entire array each pass, bozo sort disturbs only two elements. In practice this makes it neither better nor worse in any meaningful sense; it still averages O(n * n!) and can technically run forever. The name is the joke: it is, in fact, a bozo's approach to sorting."
    },
    {
        "name": "3-Way Quick Sort",
        "fn": three_way_quick_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n log n)",
        "time_best": "O(n)",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "Quick sort that partitions into three regions: less than, equal to, and greater than the pivot using Dijkstra's Dutch National Flag algorithm. The equal region is settled in a single pass and never recursed on again, making it optimal on inputs with many duplicate keys where standard quick sort degrades toward O(n²). Best case O(n) occurs when all elements are equal."
    },
    {
        "name": "Dual-Pivot Quick Sort",
        "fn": dual_pivot_quick_sort,
        "time_worst": "O(n²)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "Quick sort that selects two pivots and partitions into three regions: less than the first pivot, between the two pivots, and greater than the second pivot. Introduced by Yaroslavskiy and used in Java's Arrays.sort for primitive types since Java 7. Performs fewer comparisons than single-pivot quick sort in practice and has better cache behaviour than 3-way partitioning on inputs without many duplicates. The two-pivot approach means the middle partition, typically the largest, is handled in a single recursive call."
    },
    {
        "name": "Quantum Bogo Sort",
        "fn": quantum_bogo_sort,
        "time_worst": "O(n)",
        "time_avg": "O(n)",
        "time_best": "O(n)",
        "aux": "O(1)",
        "stable": True,
        "inplace": True,
        "desc": "Leverages the many-worlds interpretation of quantum mechanics. Checks if the array is sorted; if not, the universe is destroyed. By the anthropic principle, the only universe in which an observer can exist is one where the array is already sorted, guaranteeing an O(n) check with no comparisons wasted on sorting. Requires a quantum computer capable of collapsing universes. Performance figures assume successful universal survival."
    },
    {
        "name": "Tournament Sort",
        "fn": tournament_sort,
        "time_worst": "O(n log n)",
        "time_avg": "O(n log n)",
        "time_best": "O(n log n)",
        "aux": "O(n)",
        "stable": False,
        "inplace": False,
        "desc": "Simulates an elimination tournament. Builds a winner tree in O(n) by having all elements compete pairwise from the leaves up. The root holds the overall minimum. Each extraction reads the root, retires that leaf by setting it to infinity, then replays only the single root-to-leaf path in O(log n) to find the next minimum. Repeating this n times yields a sorted sequence. The explicit winner-index tree makes the O(log n) replay intuitive: only nodes on the winning path can change."
    },
    {
        "name": "Introspective Sort",
        "fn": introspective_sort,
        "time_worst": "O(n log n)",
        "time_avg": "O(n log n)",
        "time_best": "O(n)",
        "aux": "O(log n)",
        "stable": False,
        "inplace": True,
        "desc": "A hybrid of quicksort, heapsort, and insertion sort. Starts with quicksort for its practical speed, but tracks recursion depth: if it exceeds 2 * floor(log_2(n)), indicating bad pivot choices, it switches to heapsort to guarantee O(n log n) worst case. Small subarrays of 16 or fewer elements fall through to insertion sort, which has low overhead at small sizes. The result is quicksort's average-case performance with heapsort's worst-case guarantee. Used in most production sort implementations including C++ std::sort."
    }
]

ALGOS.sort(key=lambda a: a["name"])

ALGO_MAP = {algo["name"]: algo["fn"] for algo in ALGOS}
ALGO_INFO = {algo["name"]: algo for algo in ALGOS}
ALGO_NAMES = [algo["name"] for algo in ALGOS]
