from tkinter import *
from tkinter import messagebox

root=Tk()

root.title('virus has been detected')

root.geometry('200x200')

def msg():
    messagebox.showwarning("alert!!!,virus has been detected")

button=Button(root,text='scan',command=msg)
button.place(x=40,y=80)

root.mainloop()