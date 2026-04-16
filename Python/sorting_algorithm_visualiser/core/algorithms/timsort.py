# how the fuck did i let the wrong implementation of timsort get through?
# i'm a filthy vibe coder :fearful:
# should be corrected now (i think?) with natural run detection and run stack + invariants
def timsort(state):
    arr = state.arr
    n = len(arr)

    min_run = compute_min_run(n)

    runs = []

    i = 0
    while i < n:
        run_len = yield from _count_run(state, arr, i, n)

        if run_len < min_run:
            force = min(min_run, n - i)
            yield from _insertion(state, arr, i, i + force)
            run_len = force
        
        runs.append((i, run_len))
        yield from _merge_collapse(state, arr, runs)

        i += run_len

    yield from _merge_force_collapse(state, arr, runs)

    for i in range(n):
        state.sorted_.add(i)

def compute_min_run(n):
    r = 0

    while n >= 64:
        r |= n & 1
        n >>= 1

    return n + r

def _count_run(state, arr, start, n):
    if start >= n:
        return 0

    if start >= n - 1:
        state.active = {start}
        yield
        
        return 1
    
    i = start + 1

    if arr[i] < arr[start]:
        state.active = {start, i}
        yield

        while i < n and arr[i] < arr[i - 1]:
            state.active = {i - 1, i}
            yield

            i += 1

        arr[start:i] = reversed(arr[start:i])
    else:
        state.active = {start, i}
        yield

        while i < n and arr[i] >= arr[i - 1]:
            state.active = {i - 1, i}
            yield

            i += 1
    
    return i - start

def _insertion(state, arr, lo, hi):
    for i in range(lo + 1, hi):
        key = arr[i]
        j = i - 1

        while j >= lo and arr[j] > key:
            state.active = {j, j + 1}
            yield

            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

def _merge_collapse(state, arr, runs):
    while True:
        n = len(runs)
        if n <= 1:
            return
    
        if n >= 3:
            A = runs[-3][1]
            B = runs[-2][1]
            C = runs[-1][1]

            if A <= B + C:
                if A < C:
                    yield from _merge_at(state, arr, runs, -3)
                else:
                    yield from _merge_at(state, arr, runs, -2)
                continue
        
        if n >= 2:
            B = runs[-2][1]
            C = runs[-1][1]

            if B <= C:
                yield from _merge_at(state, arr, runs, -2)
                continue
        
        break

def _merge_force_collapse(state, arr, runs):
    while len(runs) > 1:
        yield from _merge_at(state, arr, runs, -2)

def _merge_at(state, arr, runs, i):
    start1, len1 = runs[i]
    start2, len2 = runs[i + 1]

    yield from _merge(state, arr, start1, start1 + len1 - 1, start2 + len2 - 1)

    runs[i] = (start1, len1 + len2)
    del runs[i + 1]

def _merge(state, arr, left, mid, right):
    l, r = arr[left:mid+1], arr[mid+1:right+1]
    i = j = 0
    k = left

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1

        state.active = {k}
        yield

        k += 1

    while i < len(l):
        arr[k] = l[i]
        state.active = {k}
        yield

        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        state.active = {k}
        yield

        j += 1
        k += 1
