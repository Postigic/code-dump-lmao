def intelligent_design_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n):
        state.sorted_.add(i)
    
    yield
