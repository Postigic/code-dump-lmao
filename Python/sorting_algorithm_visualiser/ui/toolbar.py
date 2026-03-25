import dearpygui.dearpygui as dpg
from core.engine import engine
from ui.canvas import draw_bars
from ui.info_panel import update_info_panel
from core.constants import DATASET_NAMES, ALGO_NAMES, SIZES

SPEEDS = {
    "Glacial": 0.1,
    "Slow": 0.5,
    "Normal": 1.0,
    "Fast": 2.0,
    "Turbo": 4.0,
    "Ludicrous": 6.0
}

def _reset_controls():
    dpg.set_item_label("run_btn", "Run")
    dpg.enable_item("step_btn")

def on_dataset_change(_, app_data):
    engine.set_dataset(app_data)
    draw_bars()
    _reset_controls()

def on_algo_change(_, app_data):
    engine.set_algo(app_data)
    draw_bars()
    update_info_panel()
    _reset_controls()

def on_shuffle():
    engine.shuffle()
    draw_bars()
    _reset_controls()

def on_run():
    now_running = engine.run()

    if now_running:
        dpg.disable_item("step_btn")
        dpg.set_item_label("run_btn", "Stop")
    else:
        dpg.enable_item("step_btn")
        dpg.set_item_label("run_btn", "Run")

def on_step():
    if not dpg.is_item_enabled("step_btn"):
        return

    alive = engine.step()
    draw_bars()

    if not alive:
        dpg.set_item_label("run_btn", "Run")

def on_size_change(_, app_data):
    engine.set_size(int(app_data))
    draw_bars()
    _reset_controls()

def on_speed_change(_, app_data):
    engine.speed = SPEEDS[app_data]

def on_mute(_, app_data):
    engine.muted = app_data

# i know i violated DRY i just don't care anymore
def setup_toolbar(parent):
    with dpg.theme() as tooltip_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (42, 35, 28))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (85, 69, 56, 180))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (210, 190, 165))
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 8, 5)
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 4)
            dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 1)

    with dpg.group(parent=parent):
        with dpg.group(horizontal=True):
            dpg.add_combo(label="Algorithm", items=ALGO_NAMES, default_value=engine.algo_name, callback=on_algo_change, width=200)

            dpg.add_spacer(width=20)

            dpg.add_combo(label="Dataset", items=DATASET_NAMES, default_value="Random", callback=on_dataset_change, width=200)
            dpg.add_combo(label="Size", items=SIZES, default_value=str(engine.state.n), callback=on_size_change, width=70)

            dpg.add_spacer(width=20)

            dpg.add_combo(label="Speed", items=list(SPEEDS.keys()), default_value="Normal", callback=on_speed_change, width=150)
            dpg.add_checkbox(label="Mute", default_value=engine.muted, callback=on_mute)

        with dpg.group(horizontal=True):
            dpg.add_button(label="Shuffle", callback=on_shuffle)

            with dpg.tooltip(dpg.last_item()) as tooltip:
                dpg.add_text("F5")

            dpg.bind_item_theme(tooltip, tooltip_theme)

            dpg.add_button(label="Step", tag="step_btn", callback=on_step)
            
            with dpg.tooltip(dpg.last_item()) as tooltip:
                dpg.add_text("Right Arrow")    
            
            dpg.bind_item_theme(tooltip, tooltip_theme)
            
            dpg.add_button(label="Run", tag="run_btn", callback=on_run)
            
            with dpg.tooltip(dpg.last_item()) as tooltip:
                dpg.add_text("Space")

            dpg.bind_item_theme(tooltip, tooltip_theme)

    dpg.add_separator()
