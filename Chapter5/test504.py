import PySimpleGUI as sg

savename = sg.popup_get_file('テキストファイルを選択してください。',
                             default_path='test.txt', save_as=True)
print(savename)