from tkinter import *
import math
window= Tk()

window.title("getting started with widgets")
window.geometry('500x400')
lb1=Label(text=" hey there",fg="#8D61B5",bg="white",height=5,width=10)

name_lb1=Label(text="enter digit 1 ",bg="#C7C2E4")
name_entry1=Entry()
name_lb2=Label(text="enter digit 2",bg="#2C0FE6")
name_entry2=Entry()








def display():
    num1=float(name_entry1.get())
    num2=float(name_entry2.get())
    producter=(num1 * num2)
    global message
    message="the product of the two numbers is :",producter
    greet="hello "
    
    text_box.insert(END,greet)
    text_box.insert(END,message)
text_box=Text(height=10)
button=Button(text="answer",fg="#5316C5",bg="white",command=display)

lb1.pack()
name_lb1.pack()
name_entry1.pack()
name_lb2.pack()
name_entry2.pack()
text_box.pack()
button.pack()



window.mainloop()
 


