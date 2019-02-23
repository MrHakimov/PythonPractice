# author: Muhammadjon Hakimov
import random
def Insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]<key:
            A[i+1] = A[i]
            i-=1
        A[i+1]=key
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
