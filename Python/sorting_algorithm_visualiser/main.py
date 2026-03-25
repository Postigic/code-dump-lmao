import dearpygui.dearpygui as dpg
from ui.toolbar import setup_toolbar, on_run, on_step, on_shuffle
from ui.canvas import setup_canvas, draw_bars
from ui.info_panel import setup_info_panel, update_info_panel
from core.engine import engine

frame_count = 0

def on_resize(_, appdata):
    width, height = dpg.get_viewport_width(), dpg.get_viewport_height()
    dpg.configure_item("canvas", width=width - 30, height=height - 350)
    draw_bars()

def render_loop():
    global frame_count
    dpg.set_frame_callback(dpg.get_frame_count() + 1, render_loop)
    
    if not dpg.is_viewport_ok():
        return
    
    w = dpg.get_item_width("canvas")
    h = dpg.get_item_height("canvas")
    
    if w <= 0 or h <= 0:
        return

    frame_count += 1

    if engine.running:
        engine.tick(frame_count)
        draw_bars()

        if not engine.running:
            dpg.set_item_label("run_btn", "Run")
            dpg.enable_item("step_btn")

def main():
    dpg.create_context()

    with dpg.font_registry():
        engine.font_sans = dpg.add_font("fonts/DMSans-Regular.ttf", 25)
        engine.font_mono = dpg.add_font("fonts/JetBrainsMono-Regular.ttf", 25)

    dpg.bind_font(engine.font_sans)

    with dpg.window(tag="main", no_title_bar=True, no_move=True, no_resize=True):
        setup_toolbar("main")
        setup_canvas("main")
        setup_info_panel("main")

    dpg.set_primary_window("main", True)

    dpg.create_viewport(title="Sorting Visualiser", width=1200, height=900, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()

    with dpg.handler_registry():
        dpg.add_key_press_handler(key=dpg.mvKey_Spacebar, callback=on_run)
        dpg.add_key_press_handler(key=dpg.mvKey_Right, callback=on_step)
        dpg.add_key_press_handler(key=dpg.mvKey_F5, callback=on_shuffle)

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (32, 28, 24))

            dpg.add_theme_color(dpg.mvThemeCol_Button, (46, 39, 32))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (61, 50, 40))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (85, 69, 56))

            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (46, 39, 32))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (61, 50, 40))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (85, 69, 56))

            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (30, 25, 20))

            dpg.add_theme_color(dpg.mvThemeCol_Header, (55, 42, 32))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (80, 61, 44))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (100, 78, 55))

            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (30, 25, 20))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (85, 69, 56))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (100, 82, 65))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (120, 98, 76))

            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (240, 168, 48))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (85, 69, 56))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (61, 50, 40))

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

    dpg.bind_theme(global_theme)

    with dpg.theme() as disabled_theme:
        with dpg.theme_component(dpg.mvButton, enabled_state=False):
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (38, 32, 26))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (38, 32, 26))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (38, 32, 26))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (90, 75, 62))

    dpg.bind_item_theme("step_btn", disabled_theme)

    dpg.set_frame_callback(1, lambda: [draw_bars(), update_info_panel()])
    dpg.set_frame_callback(2, render_loop)
    dpg.set_viewport_resize_callback(on_resize)

    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()
