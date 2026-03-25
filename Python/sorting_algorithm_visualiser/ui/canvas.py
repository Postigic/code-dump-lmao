import dearpygui.dearpygui as dpg
from core.engine import engine
from core.constants import MAX_SIZE

BLUE = (70, 130, 210)
RED = (210, 80, 55)
GREEN = (45, 150, 100)
AMBER = (230, 145, 30)

def setup_canvas(parent):
    dpg.add_drawlist(tag="canvas", width=780, height=400, parent=parent)

    for i in range(MAX_SIZE):
        dpg.draw_rectangle([0, 0], [0, 0], fill=BLUE, color=(0, 0, 0, 0), tag=f"bar_{i}", parent="canvas")

def draw_bars():
    state = engine.state
    n = len(state.arr)

    if n == 0:
        return
    
    w = dpg.get_item_width("canvas")
    h = dpg.get_item_height("canvas")
    bar_w = w / n

    for i in range(MAX_SIZE):
        if i < n:
            val = state.arr[i]
            x0 = i * bar_w
            x1 = x0 + bar_w - 1
            bar_h = (val / state.n) * h
            y0 = h - bar_h

            if i in state.pivot:
                color = AMBER
            elif i in state.active:
                color = RED
            elif i in state.sorted_:
                color = GREEN
            else:
                color = BLUE

            dpg.configure_item(f"bar_{i}", pmin=[x0, y0], pmax=[x1, h], fill=color)
        else:
            dpg.configure_item(f"bar_{i}", pmin=[0,0], pmax=[0,0])
