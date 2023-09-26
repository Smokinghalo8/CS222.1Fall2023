import tkinter as tk    #Popular package for User Interface

window = tk.Tk()
hello = tk.Label(text="Hello World")
welcome = tk.Label(text="Welcome to CS 222", foreground="white",background="black")
entry = tk.Entry()
button1 = tk.Button(text="Press me after you say something!",fg="white", bg="black")
name = entry.get()
intro = tk.Label(text="test_ "+name)
hello.pack() #packing the label made into the window
welcome.pack()
button1.pack()
entry.pack()
intro.pack()

window.mainloop()#basically starts up the window to get it showing - show function