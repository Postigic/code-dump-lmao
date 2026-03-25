# this is like the prisoner box riddle thing i dunno
def cycle_sort(state):
    arr = state.arr
    n = len(arr)

    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start

        for i in range(cycle_start + 1, n):
            state.active = {i, cycle_start}
            yield
            if arr[i] < item:
                pos += 1

        if pos == cycle_start:
            state.sorted_.add(cycle_start)
            continue

        while item == arr[pos]:
            pos += 1

        arr[pos], item = item, arr[pos]
        state.active = {pos, cycle_start}
        yield

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                state.active = {i, cycle_start}
                yield
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]
            state.active = {pos, cycle_start}
            yield

        state.sorted_.add(cycle_start)

    state.sorted_.add(n - 1)
