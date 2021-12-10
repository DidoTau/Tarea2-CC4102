import numpy as np 
import math

class SuffixArray:
    def __init__(self, file):
        self.file = file
        self.n = len(file)
        self.arr = list(range(self.n))
        self.estebanSort(0, self.n-1)
    def estebanSort(self, first, last):
        i = first
        j = last 
        pivot = self.arr[math.ceil((i+j)/2)]

        while i < j:
            while self.file[self.arr[i]:] < self.file[pivot:]:
                i+=1
            while self.file[self.arr[j]:]> self.file[pivot:]:
                j-=1
            if i<=j: 
                s = self.arr[j]
                self.arr[j] = self.arr[i]
                self.arr[i] = s
                i+=1
                j-=1
        if first < j:
            self.estebanSort( first, j)
        if last > i:
            self.estebanSort(i, last)
        

    def ocurrenceLine(self, index):
        for i in range(index, self.n):
            if self.file[i] == "\n":
                return i 

    def searchSuffix(self,s):
        f = 0
        arr_occ = []
        for i in self.arr: 
            if self.file[i:self.n].startswith(s):
                f+=1
                arr_occ.append(self.file[i:self.ocurrenceLine(i)])
        return f, arr_occ
    def getArr(self):
        return self.arr


# if __name__ == '__main__':
#     print("Hermanite ingresa el archivo: ")
#     inp =  input()
#     T = open(inp, 'r')
#     T = T.read()
#     print("Hermanite, me mandaste esto:\n {}".format(T))
#     n = len(T)
#     A = list(range(n))
#     A = estebanSort(A, 0, n-1)
#     print("Pana mio, vota Boric, este es tu arreglo de sufijos bien progre: \n {}".format(A))

#     print("Buscate algguna weaita po : \n")
#     busqueda = input()
#     c = searchSuffix(busqueda)
#     print("{} aparece {} veces \n".format(busqueda, c))
