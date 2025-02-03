import time


STYLE = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "RESET": "\033[0m"
}


def test_sort(func):
    test_cases = [
        ([1, 6, 4, 3, 7, 9, 10, 2, 4, 6, 5], [1, 2, 3, 4, 4, 5, 6, 6, 7, 9, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),
        ([], []),
        ([42], [42]),
        ([-3, -1, -7, -5, -2], [-7, -5, -3, -2, -1]),
        ([3, -1, 7, -5, 2], [-5, -1, 2, 3, 7]),
        ([0, 5, 3, 0, 2, -1], [-1, 0, 0, 2, 3, 5]),
        ([99999, 123456, -123456, 0], [-123456, 0, 99999, 123456]),
        (
            [42, -3, 17, 88, 5, 73, 29, -15, 91, 60, 
            34, 7, -8, 55, 21, 39, 99, -22, 10, 84, 
            -5, 66, 31, -1, 50, 13, 77, 3, -11, 95],
            [-22, -15, -11, -8, -5, -3, -1, 3, 5, 7, 
            10, 13, 17, 21, 29, 31, 34, 39, 42, 50, 
            55, 60, 66, 73, 77, 84, 88, 91, 95, 99]
        ),
    ]

    print(STYLE["YELLOW"] + f"Testing \"{func.__name__.replace('_', ' ')}\"...\n" + STYLE["RESET"])

    for idx, (input_list, expected) in enumerate(test_cases, start=1):
        start_time = time.perf_counter_ns()
        result = func(input_list[:])
        end_time = time.perf_counter_ns()

        time_taken = end_time - start_time
        status = STYLE["GREEN"] + "Pass ✅" if result == expected else STYLE["RED"] + f"Fail ❌ (Got {result}, Expected {expected})"

        print(f"Test Case {idx}: {input_list}")
        print(f"{status}" + STYLE["RESET"])
        print(STYLE["CYAN"] + f"Time taken: {time_taken} nanoseconds\n" + STYLE["RESET"])

        
# thank you chatgpt.... i mean what i totally wrote this all myself huh what do you mean i'm lying