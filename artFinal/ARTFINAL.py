import tkinter as tk
import os
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("1100x550")
window.title("Art Final About Edo Period")


currectDirectory = os.getcwd()
file1Dir = currectDirectory+"\\artFinal\image1.jpg"
file2Dir = currectDirectory+"\\artFinal\image2.jpg"
file3Dir = currectDirectory+"\\artFinal\image3.jpg"
file4Dir = currectDirectory+"\\artFinal\image4.jpg"
file5Dir = currectDirectory+"\\artFinal\image5.jpg"
#file6Dir = currectDirectory+"\\artFinal\image6.jpg"    This will be the final slide that will have sources on it


def nextImage():
    tempString = image1["text"]
    tempInt = int(tempString)
    image1.configure(text=tempInt+1)
    match(tempInt):
        case 0:
            image1.configure(image=photo1)
            Descreiption.configure(text="Hey Everyone! This is an art project that I did\nafter thinking about what I should do for awhile!\nI hope you all enjoy and learn something!", justify="left")
        case 1:
            image1.configure(image=photo2)
            Descreiption.configure(text="Warriors normally would wear their armor on\nspecial occasions but would wear their sword always;\nWarriors from the Edo period would use weapons such as; Halberds,\nspears, katanas, swords, and bows - Even during a peaceful\ntime they needed a well armed militia. They also liked to practice\nhorsemanship and archery!", justify="left")
        case 2:
            image1.configure(image=photo3)
            Descreiption.configure(text="Had great political and economical growth during the Edo time\nand books/literature was also growing at this point in time!\nPaintings and artistic goods started being made.\nMore entertainment was being made during this time as well\nand care for the citizens was starting to become commonplace\nScenic landmarks started to be painted by artists that\nstarted to arise during this time.", justify="left")
        case 3:
            image1.configure(image=photo4)
            Descreiption.configure(text="Samurai armor is made of 14 parts;\n(Kabuto, Menpo, Shikoro, Nodowa, Do, Kusazuri, Sode, Kote,\nTekko, Haidate, Suneate, Kogake, and the Kegutsu)\neach part in the armor is detrimental to making the\narmor comfortable and protective.\nSilk, Bamboo, iron, gold and/or silver dust would all be\nused in the creation of the armor sets;\nEach set would also be made specifically\nfor a certain family or individual and would have a family symbol ornate\non the armor somewhere, most likely at the top of the helmet.", justify="left")
        case 4:
            image1.configure(image=photo5)
            Descreiption.configure(text="Samurai armor was mainly made by layering\ndifferent plates of steel or some other metal over themselves\nand tying them together with string or rope.\nEach of the different pieces of armor are vital\nand have importance to the armor as a whole.\nThere was a lot of movable parts in the samurai armor,\nmaking it easier for another to use them in a group.\nSome Samurai would also wear accessories to make them seem more\nfierce on the battlefield, and there is a specific order of putting\non samurai armorthat needs to be put on in that specific order,\nbecause if it isn’t, not all pieces would fit!", justify="left")
        case 5:
            Descreiption.configure(text="This is the end! You can go back if you want\nbut you've learned all there is to this as of now!",justify="left")
            image1.configure(text="4")
        case _:
            Descreiption.configure(text="Error found in nextImage Function babey")

def prevImage():
    tempString = image1["text"]
    tempInt = int(tempString)
    image1.configure(text=tempInt-1)
    match(tempInt):
        case 0:
            image1.configure(image=photo1)
            Descreiption.configure(text="Hey Everyone! This is an art project that I did\nafter thinking about what I should do for awhile!\nI hope you all enjoy and learn something!", justify="left")
        case 1:
            image1.configure(image=photo2)
            Descreiption.configure(text="Warriors normally would wear their armor on\nspecial occasions but would wear their sword always;\nWarriors from the Edo period would use weapons such as; Halberds,\nspears, katanas, swords, and bows - Even during a peaceful\ntime they needed a well armed militia. They also liked to practice\nhorsemanship and archery!", justify="left")
        case 2:
            image1.configure(image=photo3)
            Descreiption.configure(text="Had great political and economical growth during the Edo time\nand books/literature was also growing at this point in time!\nPaintings and artistic goods started being made.\nMore entertainment was being made during this time as well\nand care for the citizens was starting to become commonplace\nScenic landmarks started to be painted by artists that\nstarted to arise during this time.", justify="left")
        case 3:
            image1.configure(image=photo4)
            Descreiption.configure(text="Samurai armor is made of 14 parts;\n(Kabuto, Menpo, Shikoro, Nodowa, Do, Kusazuri, Sode, Kote,\nTekko, Haidate, Suneate, Kogake, and the Kegutsu)\neach part in the armor is detrimental to making the\narmor comfortable and protective.\nSilk, Bamboo, iron, gold and/or silver dust would all be\nused in the creation of the armor sets;\nEach set would also be made specifically\nfor a certain family or individual and would have a family symbol ornate\non the armor somewhere, most likely at the top of the helmet.", justify="left")
        case 4:
            image1.configure(image=photo5)
            Descreiption.configure(text="Samurai armor was mainly made by layering\ndifferent plates of steel or some other metal over themselves\nand tying them together with string or rope.\nEach of the different pieces of armor are vital\nand have importance to the armor as a whole.\nThere was a lot of movable parts in the samurai armor,\nmaking it easier for another to use them in a group.\nSome Samurai would also wear accessories to make them seem more\nfierce on the battlefield, and there is a specific order of putting\non samurai armorthat needs to be put on in that specific order,\nbecause if it isn’t, not all pieces would fit!", justify="left")
        case 5:
            Descreiption.configure(text="This is the end! You can go back if you want\nbut you've learned all there is to this as of now!",justify="left")
            image1.configure(text="4")
        case -1:
            Descreiption.configure(text="Error but is okay, dont go back on the main screen!")
            image1.configure(text="0")
        case _:
            Descreiption.configure(text="Error found in nextImage Function babey")




# Position text in frame
photo1 = ImageTk.PhotoImage(Image.open(file1Dir))
photo2 = ImageTk.PhotoImage(Image.open(file2Dir))
photo3 = ImageTk.PhotoImage(Image.open(file3Dir))
photo4 = ImageTk.PhotoImage(Image.open(file4Dir))
photo5 = ImageTk.PhotoImage(Image.open(file5Dir))
#photo6 = ImageTk.PhotoImage(Image.open(file6Dir))

image1 = tk.Label(window, image = photo1, text="1")
Descreiption = tk.Label(window, text="Hey Everyone! This is an art project that I did\nafter thinking about what I should do for awhile!\nI hope you all enjoy and learn something!", justify="left")
#"C:\Users\ethan\Documents\GitHub\CS222.1Fall2023\artFinal\image1.jpg"
button1 = tk.Button(window, text="Next Image", command=nextImage)
button2 = tk.Button(window, text="Previous Image", command=prevImage)

image1.grid(column=0,row=0)
Descreiption.grid(column=1, row=0)
button1.grid(column=0, row=2)
button2.grid(column=0,row=1)
                                                    
                                                    
window.mainloop()