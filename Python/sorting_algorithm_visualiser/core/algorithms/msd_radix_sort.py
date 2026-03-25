def msd_radix_sort(state):
    arr = state.arr
    n = len(arr)

    max_num = max(arr)
    max_digits = len(str(max_num))

    yield from _msd_sort(state, arr, 0, n - 1, max_digits - 1)

    for i in range(n):
        state.sorted_.add(i)
    
def _msd_sort(state, arr, lo, hi, digit):
    if lo >= hi or digit < 0:
        return

    buckets = [[] for _ in range(10)]

    for i in range(lo, hi + 1):
        d = (arr[i] // (10 ** digit)) % 10

        state.active = {i}
        yield

        buckets[d].append(arr[i])

    pos = lo
    for bucket in buckets:
        for val in bucket:
            arr[pos] = val
            state.active = {pos}
            yield
            pos += 1

    pos = lo
    for bucket in buckets:
        if len(bucket) > 1:
            yield from _msd_sort(state, arr, pos, pos + len(bucket) - 1, digit - 1)
        
        pos += len(bucket)
