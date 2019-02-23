# created 01.06.2013 by Muhammadjon Hakimov
from turtle import *
import time
speed(50)
hideturtle()
x = 0
y = 300
for i in range(1):
    for i in range(0, 301,10):
        clear()
        up()
        goto(x, i)
        down()
        circle(10)
    for i in range(0, 301,10):
        clear()
        up()
        goto(i, y)
        down()
        circle(10)
    for i in range(300, -1, -10):
        clear()
        up()
        goto(y, i)
        down()
        circle(10)
    for i in range(300, -1, -10):
        clear()
        up()
        goto(i, x)
        down()
        circle(10)
mainloop()