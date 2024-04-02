# Edge Terminal - Created by @cascade_ed


import dearpygui.dearpygui as dpg
from wrap import RectWrappingCollection

# Filler values - CHANGE THIS
ticker = "BTC"              # Ticker w/o pair
ticker_price = 69420.55     # Current Ticker Price
ticker_change = 55.25       # Current Ticker Change % in the last 5 minutes
acc_balance = 11115000.5        # Total Account Balance (excluding uPNL)
acc_risk_percent = 15.55  # Total Account Risk in Percentage
acc_risk_usd = 111500.5       # Total Account Risk in USD

dpg.create_context()

#region Styling
GREEN_COLOR = (7, 183, 138)
GREEN_HOVER_COLOR = (2, 133, 114, 255)
RED_COLOR = (255, 62, 78, 255)
RED_HOVER_COLOR = (205, 75, 79, 255)
PRIMARY_COLOR = (107, 103, 160, 255)
PRIMARY_HOVER_COLOR = (91, 87, 118, 255)
BACKGROUND_COLOR = (37, 37, 38, 255)

with dpg.font_registry():
    default_font = dpg.add_font("JetBrainsMono-Regular.ttf", 16)
    default_bold_font = dpg.add_font("JetBrainsMono-Bold.ttf", 16)
    small_font = dpg.add_font("JetBrainsMono-Regular.ttf", 12)
    small_bold_font = dpg.add_font("JetBrainsMono-Bold.ttf", 12)
    large_font = dpg.add_font("JetBrainsMono-Regular.ttf", 20)
    large_bold_font = dpg.add_font("JetBrainsMono-Bold.ttf", 20)

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, PRIMARY_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, PRIMARY_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, PRIMARY_HOVER_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, PRIMARY_HOVER_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, PRIMARY_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, PRIMARY_HOVER_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, PRIMARY_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 5, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3, category=dpg.mvThemeCat_Core)

with dpg.theme() as green_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Button, GREEN_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, GREEN_HOVER_COLOR, category=dpg.mvThemeCat_Core)

with dpg.theme() as red_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Button, RED_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, RED_HOVER_COLOR, category=dpg.mvThemeCat_Core)

# Button masked as text to align right (No alignment support for DearPyGUI)
with dpg.theme() as hidden_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 1.00, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, BACKGROUND_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, BACKGROUND_COLOR, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, BACKGROUND_COLOR, category=dpg.mvThemeCat_Core)

#endregion

