import tkinter as tk
import threading
from tkinter import filedialog
from tkinter.constants import ACTIVE, CENTER
from State import State

state = State(None, None, '0.1')

def path_button_action():
    filetypes = (('Pliki .csv .txt', '.csv .txt'))
    file_path = filedialog.askopenfilename(title='Otwórz', filetypes=filetypes)
    state.update_path(str(file_path))

def output_button_action():
    output_path = filedialog.askdirectory()
    print(output_path)
    state.update_output(str(output_path))

def exit_button_action():
    import sys
    sys.exit(root)


def quarter_roll_button_action():
    from Validate import Validate
    validate = Validate(state.path, state.output_path, 'Q')
    validate.validation()

def monthly_roll_button_action():
    from Validate import Validate
    validate = Validate(state.path, state.output_path, 'M')
    validate.validation()

def daily_roll_button_action():
    from Validate import Validate
    validate = Validate(state.path, state.output_path, 'D')
    validate.validation()


root = tk.Tk()
root.geometry('600x400')
root.title('Konwerter rolowań')

path_button = tk.Button(root, text='Wybierz plik', command=path_button_action)
path_button.pack()
path_button.place(relx=0.5,rely=0.3,anchor=CENTER)

output_button = tk.Button(root, text='Wybierz ściezkę wyjścia', command=output_button_action)
output_button.pack()
output_button.place(relx=0.5,rely=0.37,anchor=CENTER)



quarter_roll_button = tk.Button(root, text='Wykres rolowania kwartału', command=quarter_roll_button_action)
quarter_roll_button.pack()
quarter_roll_button.place(relx=0.5,rely=0.5,anchor=CENTER)
quarter_roll_button.configure(state=ACTIVE)
monthly_roll_button = tk.Button(root, text='Wykres rolowania miesiąca', command=monthly_roll_button_action)
monthly_roll_button.pack()
monthly_roll_button.place(relx=0.5,rely=0.57,anchor=CENTER)
monthly_roll_button.configure(state=ACTIVE)
daily_roll_button = tk.Button(root, text='Wykres rolowania dzienny (OPEN_INT)', command=daily_roll_button_action)
daily_roll_button.pack()
daily_roll_button.place(relx=0.5,rely=0.64,anchor=CENTER)
daily_roll_button.configure(state=ACTIVE)

exit_button = tk.Button(root, height=1, width=20, text='Wyjdź', command=exit_button_action)
exit_button.pack()
exit_button.place(relx=0.5,rely=0.8,anchor=CENTER)
exit_button.configure(state=ACTIVE)

version_button = tk.Button(root, text='Wersja')
version_button.pack()
version_button.place(relx=0.9,rely=0.9,anchor=CENTER)
version_button.configure(state=ACTIVE)



root.mainloop()




