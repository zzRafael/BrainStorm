import PySimpleGUI as sg
import os

# table layouts
initial_table_column_layout = [
    [
        sg.Frame(
            title='',
            expand_x=True,
            layout=[],
            key='-INITIAL_TABLE_FRAME-'
        )
    ]
]

# initial button column
initial_button_column_layout = [
    [
        sg.Button(
            button_text='Adicionar',
            key='-INITIAL_ADD_BUTTON-'
        )
    ]
]

initial_button_column_layout = [
    [
        sg.Button(
            button_text='Adicionar',
            key='-INITIAL_ADD_BUTTON-'
        )
    ]
]

initial_table_charge = [
    [
        sg.Frame(
            title='',
            expand_x=True,
            element_justification='center',
            layout=[
                [
                    sg.Text(text='          Pedido', expand_x=True),
                    sg.Text(text=' Modelo', expand_x=True),
                    sg.Text(text='Processo', expand_x=True)
                ]
            ]
        )
    ]
]

directory = os.chdir('data')
data_files = os.listdir(directory)

# first charge
for i in range(200):
    with open(data_files[i], 'r') as file:
        lines = file.readlines()
        print(lines)
        initial_table_charge.append(
        [
            sg.Frame(
                title='',
                size=(390,35),
                layout=[
                    [
                        sg.Checkbox(
                            text=None,
                            key=f'-{lines[0]}_CHECKBOX_NUMBER-'
                        ),
                        sg.Text(
                            text=f'{lines[0]}',
                            size=(5,35),
                            justification='center',
                        ),
                        sg.Text(
                            text=f'{lines[1]}',
                            size=(20,35),
                            justification='center'
                        ),
                        sg.Text(
                            text=f'{data_files[i]}',
                            size=(12,35),
                        )
                    ]
                ],
                key=f'-INITIAL_TABLE_FRAME_{lines[0]}-'
            )
        ])
    file.close()

directory = os.chdir('..')


# initial window layout
initial_window_layout = [
    # first line
    [
        sg.Column(
            size=(200, 600),
            layout=initial_button_column_layout,
            key='-INITIAL_BUTTON_COLUMN-'
        ),
        sg.Frame(
            title='',
            element_justification='center',
            layout=[
                [
                    sg.Column(
                        size=(400, 600),
                        scrollable=True,
                        vertical_scroll_only=True,
                        layout=initial_table_charge,
                        key='-INITIAL_TABLE_COLUMN-'
                    )
                ]
            ]
        )
    ]
]


# add window layout
add_window_layout = [
    # 1° row
    [
        sg.Text(
            text='Número do pedido: ',
            key='-ADD_ORDER_NUMBER_TEXT-'
        ),
        sg.Multiline(
            size=(20,3),
            default_text='',
            key='-ADD_ORDER_NUMBER_INPUT-',
            do_not_clear=False
        )
    ],
    # 2° row
    [
        sg.Text(
            text='Modelo do pedido: ',
            key='-ADD_ORDER_MODEL_TEXT-'
        ),
        sg.Input(
            default_text='',
            key='-ADD_ORDER_MODEL_INPUT-',
            do_not_clear=False
        )
    ],
    # 3° row
    [
        sg.Text(
            text='Processo atual do pedido: ',
            key='-ADD_ORDER_PROCESS_TEXT-'
        ),
        sg.Combo(
            values=['Fabricando', 'Gravação', 'Polimento'],
            default_value='Fabricando',
            key='-ADD_ORDER_PROCESS_COMBO-',
        )
    ],
    # 4° row
    [
        sg.Button(
            button_text='Adicionar',
            key='-ADD_ORDER_ADD_BUTTON-'
        ),
        sg.Button(
            button_text='Cancelar',
            key='-ADD_ORDER_CANCEL_BUTTON-'
        )
    ],
]