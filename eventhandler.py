from tkinter import *
window=Tk()
window.title('event handler')

window.geometry('200x200')


def keypress(event):
    print(event.char)

window.bind("<Key>",keypress)

def click(event):
    print(" \n the button was clicked ")


button=Button(text="click me")
button.pack()

window.bind("<Button-1>",click)

window.mainloop()

