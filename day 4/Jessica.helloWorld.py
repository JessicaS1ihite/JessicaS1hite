import PySimpleGUI as sg

layout = [
    [sg.Text("Hello World")]
]

window = sg.Window("Hello World", layout, margins=(100, 50))

window.read()
window.close()