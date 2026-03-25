import dearpygui.dearpygui as dpg
from core.constants import ALGO_INFO
from core.engine import engine

def setup_info_panel(parent):
    with dpg.group(parent=parent):
        dpg.add_separator()

        with dpg.group():
            dpg.add_text("", tag="info_desc", wrap=0)
            dpg.bind_item_font("info_desc", engine.font_sans)
        
        dpg.add_spacer(height=10)

        with dpg.group(horizontal=True):
            dpg.add_text("Worst:", color=(150, 150, 150))
            dpg.add_text("", tag="info_worst")
            dpg.bind_item_font("info_worst", engine.font_mono)

            dpg.add_spacer(width=20)

            dpg.add_text("Avg:", color=(150, 150, 150))
            dpg.add_text("", tag="info_avg")
            dpg.bind_item_font("info_avg", engine.font_mono)

            dpg.add_spacer(width=20)

            dpg.add_text("Best:", color=(150, 150, 150))
            dpg.add_text("", tag="info_best")
            dpg.bind_item_font("info_best", engine.font_mono)

            dpg.add_spacer(width=20)

            dpg.add_text("Aux:", color=(150, 150, 150))
            dpg.add_text("", tag="info_aux")
            dpg.bind_item_font("info_aux", engine.font_mono)

        with dpg.group(horizontal=True):
            dpg.add_text("Stable:", color=(150, 150, 150))
            dpg.add_text("", tag="info_stable")

            dpg.add_spacer(width=20)

            dpg.add_text("In-place:", color=(150, 150, 150))
            dpg.add_text("", tag="info_inplace")

        with dpg.group(horizontal=True):
            dpg.add_text("Comparisons")

def update_info_panel():
    info = ALGO_INFO.get(engine.algo_name)

    if not info:
        return
    
    dpg.set_value("info_desc", info.get("desc", ""))
    dpg.set_value("info_worst", info["time_worst"])
    dpg.set_value("info_avg", info["time_avg"])
    dpg.set_value("info_best", info["time_best"])
    dpg.set_value("info_aux", info["aux"])
    dpg.set_value("info_stable", "N/A" if info["stable"] is None else "Yes" if info["stable"] else "No")
    dpg.set_value("info_inplace", "Yes" if info["inplace"] else "No")
