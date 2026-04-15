def pancake_sort(state):
    arr = state.arr
    n = len(arr)

    for size in range(n, 1, -1):
        max_idx = arr.index(max(arr[:size]))

        if max_idx != size - 1:
            state.active = {max_idx, size - 1}
            yield

            if max_idx != 0:
                state.active = {0, max_idx}
                yield

                arr[:max_idx+1] = arr[:max_idx+1][::-1]

                state.active = {0, size - 1}
                yield
            
            arr[:size] = arr[:size][::-1]
            yield

        state.sorted_.add(size - 1)

    state.sorted_.add(0)
