import PySimpleGUI as sg

layout = [
    [sg.Button('Klik Saya')]
]

window = sg.Window('Contoh Program PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Klik Saya':
        sg.popup('Tombol diklik!')

window.close()