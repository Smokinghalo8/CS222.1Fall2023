import tkinter as tk
from tkinter.ttk import *

def submit():
    option = combo.get()    #Grabs the current optuoin selected inside of a combo box
    lbl["text"] = option

window = tk.Tk()


combo = Combobox(window)    #This is from tkinter.ttk! not tkinter!
combo['values'] = ("IN","CA","MA","MYballs")
btn = tk.Button(window,text="Submit", command=submit)
lbl = tk.Label(window)

combo.grid(column=0,row=0)
btn.grid(column=0,row=2)
lbl.grid(column=1,row=1)


window.mainloop()