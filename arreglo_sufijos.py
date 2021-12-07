import numpy as np 
import math


def estebanSort(A, first, last):
    i = first
    j = last 
    pivot = A[math.ceil((i+j)/2)]

    while i < j:
        while T[A[i]:n] < T[pivot:n]:
            i+=1
        while T[A[j]:n]> T[pivot:n]:
            j-=1
        if i<=j: 
            s = A[j]
            A[j] = A[i]
            A[i] = s
            i+=1
            j-=1
    if first < j:
        estebanSort(A, first, j)
    if last > i:
        estebanSort(A, i, last)
    return A 

def ocurrenceLine(index):
    for i in range(index, n):
        if T[i] == "\n":
            return i 

def searchSuffix(s):
    c = 0
    for i in A: 
        if T[i:n].startswith(s):
            c+=1
            print(T[i:ocurrenceLine(i)])
    return c


if __name__ == '__main__':
    print("Hermanite ingresa el archivo: ")
    inp =  input()
    T = open(inp, 'r')
    T = T.read()
    print("Hermanite, me mandaste esto:\n {}".format(T))
    n = len(T)
    A = list(range(n))
    A = estebanSort(A, 0, n-1)
    print("Pana mio, vota Boric, este es tu arreglo de sufijos bien progre: \n {}".format(A))

    print("Buscate algguna weaita po : \n")
    busqueda = input()
    c = searchSuffix(busqueda)
    print("{} aparece {} veces \n".format(busqueda, c))
