import random
from algorithm_tester import test_sort

def bogo_sort(arr):
    while not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        random.shuffle(arr)

    return arr

test_sort(bogo_sort)