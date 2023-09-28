import tkinter as tk

window = tk.Tk()
window.title("Calc")

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    FinishingLabel["text"]=num1+num2

FirstNumLabel = tk.Label(window,text="Enter the first Number")
entry1 = tk.Entry(window)
SecondNumLabel = tk.Label(window,text="Enter the second Number")
entry2 = tk.Entry(window)
buttonCalc = tk.Button(window, text="Calculate", command=calculate)

FinishingLabel = tk.Label(window, text="balls")

FirstNumLabel.grid(column=0,row=0)
SecondNumLabel.grid(column=0,row=1)
entry1.grid(column=1,row=0)
entry2.grid(column=1,row=1)
buttonCalc.grid(column=0,row=2)
FinishingLabel.grid(column=2,row=2)



window.mainloop()