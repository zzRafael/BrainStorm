import PySimpleGUI as sg
from windows import create_initial_window, create_add_window


initial_window, add_window = create_initial_window(), None
initial_window.maximize()

add_window_created = False

while True:
    window, event, values = sg.read_all_windows()

    if window == initial_window:
        if event == sg.WIN_CLOSED:
            break
        elif event == '-INITIAL_ADD_BUTTON-':
            if add_window_created:
                add_window.un_hide()
            else:
                add_window = create_add_window()
                add_window_created = True

    elif window == add_window:
        if event == '-ADD_ORDER_ADD_BUTTON-':
            order_input_number = values["-ADD_ORDER_NUMBER_INPUT-"]
            order_input_model = values["-ADD_ORDER_MODEL_INPUT-"]
            order_combo_process = values["-ADD_ORDER_PROCESS_COMBO-"]

            initial_window.extend_layout(
                initial_window['-INITIAL_TABLE_COLUMN-'],
                [
                    [
                        sg.Frame(
                            title='',
                            size=(390,35),
                            layout=[
                                [
                                    sg.Checkbox(
                                        text=None
                                    ),
                                    sg.Text(
                                        text=f'{order_input_number}',
                                        size=(5,35),
                                        justification='center',
                                    ),
                                    sg.Text(
                                        text=f'{order_input_model}',
                                        size=(20,35),
                                    ),
                                    sg.Text(
                                        text=f'{order_combo_process}',
                                        size=(12,35),
                                    )
                                ]
                            ],
                            key=f'-INITIAL_TABLE_FRAME_{order_input_number}-'
                        )
                    ]
                ]
            )
            
            add_window.hide()
            
        elif event == '-ADD_ORDER_CANCEL_BUTTON-':
            add_window.hide()