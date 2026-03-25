def comb_sort(state):
    arr = state.arr
    n = len(arr)

    gap = n
    shrink = 1.3
    sorted_ = False

    while not sorted_:
        gap = int(gap / shrink)

        if gap <= 1:
            gap = 1
            sorted_ = True

        for i in range(n - gap):
            state.active = {i, i + gap}
            yield

            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_ = False
    
    for i in range(n):
        state.sorted_.add(i)

def comb_sort_11(state):
    arr = state.arr
    n = len(arr)

    gap = n
    shrink = 1.3
    sorted_ = False

    while not sorted_:
        gap = int(gap / shrink)

        if gap <= 1:
            gap = 1
            sorted_ = True
        elif gap == 9 or gap == 10:
            gap = 11

        for i in range(n - gap):
            state.active = {i, i + gap}
            yield

            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_ = False
    
    for i in range(n):
        state.sorted_.add(i)
