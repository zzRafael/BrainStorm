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
headings = ['Name', 'Size', 'Type']

sizes = ['Polimento', 'Cravando', 'Flash']
types = ['Rocky', 'Gaseous', 'Frozen', 'Desertic']

data_base = []

width, height = pyautogui.size()
print(width)
print(height)

frame_size = (width // 3, height - 200)

layout = [
    [
    sg.Frame('',[[sg.Text('UNISYSTEM')]], size = frame_size, expand_y = True),
    sg.Frame('',[[sg.Table(data_base,headings = headings,justification = 'left',max_col_width = 500,expand_x = True,expand_y = True,auto_size_columns = True,key = '_MAIN_TABLE_')]], size = frame_size, expand_y = True),
    sg.Frame('',[[sg.Text('Add new orders', key = '_STATUS_TEXT_')], [sg.Input(key = '_MAIN_INPUT_', do_not_clear = False)], [sg.Button('ADD', key = '_SUBMIT_BUTTON_')]], element_justification = 'center', size = frame_size, expand_y = True),
    ]]
sg.Input(())

sg.theme('DarkTeal9')
window = sg.Window('TEST WINDOW', layout, resizable=True, finalize=True)
window.Maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '_SUBMIT_BUTTON_':
        print('botao ok')
        size_ = choice(sizes)
        type_ = choice(types)
        name = values['_MAIN_INPUT_']
        data_base.append([f"{name}", size_, type_])
                
        window['_MAIN_TABLE_'].update(data_base)
        
        for data in data_base:
            if data[1] == 'Polimento':
                color = 'green'
            if data[1] == 'Cravando':
                color = 'yellow'
            if data[1] == 'Flash':
                color = 'red'

            window['_MAIN_TABLE_'].Update(row_colors = [[data_base.index(data), color]])
        
    print(f'EVENT: {event}\nVALUE: {values}')

