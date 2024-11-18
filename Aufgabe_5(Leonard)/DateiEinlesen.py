import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw()



def lese_datei_ohne_erste_zeile():
    datei_name = askopenfilename()
    with open(datei_name, 'r', encoding='utf-8') as datei:
        zeilen = datei.readlines()[1:]
    return zeilen


