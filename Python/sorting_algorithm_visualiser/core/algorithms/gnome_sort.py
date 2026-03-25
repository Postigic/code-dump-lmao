def gnome_sort(state):
    arr = state.arr
    n = len(arr)
    
    i = 0

    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            state.active = {i} if i + 1 >= n else {i, i + 1}
            yield

            i += 1
        else:
            state.active = {i, i - 1}
            yield

            arr[i], arr[i - 1] = arr[i - 1], arr[i]            
            i -= 1

    for i in range(n):
        state.sorted_.add(i)
