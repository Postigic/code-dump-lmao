def counting_sort(state):
    arr = state.arr

    max_num = max(arr)
    count_arr = [0] * (max_num + 1)

    for i, num in enumerate(arr):
        count_arr[num] += 1
        state.active = {i}
        yield

    state.active.clear()
    pos = 0

    for val, count in enumerate(count_arr):
        for _ in range(count):
            arr[pos] = val
            state.sorted_.add(pos)

            state.active = {pos}
            yield
            
            pos += 1

def stable_counting_sort(state):
    arr = state.arr
    n = len(arr)
 
    max_num = max(arr)
    count_arr = [0] * (max_num + 1)
 
    for i, num in enumerate(arr):
        count_arr[num] += 1
        state.active = {i}
        yield
 
    for i in range(1, max_num + 1):
        count_arr[i] += count_arr[i - 1]
 
    state.active.clear()
 
    output = [0] * n
 
    for i in range(n - 1, -1, -1):
        output[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
 
    for i in range(n):
        arr[i] = output[i]
        state.sorted_.add(i)

        state.active = {i}
        yield
  