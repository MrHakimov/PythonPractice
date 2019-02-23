# author: Muhammadjon Hakimov
def multiply(a,b):
    c = [[0] * len(a[0]) for i in range(len(a))]
    n = len(a)
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c
a=[[1,2,3,4,0],[2,0,1,3,0],[1,1,2,0,0],[4,1,1,4,0],[0,0,0,0,0]]
b=[[1,0,1,2,0],[3,1,4,2,0],[0,2,3,1,0],[4,3,0,2,0],[0,0,0,0,0]]
print('A:')
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end = '\t')
    print()
print('B:')
for i in range(len(b)):
    for j in range(len(b[0])):
        print(b[i][j], end = '\t')
    print()
c = multiply(a, b)
print('C:')
for i in range(len(c)):
    for j in range(len(c[0])):
        print(c[i][j],end = '\t')
    print()
