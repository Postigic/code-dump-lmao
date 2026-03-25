def stalin_sort(state):
    arr = state.arr
    i = 1

    while i < len(arr):
        state.active = {i, i - 1}
        yield

        if arr[i] < arr[i - 1]:
            arr.pop(i)
        else:
            state.sorted_.add(i - 1)
            i += 1

    for i in range(len(arr)):
        state.sorted_.add(i)
