import tkinter as tk
window = tk.Tk()
window.title("Second Python GUI")
window.geometry('500x300')

Label1 = tk.Label(window, text="Ok")

Label1.grid(column=0,row=0)

txt = tk.Entry(window,width=10)
txt.grid(column=1,row=0)


def clicked():
    result = "Welcome to "+txt.get()
    Label1.configure(text=result)



button = tk.Button(window,text="Welcome", command=clicked)#Need to define this
button.grid(column=2,row=0)

window.mainloop()