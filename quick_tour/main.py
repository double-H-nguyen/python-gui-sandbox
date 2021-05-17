# last left off https://pysimplegui.readthedocs.io/en/latest/#the-window-designer

import PySimpleGUI as sg
# sg.theme_previewer()

sg.theme('darkgrey11')

print = sg.Print

for i in range(100):
    print(i)