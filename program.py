from tkinter import *
root = Tk()
root.title("DataEntry")
root.geometry("300x200")
   

Label(text="Name").grid(row=0)
Label(text="Surname").grid(row=1)
Label(text="Contact Number").grid(row=2)

et1=Entry()
et1.grid(row=0,column=1)
et1.insert(0,"Wanwisa")

et2=Entry()
et2.grid(row=1,column=1)
et2.insert(0,"Waddington")

et3=Entry()
et3.grid(row=2,column=1)
et3.insert(0,"079x-xxx-xxx-x")

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

button = Button(text="Delete",command=deleteText).grid(row=3,column=1)

root.mainloop()