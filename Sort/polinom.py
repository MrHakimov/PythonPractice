# author: Muhammadjon Hakimov
# -*- coding: utf-8 -*-
a = [1, 2, 3, 4, 5]
y1 = 0
x = 2
for i in range(len(a)-1, 0, -1):
    print('y1',a[i] + x * y1)
    y1 = a[i] + x * y1
print(y1)
y2 = 0
for i in range(len(a)-1, 0, -1):
    print('y2',(y2 + (x ** (i - 1) * a[i])))
    y2 = (y2 + (x ** (i - 1) * a[i]))

print(y2)
