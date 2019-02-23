# created 04.06.2013 by Muhammadjon Hakimov
#-*- coding:utf-8 -*-
from math import*
from tkinter import *
tk=Tk()
can=Canvas(tk)# , bg="LightBlue", width="1i", height=100, relief=SUNKEN)
can.pack(expand=1, fill=BOTH)
def delt():
    r = list(w["text"])
    r = r[:len(r)-1:]
    y=""
    for i in r:
        y+=i
    w["text"] = y
def wrt_tn():
    tn = "tan("
    wrt(tn)
def wrt_f():
    f="fact("
    wrt(f)
def wrt_sq():
    sq = "sqrt("
    wrt(sq)
def fact(n):
    if n != 1:
        n = n * factorial(n-1)
    return n
def wrt_st():
    st = "**"
    wrt(st)
def wrt_cs():
    cs = "cos("
    wrt(cs)
def wrt_lg():
    lg="(1/log(10))*log("
    wrt(lg)
def wrt_e():
    che = str(e)
    wrt(che)
def wrt_zs():
    zs = ")"
    wrt(zs)
def wrt_sn():
    sn = "sin("
    wrt(sn)
def wrt_ln():
    ln="ln("
    wrt(ln)
def wrt_pi():
    chpi = str(pi)
    wrt(chpi)
def wrt_os():
    os = "("
    wrt(os)

def wrt_ts():
    ts = "/"
    wrt(ts)
def wrt_zb():
    zb="X"
    wrt(zb)
def wrt_mn():
    mn = "-"
    wrt(mn)
def wrt_pl():
    pl = "+"
    wrt(pl)
def wrt_rn():
    rn = "9"
    wrt(rn)
def wrt_rsh():
    rsh = "6"
    wrt(rsh)
def wrt_rs():
    rs = "3"
    wrt(rs)
def wrt_br():
    try:
        s = w["text"]
        s = s.replace("X","*")
        '''s = s.replace("^","**")
        s = s.replace("√","sqrt(")
        a = list(s)
        f, f1, f2 = a.index("l"),a.index("o"),a.index("g")
        fs = a.index(")")
        fs1 = a.index("(")
        if f2>f1>f:
            a = a[f:fs1+1]+a[fs1+1:fs+1]
            b = ""
            for i in a[fs1+1:fs]:
                b+=i
            s = s.replace("log("+b+")","log("+b+")/log(10)")
        a = list(s)
        f, f1 = a.index("l"),a.index("n")
        fs = a.index(")")
        fs1 = a.index("(")
        print(a)
        if f1>f:
            a = a[f:fs1+1]+a[fs1+1:fs+1]
            b = ""
            for i in a[fs1+1:fs]:
                b+=i
            s = s.replace("ln("+b+")","log("+b+")")'''
        w["text"] = str(eval(s))
    except:
        w["fg"] = "red"
        w["text"]="Error!!!"
def wrt_rh():
    rh = "8"
    wrt(rh)
def wrt_rp():
    rp  = "5"
    wrt(rp)
def wrt_rd():
    rd = "2"
    wrt(rd)
def wrt_rnl():
    rnl = "0"
    wrt(rnl)

def wrt_rf():
    rf = "7"
    wrt(rf)
def wrt_rch():
    rch = "4"
    wrt(rch)
def wrt_ry():
    ry = "1"
    wrt(ry)
def wrt_rt():
    rt = "."
    wrt(rt)
def wrt(n):
    w["text"] += n# ["text"]
Button(can,text="<",command = delt,background="white",font=("Puriza",25), fg = "darkblue", height  = 0, width = 4).pack({"side":"right"})
w = Button(can)
w["width"] = 26
w["background"] = "LightBlue"
w["font"]=("Puriza",25)
w["height"] = 0
w["fg"] = "white"
w.pack()
md1 = Frame()
md1["background"]="black"
md1.pack({"side":"right", "fill":"y"})
Button(md1, text="tan", width=4,command=wrt_tn,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md1, text="!", width=4,command=wrt_f,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md1, text="^", width=4,command=wrt_st,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md1, text="√", width=4,command=wrt_sq,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
md2 = Frame()
md2["background"]="black"
md2.pack({"side":"right", "fill":"y"})
Button(md2, text="cos", width=4,command=wrt_cs,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md2, text="log", width=4,command=wrt_lg,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md2, text="e", width=4,command=wrt_e,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md2, text=")", width=4,command=wrt_zs,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
md3 = Frame()
md3["background"]="black"
md3.pack({"side":"right", "fill":"y"})
Button(md3, text="sin", width=4,command=wrt_sn,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md3, text="ln", width=4,command=wrt_ln,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md3, text="π", width=4,command=wrt_pi,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
Button(md3, text="(", width=4,command=wrt_os,background="darkblue",font=("Puriza",25),height = 0, fg = "white").pack()
m1 = Frame()
m1["background"]="black"
m1.pack({"side":"right", "fill":"y"})
Button(m1, text="/", width=4,command=wrt_ts,background="black",font=("Puriza",25),height = 0, fg = "white").pack()
Button(m1, text="X", width=4,command=wrt_zb,background="black",font=("Puriza",25),height = 0, fg = "white").pack()
Button(m1, text="-", width=4,command=wrt_mn,background="black",font=("Puriza",25),height = 0, fg = "white").pack()
Button(m1, text="+", width=4,command=wrt_pl,background="black",font=("Puriza",25),height = 0, fg = "white").pack()
m2 = Frame()
m2["background"]="black"
m2.pack({"side":"right", "fill":"y"})
Button(m2, text="9", width=4,command=wrt_rn,font=("Puriza",25),height = 0).pack()
Button(m2, text="6", width=4,command=wrt_rsh, font=("Puriza",25),height = 0).pack()
Button(m2, text="3", width=4,command=wrt_rs,font=("Puriza",25),height = 0).pack()
Button(m2, text="=", width=4,command=wrt_br,background="black",font=("Puriza",25),height = 0, fg = "white").pack()
m3 = Frame()
m3["background"]="black"
m3.pack({"side":"right", "fill":"y"})
Button(m3, text="8", width=4,command=wrt_rh,font=("Puriza",25),height = 0).pack()
Button(m3, text="5", width=4,command=wrt_rp,font=("Puriza",25),height = 0).pack()
Button(m3, text="2", width=4,command=wrt_rd,font=("Puriza",25),height = 0).pack()
Button(m3, text="0", width=4,command=wrt_rnl,font=("Puriza",25),height = 0).pack()
m4 = Frame()
m4["background"]="black"
m4.pack({"side":"right", "fill":"y"})
Button(m4, text="7", width=4,command=wrt_rf,font=("Puriza",25),height = 0).pack()
Button(m4, text="4", width=4,command=wrt_rch,font=("Puriza",25),height = 0).pack()
Button(m4, text="1", width=4,command=wrt_ry,font=("Puriza",25),height = 0).pack()
Button(m4, text=".", width=4,command=wrt_rt,font=("Puriza",25),height = 0).pack()
mainloop()