import random

def quick_sort(state):
    arr = state.arr
    yield from _qs(state, arr, 0, len(arr) - 1, randomised=False, median=False)
 
def randomised_quick_sort(state):
    arr = state.arr
    yield from _qs(state, arr, 0, len(arr) - 1, randomised=True, median=False)
 
def median_of_three_quick_sort(state):
    arr = state.arr
    yield from _qs(state, arr, 0, len(arr) - 1, randomised=False, median=True)

def three_way_quick_sort(state):
    arr = state.arr
    yield from _qs_3way(state, arr, 0, len(arr) - 1)
 
def dual_pivot_quick_sort(state):
    arr = state.arr
    yield from _qs_dual(state, arr, 0, len(arr) - 1)

def _qs(state, arr, lo, hi, randomised, median):
    if lo >= hi:
        if lo == hi:
            state.sorted_.add(lo)
        return

    yield from _partition(state, arr, lo, hi, randomised, median)

    pivot_idx, = state.pivot
    state.sorted_.add(pivot_idx)
    state.pivot.clear()

    yield from _qs(state, arr, lo, pivot_idx - 1, randomised, median)
    yield from _qs(state, arr, pivot_idx + 1, hi, randomised, median)

def _partition(state, arr, lo, hi, randomised, median):
    if randomised:
        rand_idx = random.randint(lo, hi)
        
        arr[rand_idx], arr[hi] = arr[hi], arr[rand_idx]

        state.active = {rand_idx, hi}
        yield

        state.pivot = {hi}
        state.active = {rand_idx}
        yield
    elif median and hi - lo >= 2:
        mid = (lo + hi) // 2

        state.active = {lo, mid, hi}
        yield

        if arr[lo] > arr[mid]:
            arr[lo], arr[mid] = arr[mid], arr[lo]

            yield
        
        if arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]

            yield
        
        if arr[mid] > arr[hi]:
            arr[mid], arr[hi] = arr[hi], arr[mid]

            yield
        
        arr[mid], arr[hi] = arr[hi], arr[mid]

        yield

        state.pivot = {hi}
        state.active = {mid}
        yield

    pivot = arr[hi]
    state.pivot = {hi}
    i = lo - 1

    for j in range(lo, hi):
        state.active = {j, hi}
        yield

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

            state.active = {i, j}
            yield

    state.active = {i + 1, hi}
    yield

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]

    yield

    state.pivot = {i + 1}

def _qs_3way(state, arr, lo, hi):
    if lo >= hi:
        if lo == hi:
            state.sorted_.add(lo)
        return
 
    lt, gt = yield from _partition_3way(state, arr, lo, hi)
 
    for i in range(lt, gt + 1):
        state.sorted_.add(i)
 
    yield from _qs_3way(state, arr, lo, lt - 1)
    yield from _qs_3way(state, arr, gt + 1, hi)
 
def _partition_3way(state, arr, lo, hi):
    pivot = arr[lo]
    state.pivot = {lo}
 
    lt = lo
    gt = hi
    i = lo
 
    while i <= gt:
        state.active = {i, lt, gt}
        yield
 
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]

            state.active = {i, lt}
            yield

            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]

            state.active = {i, gt}
            yield

            gt -= 1
        else:
            i += 1
 
    state.active = set()
    state.pivot.clear()
    return lt, gt

def _qs_dual(state, arr, lo, hi):
    if lo >= hi:
        if lo == hi:
            state.sorted_.add(lo)
        return
 
    lt, gt = yield from _partition_dual(state, arr, lo, hi)
 
    state.sorted_.add(lt)
    state.sorted_.add(gt)
 
    yield from _qs_dual(state, arr, lo, lt - 1)
    yield from _qs_dual(state, arr, lt + 1, gt - 1)
    yield from _qs_dual(state, arr, gt + 1, hi)
 
def _partition_dual(state, arr, lo, hi):
    state.active = {lo, hi}
    yield

    if arr[lo] > arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]

        yield
 
    p1 = arr[lo]
    p2 = arr[hi]
    state.pivot = {lo, hi}
 
    lt = lo + 1
    gt = hi - 1
    k = lo + 1
 
    while k <= gt:
        state.active = {k, lo, hi}
        yield
 
        if arr[k] < p1:
            arr[k], arr[lt] = arr[lt], arr[k]

            state.active = {k, lt}
            yield

            lt += 1
            k += 1
        elif arr[k] > p2:
            arr[k], arr[gt] = arr[gt], arr[k]

            state.active = {k, gt}
            yield

            gt -= 1
        else:
            k += 1
 
    lt -= 1
    gt += 1
 
    arr[lo], arr[lt] = arr[lt], arr[lo]
    arr[hi], arr[gt] = arr[gt], arr[hi]

    state.active = {lo, lt, hi, gt}
    yield
 
    state.active = set()
    state.pivot.clear()
    return lt, gt
 