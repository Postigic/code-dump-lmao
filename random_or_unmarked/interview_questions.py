import heapq
from collections import Counter
from math import ceil
from functools import reduce
from math import log, pow, exp


def print_pass(test_name):
    print(f"{test_name}:\t Pass ✅")


def print_fail(test_name):
    print(f"{test_name}:\t Fail ❌")

# Exercise 1: Multiply 2 numbers without using the * symbol


def test_mult(func):
    if func(5, 6) == 5*6:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

# Solutions


def mult_recursive(num1, num2):
    if num2 == 1:
        return num1
    return num1 + mult_recursive(num1, num2 - 1)


test_mult(mult_recursive)


def mult_loop(num1, num2):
    sum = 0
    for i in range(num2):
        sum += num1
    return sum


test_mult(mult_loop)


def mult_exp(num1, num2):
    return log(pow(exp(num1), num2))


test_mult(mult_exp)

# Print separation line

print("-------------------------")

# Exercise 2: Find the largest number in a list


def test_largest(func):
    if func([8, 6, 7, 5, 309]) == 309:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

# Solutions


def largest_loop(numlist):
    largest = numlist[0]
    for num in numlist:
        if largest < num:
            largest = num
    return largest


test_largest(largest_loop)


def largest_simple(numlist):
    return max(numlist)


test_largest(largest_simple)


def largest_recursive(numlist):
    if len(numlist) == 2:
        if numlist[0] < numlist[1]:
            return numlist[1]
        return numlist[0]
    leftmost = numlist[0]
    largest_on_right = largest_recursive(numlist[1:])
    if largest_on_right > leftmost:
        return largest_on_right
    return leftmost


test_largest(largest_recursive)


def largest_functional(numlist):
    return reduce(lambda x, y: x if x > y else y, numlist)


test_largest(largest_functional)

# Print separation line

print("-------------------------")

# Exercise 3: Check if a string is a palindrome permutation
# E.g. "tacocat", "acocatt", and "cattaco" would all be true


def test_palindrome(func):
    if (func("tacocat") and func("acocatt") and not func("tacodog")):
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

# Solutions


def palindrome_loop(letters):
    def rotate(s):
        return s[1:] + s[0]

    def is_palindrome(s):
        while len(s) > 1:
            if s[0] != s[-1]:
                return False
            s = s[1:-1]
        return True

    temp_str = str(letters)
    for _ in letters:
        if is_palindrome(temp_str):
            return True
        temp_str = rotate(temp_str)
    return False


test_palindrome(palindrome_loop)


def palindrome_stack(letters):
    stack_size = ceil(len(letters)/2)
    stack = ""
    repeated = letters + letters
    for idx, l in enumerate(letters + letters):
        stack = l + stack
        stack = stack[-stack_size:]
        if stack == repeated[idx: (idx + stack_size)]:
            return True
    return False


test_palindrome(palindrome_stack)

# Print separation line

print("-------------------------")

# Exercise 4: Determine if all the characters in a string are unique


def test_unique(func):
    if func("asdf") and not func("asdfa"):
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

# Solutions


def is_unique_set(chars):
    return len(chars) == len(set(chars))


test_unique(is_unique_set)


def is_unique_sort(chars):
    prev = ""
    for char in sorted(list(chars)):
        if char == prev:
            return False
        prev = char
    return True


test_unique(is_unique_sort)


def is_unique_count(chars):
    for char in chars:
        if chars.count(char) > 1:
            return False
    return True


test_unique(is_unique_count)


def is_unique_alphabet(chars):
    alphabet = list(set("thequickbrownfoxjumpsoverthelazydog"))
    alphabet_size = len(alphabet)
    alphabet = [c for c in alphabet if c not in chars]
    result = (alphabet_size - len(chars)) == len(alphabet)
    return result


test_unique(is_unique_alphabet)

# Print separation line

print("-------------------------")

# Exercise 5: Check if a pair of strings are an anagram
# E.g. "nameless" and "salesmen" would be true


def test_anagram(func):
    if func("nameless", "salesmen") and not func("garden", "dagger"):
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

# Solutions


def are_anagrams_dict(str1, str2):
    if len(str1) != len(str2):
        return False
    freq1 = {}
    freq2 = {}
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


test_anagram(are_anagrams_dict)


def are_anagrams_counter(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


test_anagram(are_anagrams_counter)


def are_anagrams_sort(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


test_anagram(are_anagrams_sort)

# Print separation line

print("-------------------------")

# Exercise 6: Find the range of a specific element in an array


def test_range(func):
    if func([2, 4, 5, 5, 5, 5, 5, 7, 9, 9], 5) == [2, 6] and func([2, 4, 4, 6, 7, 9], 5) == [-1, -1]:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

# Solutions


def target_range_loop(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i + 1] == target:
                i += 1
            return [start, i]
    return [-1, -1]


test_range(target_range_loop)


def target_range_binary(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]

    def find_start():
        if arr[0] == target:
            return 0
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target and arr[mid - 1] < target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def find_end():
        if arr[-1] == target:
            return len(arr) - 1
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target and arr[mid + 1] > target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    return [find_start(), find_end()]


test_range(target_range_binary)

# Print separation line

print("-------------------------")

# Exercise 7: Find the kth largest element in an array


def test_kth_largest(func):
    if func([4, 2, 9, 7, 5, 6, 7, 1, 3], 4) == 6:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

# Solutions


def kth_largest_loop(arr, k):
    for _ in range(k - 1):
        arr.remove(max(arr))
    return max(arr)


test_kth_largest(kth_largest_loop)


def kth_largest_sort(arr, k):
    arr.sort()
    return arr[len(arr) - k]


test_kth_largest(kth_largest_sort)


def kth_largest_heap(arr, k):
    neg_arr = [-elem for elem in arr]
    heapq.heapify(neg_arr)
    for _ in range(k - 1):
        heapq.heappop(neg_arr)
    return -heapq.heappop(neg_arr)


test_kth_largest(kth_largest_heap)
