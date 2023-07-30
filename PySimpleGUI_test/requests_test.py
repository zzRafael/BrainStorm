'''import PySimpleGUI as sg
import random

headings = ['Name', 'Size', 'Type']

names = ['Aurora', 'Kepler - JC2', 'Proxima B', 'Sigmon', 'Monjo - 62', 'Gerdalt']
sizes = ['Small', 'Medium', 'Big']
types = ['Aquatic', 'Rocky', 'Gaseous', 'Frozen', 'Desertic']

data = []

number_of_planets = 1200

for i in range(number_of_planets):
    data.append([random.choice(names), random.choice(sizes),random.choice(types)])

layout = [
    [sg.Table(
    data,
    headings = headings,
    justification = 'right',
    max_col_width =500,
    expand_x = True,
    expand_y = True,
    auto_size_columns = True
    ),
    sg.Table(
    data,
    headings = headings,
    justification = 'right',
    max_col_width =500,
    expand_x = True,
    expand_y = True,
    auto_size_columns = True,
    ),
    sg.Table(
    data,
    headings = headings,
    justification = 'right',
    max_col_width =500,
    expand_x = True,
    expand_y = True,
    auto_size_columns = True,
    )]
    ]

window = sg.Window('Table', layout, resizable=True).finalize()
window.Maximize()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break'''


import PySimpleGUI as sg
from random import choice
import pyautogui
headings = ['Number', 'Model', 'Process']

processes = ['Flash', 'Polimento', 'Gravando', 'Black', 'Cravando']

data_base = []

width, height = pyautogui.size()
print(width)
print(height)

frame_size = (width // 3, height - 200)

layout = [
    [
    sg.Frame('',[[sg.Text('UNISYSTEM')]], size = frame_size, expand_y = True),
    sg.Frame('',[[sg.Table(data_base,headings = headings,justification = 'left',max_col_width = 500,expand_x = True,expand_y = True,auto_size_columns = True,key = '_MAIN_TABLE_')]], size = frame_size, expand_y = True),
    sg.Frame('',[[sg.Text('Add new orders', key = '_TITLE_', text_color='white')], [sg.Text('Order number: '), sg.Input(key = '_INPUT_NUMBER_', do_not_clear = False)], [sg.Text('Model name:  '), sg.Input(key = '_INPUT_MODEL_', do_not_clear = False)], [sg.Combo(key = '_INPUT_PROCESS_', default_value = 'Produzindo', values = processes)], [sg.Button('ADD', key = '_SUBMIT_BUTTON_')]], element_justification = 'center', size = frame_size, expand_y = True),
    ]
    ]
sg.Input(())

sg.theme('default1')
window = sg.Window('TEST WINDOW', layout, resizable=True, finalize=True)
window.Maximize()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '_SUBMIT_BUTTON_':
        number = values['_INPUT_NUMBER_']
        model = values['_INPUT_MODEL_']
        process  = values['_INPUT_PROCESS_']
        
        if number.isnumeric():
            # checking if name already exists 
            number_exists = False
            for data in data_base:
                if number == data_base[data_base.index(data)][0]:
                    print(data_base[data_base.index(data)])
                    window['_TITLE_'].update('Order already exists!', text_color='red')
                    number_exists = True

            if number_exists:
                pass
            else:
                order = [number, model, process]
                
                data_base.append(order)

                window['_MAIN_TABLE_'].update(data_base)

                window['_TITLE_'].update(f'Order {number} has been added', text_color='white')

                '''for data in data_base:
                    if data.process == processes[0]:
                        color = 'green'
                    elif data.process == processes[1]:
                        color = 'blue'
                    elif data.process == processes[2]:
                        color = 'pink'
                    else:
                        color = 'yellow'
                
                    

                    window['_MAIN_TABLE_'].Update(row_colors = [[data_base.index(data), color]])'''
        else:
            window['_TITLE_'].update('This order is not a valid number', text_color='red')

    print(f'EVENT: {event}\nVALUE: {values}')
