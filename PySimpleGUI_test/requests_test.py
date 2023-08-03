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

def delete_not_numbers(list):

    counter_not_number = 0

    for item in list:
        if item.isnumeric() == False:
            counter_not_number += 1

    for i in range(counter_not_number):
        for item in list:
            if item.isnumeric() == False:
                numbers.remove(item)

    new_list = numbers

    return new_list

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '_SUBMIT_BUTTON_':
        number = values['_INPUT_NUMBER_']
        model = values['_INPUT_MODEL_']
        process  = values['_INPUT_PROCESS_']
        
        # MAKE THE STRING SPLITED WITH ',' OK;.
        print("Checking if orders are valid...")

        numbers = number.replace(' ', '')
        numbers = numbers.split(',')
        numbers = delete_not_numbers(numbers)

        for number in numbers:
            if number.isnumeric():
                # checking if name already exists 
                number_exists = False
                for data in data_base:
                    if number == data_base[data_base.index(data)][0]:
                        print(data_base[data_base.index(data)])
                        sg.popup(f'Pedido "{number}" já está cadastrado!', title='Atenção')
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
