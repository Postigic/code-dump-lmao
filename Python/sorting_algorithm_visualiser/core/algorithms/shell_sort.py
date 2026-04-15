def shell_sort(state):
    arr = state.arr
    n = len(arr)
    
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                state.active = {j, j - gap}
                yield

                arr[j] = arr[j - gap]

                j -= gap

            arr[j] = key

            state.active = {i, j}
            yield

        gap //= 2

    for i in range(n):
        state.sorted_.add(i)
