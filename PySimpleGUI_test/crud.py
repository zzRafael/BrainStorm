import PySimpleGUI as sg
import os
from windows import create_initial_window, create_add_window
from defs import delete_not_numbers

# creating the windows
initial_window, add_window = create_initial_window(), None

# maximize the initial window
initial_window.maximize()

add_window_created = False

# create / confirm the data path
try:
    os.mkdir('data')
except FileExistsError:
    pass

# main loop
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
            order_input_numbers = values["-ADD_ORDER_NUMBER_INPUT-"]
            order_input_model = values["-ADD_ORDER_MODEL_INPUT-"]
            order_combo_process = values["-ADD_ORDER_PROCESS_COMBO-"]

            numbers = order_input_numbers.replace(' ', '')
            numbers = numbers.split(',')
            numbers = delete_not_numbers(numbers)

            for number in numbers:
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
                                            text=None,
                                            key=f'-{number}_CHECKBOX_NUMBER-'
                                        ),
                                        sg.Text(
                                            text=f'{number}',
                                            size=(5,35),
                                            justification='center',
                                        ),
                                        sg.Text(
                                            text=f'{order_input_model}',
                                            size=(20,35),
                                            justification='center'
                                        ),
                                        sg.Text(
                                            text=f'{order_combo_process}',
                                            size=(12,35),
                                        )
                                    ]
                                ],
                                key=f'-INITIAL_TABLE_FRAME_{number}-'
                            )
                        ]
                    ]
                )
            
            add_window.hide()
            
        elif event == '-ADD_ORDER_CANCEL_BUTTON-' or event == None:
            add_window.hide()
            
    print(values)
    print(event)