from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

window=Tk()
window.title('denomination counter')
window.configure(bg="light blue")
window.geometry('650x400')

upload=Image.open("download (2).jpeg")
upload=upload.resize((300,300))
img=ImageTk.PhotoImage(upload)

label=Label(window,bg="light blue",image=img)
label.place(x=180,y=20)
label1=Label(window,bg="light blue",text="hey user welcome to the denomination application")

label1.place(relx=0.5,y=340,anchor=CENTER)


def msg():

    msgbox=messagebox.showinfo("alert!!!","Do you want to calculate the denomination?")

    if msgbox=="ok":
        topwin()

button=Button(window,text="lets begin",command=msg,bg="brown",fg="white")
button.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.title("denomination calculator")
    top.geometry('600x450')
    top.configure(bg="light grey")

    label=Label(top,text="Enter total amount")
    entry=Entry(top)
    top.mainloop()
    
window.mainloop()





