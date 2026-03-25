def shell_sort(state):
    arr = state.arr
    n = len(arr)
    
    gap = n // 2

    while gap > 0:
        # for the stupid visuals
        start = 0 if gap == 1 else gap

        for i in range(start, n):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                state.active = {j, j - gap}
                yield

                arr[j] = arr[j - gap]
                j -= gap
            
            state.active = {j, i}
            yield

            arr[j] = key
        
            if gap == 1:
                state.sorted_.add(i)

        gap //= 2
