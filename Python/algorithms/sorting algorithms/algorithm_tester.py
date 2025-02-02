def test_sort(func):
    test_cases = [
        # Test case 1: Typical case with duplicates and random order
        ([1, 6, 4, 3, 7, 9, 10, 2, 4, 6, 5], [1, 2, 3, 4, 4, 5, 6, 6, 7, 9, 10]),

        # Test case 2: Already sorted list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),

        # Test case 3: Reverse sorted list
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),

        # Test case 4: List with all identical elements
        ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),

        # Test case 5: Empty list
        ([], []),

        # Test case 6: Single-element list
        ([42], [42]),

        # Test case 7: List with negative numbers
        ([-3, -1, -7, -5, -2], [-7, -5, -3, -2, -1]),

        # Test case 8: Mixed positive and negative numbers
        ([3, -1, 7, -5, 2], [-5, -1, 2, 3, 7]),

        # Test case 9: List with zero
        ([0, 5, 3, 0, 2, -1], [-1, 0, 0, 2, 3, 5]),

        # Test case 10: Large numbers
        ([99999, 123456, -123456, 0], [-123456, 0, 99999, 123456]),
    ]

    for idx, (input_list, expected) in enumerate(test_cases, start=1):
        result = func(input_list)
        if result == expected:
            print(f"Test Case {idx} -> {input_list} : Pass ✅")
        else:
            print(f"Test Case {idx} -> {input_list} : Fail ❌ (Got {result}, Expected {expected})")

# thank you chatgpt.... i mean what i totally wrote this all myself huh what do you mean i'm lying