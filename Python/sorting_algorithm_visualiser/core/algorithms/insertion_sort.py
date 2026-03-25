# how have i only realised now that insertion PICKS up
# the first element of the unsorted partition?
# never calling myself a programmer ever again...
def insertion_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            state.active = {j, j + 1}
            yield

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    for i in range(n):
        state.sorted_.add(i)

def binary_insertion_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        lo, hi = 0, i

        while lo < hi:
            mid = (lo + hi) // 2

            state.active = {mid, i}
            yield

            if arr[mid] < key:
                lo = mid + 1
            else:
                hi = mid

        j = i

        while j > lo:
            state.active = {j, j - 1}
            yield

            arr[j] = arr[j - 1]
            j -= 1
        
        arr[lo] = key

    for i in range(n):
        state.sorted_.add(i)
