import PySimpleGUI as sg
from layouts import initial_window_layout, add_window_layout

def create_initial_window():
    sg.theme('Default1')
    return sg.Window(
        title='UniSystem', 
        element_justification='center', 
        resizable=True, 
        finalize=True, 
        layout=initial_window_layout
    )

def create_add_window():
    sg.theme('Default1')
    return sg.Window(title='Adicione novos pedidos',
        element_justification='center',
        finalize=True,
        layout=add_window_layout
    )