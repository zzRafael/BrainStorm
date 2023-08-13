from random import randint
import PySimpleGUI as sg

items = ["Manage Catagorys", "Manage Items", "Edit Items", "Add Stock"]
width = max(map(len, items))

column1 = [[sg.Button(item, expand_x=True)] for item in items]

column2 = [[]]
for i, item in enumerate(items):
    column = []
    # Keep same width for all pages
    column.append([sg.Text(item, justification='center', background_color='green', size=width)])
    lines = randint(1, 10)
    for j in range(10):
        if j<lines:
            column.append([sg.Text(f'Element {j+1:0>2d}')])
        else:
            # Keep same height for all pages
            column.append([sg.Text("")])
    # Keep all pages in same row and only one visible
    column2[0].append(sg.Column(column, visible=(i==0), key=("Page", item)))

layout = [[sg.Column(column2), sg.VerticalSeparator(), sg.Column(column1, vertical_alignment='top')]]
window = sg.Window('Title', layout)
page = items[0]

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event in items:
        window[("Page", page)].update(visible=False)
        page = event
        window[("Page", page)].update(visible=True)

window.close() 