import tkinter as tk
window = tk.Tk()

def decerease():
    temp = int(lblCounter["text"]) #Cast the string into a variable, afer grabbing all the text inside lblCounter
    temp-=1
    lblCounter.configure(text=temp)

def increase():
    temp = int(lblCounter["text"]) #Cast the string into a variable, afer grabbing all the text inside lblCounter
    temp+=1
    lblCounter.configure(text=temp)

window.title("Counter")
window.geometry('50x50')

btnDecrease = tk.Button(window,text="-",command=decerease)
lblCounter = tk.Label(window,text="0")
btnIncrease = tk.Button(window,text="+",command=increase)

btnDecrease.grid(column=0,row=0)
btnIncrease.grid(column=2,row=0)
lblCounter.grid(column=1,row=0)



window.mainloop()