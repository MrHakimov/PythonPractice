# author: Muhammadjon Hakimov
from random import randint
from sys import argv
try:
    k = int(argv[1])
except:
    k = 10

a = [randint(1,100) for x in range(k)]
a = list(set(a))

def merge(A,lo,hi):
    if lo < hi:
        m = int((lo+hi)/2)
        merge(a,lo,m)
        merge(a,m+1,hi)
        b = a[lo:m+1]
        c = a[m+1:hi+1]
        i = j = 0
        for k in range(lo,hi+1):
            if i < len(b)and (j == len(c) or b[i] < c[j]):
                a[k] = b[i]
                i = i + 1
            else:
                a[k] = c[j]
                j = j + 1

def merge_sort(a):
    merge(a,0,len(a)-1)

# def find_x(s,x):
#     j = len(s)-1
#     k = 0
#     r = "NIL"
#     while j > k:
#         if s[k]+s[j] == x:
#             r = (s[k],s[j])
#             break
#         elif s[k]+s[j] < x:
#             j = len(s)-1
#             k += 1
#         else:
#             j -= 1
#     return  r

def find_x(s,x,j,k=0):
    #j = len(s)-1
    #k = 0
    r = "NIL"
    if j > k:
        if s[k]+s[j] == x:
            r = (s[k],s[j])
            return r
        elif s[k]+s[j] < x:
            j = len(s)-1
            k += 1
        else:
            j -= 1
        r = find_x(s,x,j,k)
    return r

print('a1',a)
x = a[randint(0,len(a)-1)]
a = [a[i] for i in range(len(a)) if a[i] < x]
merge_sort(a)
print("*"*100)
print('x',x)
print("*"*100)
print('aS',a)
print("*"*100)
print(find_x(a,x,len(a)-1))


