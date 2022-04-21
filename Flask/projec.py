from PySimpleGUI import PySimpleGUI as sg

sg.theme('LightBrown13')

def janela():
  layout = [
    [sg.Text('Bem-Vindo')],
    [sg.Button('Entrar') , sg.Button('Sair')]
  ]
  window = sg.Window('Julio.py' , layout , size=(500 , 100) , element_justification='center' , finalize=True)
  window.read()
janela()