#region GUI
with dpg.window(label="Edge Terminal", width=500, height=350, no_move=True, no_resize=True, no_collapse=True,
                on_close=lambda: dpg.destroy_context()) as main_window:

    dpg.add_spacer(height=1)

    with dpg.group(label="Overview", indent=5):
        with dpg.group(label="Ticker Info", horizontal=True):
            dpg.add_input_text(tag="Ticker", default_value="BTCUSD", no_spaces=True, uppercase=True, hint="BTCUSD",
                               width=125)
            dpg.bind_item_font("Ticker", large_bold_font)
            dpg.add_text('${:,}'.format(ticker_price), tag="Price")
            dpg.bind_item_font("Price", large_bold_font)
            dpg.add_text('{:,.2f}%'.format(ticker_change), tag="Change", color=RED_COLOR)

            with dpg.group(label="Quick Buttons", horizontal=True, height=30, pos=(315, 38)):
                dpg.add_button(label="QuickBuy", tag="QuickBuy")
                dpg.bind_item_theme("QuickBuy", green_theme)
                dpg.add_button(label="QuickSell", tag="QuickSell")
                dpg.bind_item_theme("QuickSell", red_theme)

        with dpg.group(label="Account Info", horizontal=True):
            dpg.add_button(label="Detect", tag="Detect")  # Auto-detect ticker on screen

            wrapper = [RectWrappingCollection(text_align=0)]

            def update_pos(widget):
                pos = list(wrapper[0].get_sizes())

                offset_x, offset_y = dpg.get_item_pos(widget)
                for i, rect in enumerate(dpg.get_item_children(widget, 1)):
                    x, y = pos[i]
                    dpg.set_item_pos(rect, (offset_x + x, offset_y + y))


            with dpg.group(tag="Account Text") as acc_text_group:
                balance_label = dpg.add_text("Balance:", parent=acc_text_group)
                balance_value = dpg.add_text('${:,.1f}'.format(acc_balance), parent=acc_text_group)
                dpg.bind_item_font(balance_value, default_bold_font)
                risk_label = dpg.add_text("  Risk:", parent=acc_text_group)
                risk_percent_value = dpg.add_text('{:,.2f}%'.format(acc_risk_percent), parent=acc_text_group, color=RED_COLOR)
                dpg.bind_item_font(risk_percent_value, default_bold_font)
                risk_usd_value = dpg.add_text('${:,.1f}'.format(acc_risk_usd), parent=acc_text_group)
                dpg.bind_item_font(risk_usd_value, default_bold_font)

                def add_rects():
                    for i, widget in enumerate(dpg.get_item_children(acc_text_group, 1)):
                        if dpg.get_item_type(widget) == 'mvAppItemType::mvText':
                            font = dpg.get_item_font(widget)
                            wrapper[0].add_rect(
                                *dpg.get_text_size(
                                    dpg.get_value(widget),
                                    font=font
                                )
                            )
                        else:
                            wrapper[0].add_rect(*dpg.get_item_rect_size(widget))

                    wrapper[0].set_wrap(410)
                    wrapper[0].set_align(2)
                    update_pos(acc_text_group)

                dpg.set_frame_callback(3, add_rects)

        dpg.add_spacer(height=2)

        with dpg.group(tag="Position Info", horizontal=True):
            with dpg.table(header_row=False, row_background=True, width=470):
                dpg.add_table_column(indent_enable=True)  # Ticker
                dpg.add_table_column()  # Entry
                dpg.add_table_column()  # Liq
                dpg.add_table_column()  # Soft SL
                dpg.add_table_column()  # Hard SL
                dpg.add_table_column()  # PnL

                with dpg.table_row(tag="Position Header") as pos_header:
                    header_ticker = dpg.add_text("Ticker", indent=5)
                    header_entry = dpg.add_text("Entry")
                    header_liq = dpg.add_text("Liq")
                    header_softSL = dpg.add_text("Soft SL")
                    header_hardSL = dpg.add_text("Hard SL")
                    header_pnl = dpg.add_text("PnL")
                    dpg.bind_item_font(header_ticker, small_font)
                    dpg.bind_item_font(header_entry, small_font)
                    dpg.bind_item_font(header_liq, small_font)
                    dpg.bind_item_font(header_softSL, small_font)
                    dpg.bind_item_font(header_hardSL, small_font)
                    dpg.bind_item_font(header_pnl, small_font)

                with dpg.table_row(tag="Position Data"):
                    dpg.add_text("BTCUSD", indent=5)
                    dpg.add_text("$69,420.5")
                    dpg.add_text("$64,000.5")
                    dpg.add_text("$64,200.0")
                    dpg.add_text("$64,100.0")
                    dpg.add_text("+$5,500.5", color=GREEN_COLOR)

    dpg.add_spacer(height=10)

    with dpg.tab_bar(label="Actions"):
        with dpg.tab(label="Limit", indent=5):
            dpg.add_spacer(height=5)
            with dpg.group(horizontal=True):
                dpg.add_text("Trade Risk %")
                dpg.add_drag_float(min_value=0.1, max_value=100, speed=0.01, format='%0.2f%%', clamped=True, width=100)
                dpg.add_spacer(width=50)
                dpg.add_text("Acc Risk %")
                dpg.add_drag_float(min_value=0.1, max_value=100, speed=0.1, format='%0.2f%%', clamped=True, width=100)

            dpg.add_spacer(height=5)
            with dpg.group(label="Buttons", horizontal=True):
                with dpg.group(horizontal=True) as longs:
                    dpg.add_button(label="1.0%")
                    dpg.add_button(label="1.5%")
                    dpg.add_button(label="2.0%")
                    dpg.add_button(label="2.5%")

                dpg.add_spacer()
                with dpg.group(horizontal=True) as shorts:
                    dpg.add_button(label="1.0%")
                    dpg.add_button(label="1.5%")
                    dpg.add_button(label="2.0%")
                    dpg.add_button(label="2.5%")

        with dpg.tab(label="Market"):
            dpg.add_button(label="Buy")
            dpg.add_button(label="Sell")


# Setting styling
dpg.bind_font(default_font)
dpg.bind_theme(global_theme)
dpg.bind_item_theme(longs, green_theme)
dpg.bind_item_theme(shorts, red_theme)

#endregion

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
    is_title_bar_clicked = True if dpg.get_mouse_pos(local=False)[1] < 30 else False  # 30 pixels Title Bar


with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)
    dpg.add_mouse_click_handler(button=0, callback=mouse_click_callback)

#endregion

dpg.create_viewport(width=500, height=350, decorated=False, always_on_top=True, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
