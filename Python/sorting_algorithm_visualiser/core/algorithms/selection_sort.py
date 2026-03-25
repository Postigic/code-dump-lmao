def selection_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            state.active = {min_index, j}
            yield

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        state.sorted_.add(i)
