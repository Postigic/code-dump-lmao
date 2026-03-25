def cocktail_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            state.active = {j, j + 1}
            yield

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        state.sorted_.add(n - i - 1)

        for j in range(n - i - 1, i, -1):
            state.active = {j, j - 1}
            yield

            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

        state.sorted_.add(i)

    state.sorted_.add(0)

def optimised_cocktail_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n // 2):
        swapped = False

        for j in range(i, n - i - 1):
            state.active = {j, j + 1}
            yield

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        state.sorted_.add(n - i - 1)

        for j in range(n - i - 1, i, -1):
            state.active = {j, j - 1}
            yield

            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True

        state.sorted_.add(i)

        if not swapped:
            for k in range(n):
                state.sorted_.add(k)
            break
    
    state.sorted_.add(0)
