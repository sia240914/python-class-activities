from tkinter import *
from datetime import date
window= Tk()

window.title("getting started with widgets")
window.geometry('300x300')
lb1=Label(text=" hey there",fg="#8D61B5",bg="white",height=5,width=10)

name_lb1=Label(text="enter your full name",bg="#BBB0FF")
name_entry=Entry()


def display():
    name=name_entry.get()
    global message
    message="welcome to this application \n todays date is "
    greet="hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=10)
button=Button(text="begin",fg="#5316C5",bg="white",command=display)

















lb1.pack()
name_lb1.pack()
name_entry.pack()
text_box.pack()
button.pack()



window.mainloop()
 


