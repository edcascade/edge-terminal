# Edge Terminal - Created by @cascade_ed

import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    jetbrains_font = dpg.add_font("JetBrainsMono-Regular.ttf", 16)


with dpg.window(label="Edge Terminal", width=500, height=300, no_move=True, no_resize=True, no_collapse=True, on_close=lambda: dpg.destroy_context()):
    with dpg.tab_bar(label="Trade Type"):
        with dpg.tab(label="Limit"):
            dpg.add_input_float(label="Limit Price")
            dpg.add_button(label="Buy")
            dpg.add_button(label="Sell")

        with dpg.tab(label="Market"):
            dpg.add_button(label="Buy")
            dpg.add_button(label="Sell")

    dpg.bind_font(jetbrains_font)  # Set font


#region GUI Drag Window
is_title_bar_clicked = False

def mouse_drag_callback(_, app_data):
    if is_title_bar_clicked:
        _, drag_delta_x, drag_delta_y = app_data
        viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
        new_pos_x = viewport_pos_x + drag_delta_x
        new_pos_y = max(viewport_pos_y + drag_delta_y, 0)
        dpg.set_viewport_pos([new_pos_x, new_pos_y])


def mouse_click_callback():
    global is_title_bar_clicked
    is_title_bar_clicked = True if dpg.get_mouse_pos(local=False)[1] < 30 else False # 30 pixels is slightly more than the height of the default menu bar


with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)
    dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)

#endregion

dpg.create_viewport(width=500, height=300, decorated=False, always_on_top=True, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
