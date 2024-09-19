# PySimpleGUIの省略形
import PySimpleGUI as sg

layout = [[sg.I('フタバ', k='in')], # I=Input, k=key
          [sg.B('実行', k='btn')], # B=Button
          [sg.T(k='txt')]] # T=Text
window = sg.Window('あいさつテスト', layout)

def execute():
    txt = 'こんにちは' + v['in'] + 'さん！'
    window['txt'].update(txt)

while True:
    e, v = window.read()
    if e == 'btn':
        execute()
    if e == None:
        break
window.close()