from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfile

window=Tk()
window.title('text editor')
window.geometry('600x700')
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)


def openfile():
    filepath =askopenfilename(filetypes=[("Text Files","*.txt"),("All files","*.*")])

    if not filepath :
        return
    txt_edit.delete(1.0,END)

    with open(filepath,"r") as inputfile:
        text=inputfile.read()
        txt_edit.insert(END,text)
        inputfile.close()
    window.title(f"Codingal's text editor - {filepath}")


txt_edit=Text(window)
frbutton=Frame(window ,relief=RAISED,bd=2)
btnopen=Button(frbutton,text="Open",command=openfile)
btnsave=Button(frbutton,text="Save as")
btnopen.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btnsave.grid(row=1,column=0,sticky="ew",padx=5)
frbutton.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()




