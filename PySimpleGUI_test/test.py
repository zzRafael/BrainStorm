import PySimpleGUI as psg

file=open("C:\\Users\\Personal\\Documents\\GitHub\\BrainStorm\\PySimpleGUI_test\\pedido_x.txt")
text=file.read()

psg.popup_scrolled(text, title="Scrolled Popup", font=("Arial Bold", 16), size=(50,10))

