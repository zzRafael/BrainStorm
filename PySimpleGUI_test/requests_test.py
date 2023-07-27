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
headings = ['Name', 'Size', 'Type']

sizes = ['Small', 'Medium', 'Big']
types = ['Rocky', 'Gaseous', 'Frozen', 'Desertic']

data = []



layout = [
    [
    sg.Frame('',[[sg.Table(data,headings = headings,justification = 'left',max_col_width = 500,expand_x = True,expand_y = True,auto_size_columns = True,key = '_MAIN_TABLE_')]], expand_x=True, expand_y=True),
    sg.Frame('',[[sg.Text('TELA_1', key='_MAIN_TEXT_')], [sg.Input(key='_MAIN_INPUT_')], [sg.Button('Try', key='_MAIN_BUTTON_', expand_x = True)]], expand_x=True, expand_y=True)
    ]
]
    
window = sg.Window('TEST WINDOW', layout, resizable=True, finalize=True)


while True:
    window.Maximize()
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '_MAIN_BUTTON_':
        data.append([f"{values['_MAIN_INPUT_']}", choice(sizes),choice(types)])
        window['_MAIN_TEXT_'].update(f"{values['_MAIN_INPUT_']}")
        window['_MAIN_TABLE_'].update(data)
    print(f'EVENT: {event}\nVALUE: {values}')

