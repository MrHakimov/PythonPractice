# created 03.06.2013 by Muhammadjon Hakimov
from tkinter import*
import random
global a
a=[]
x=90
y=100
x1=''
x2=''
x3=''
x4=''
x5=''
x6=""
x7=""
x8='"'
x9=""
x10='"'
x11='"'
x12='"'
x13='"'
x14=''
x15=''
x16=''
x17=''
x18=''
x19=''
x20=''
x21=''
x22=''
x23=''
x24=''
x25=''
def change_text(g):
    can.delete("all")
    a.append("")
    for i in range(len(a)):
        can.delete("all")
        s=eval('x'+str(i+1))
        s=x+100
        for j in range(i+1):
            can.delete("all")
            s+=100
            t=can.create_text(s,y,text=".")
            can.tag_bind(t, "<1>", change_text)
tk=Tk()
can=Canvas(tk, bg="White", width="4i", height=300, relief=SUNKEN)
can.pack(expand=1, fill=BOTH)
t=can.create_text(x,y,text="Hello!")
can.tag_bind(t, "<1>", change_text)
mainloop()