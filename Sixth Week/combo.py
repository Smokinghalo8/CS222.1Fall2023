#drop down box baby

import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.geometry('500x300')
window.title("GUI three!")
combo = Combobox(window)    #This is from tkinter.ttk! not tkinter!
combo['values'] = ("IN","CA","MA","MYballs")
combo.current(3)
combo.grid(column=0,row=0)




window.mainloop()