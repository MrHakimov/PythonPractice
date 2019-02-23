# author: Muhammadjon Hakimov
import random
def Insertion_sort(A,n=1):
    if n < len(A):
        key=A[n]
        i=n-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
        n = n + 1
        Insertion_sort(A,n)
    return A

n=input("Количество элементов:")
n=int(n)
A=[]
for i in range(n):
    a=random.randint(1,50)
    A.append(a)
print(A)
print("="*30)
print(Insertion_sort(A))
