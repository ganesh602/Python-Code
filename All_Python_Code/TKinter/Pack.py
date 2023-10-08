from tkinter import *

win = Tk()

win.title("Pack Label")

l1 = Label(win,bg="red",fg="yellow",text="Label 1")
l1.pack(side=LEFT,fill=Y)

l2 = Label(win,bg="red",fg="yellow",text="Label 2")
l2.pack(side=TOP,fill=X)

l3 = Label(win,bg="red",fg="yellow",text="Label 3")
l3.pack(side=LEFT)

l4 = Label(win,bg="red",fg="yellow",text="Label 4")
l4.pack(side=LEFT)

win.mainloop()