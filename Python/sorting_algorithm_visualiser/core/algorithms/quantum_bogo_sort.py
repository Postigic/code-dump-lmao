import dearpygui.dearpygui as dpg

def quantum_bogo_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n - 1):
        state.active = {i, i + 1}
        yield

        if arr[i] > arr[i + 1]:
            dpg.stop_dearpygui()

    state.active.clear()
    yield

    for i in range(n):
        state.sorted_.add(i)
