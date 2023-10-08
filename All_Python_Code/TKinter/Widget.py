from tkinter import *

win = Tk()

win.title('Widget')
win.geometry('800x800+100+100')

##  Label:
l = Label(win,text='Sample Label Widget.')
l['bg'] = 'red'
l['fg'] = 'white'
l.pack()

##  Button:
b = Button(win,text='Button.')
b.pack()

##  TextEntry :
e = Entry(win)
e.pack()

##  MultiLine Text :
t = Text(win,width=30,height=10)
t.pack()

##  CheckBox :
b = Checkbutton(win,text='Yes')
b.pack()

print('')

##  Radio Button :
v1 = IntVar()
r1 = Radiobutton(win,text='Option1',variable=v1,value=1)
r1.pack()
r2 = Radiobutton(win,text='Option2',variable=v1,value=2)
r2.pack()
r3 = Radiobutton(win,text='Option3',variable=v1,value=3)
r3.pack()

##  Option Menu :
opt = StringVar()
o = OptionMenu(win,opt,'Python','Java','C++','C')   #*('Java','C++','C'))
o.pack()

##  Scale Bar :
s = Scale(win, from_=0 , to=100)
s.pack()

win.mainloop()