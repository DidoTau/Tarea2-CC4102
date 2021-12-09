from typing import Match
from utils import *

class Node:
    def __init__(self, char, length, leaf = False, index = None):
        self.children = [] # array de hijos
        self.index = index # índice de sufijo, solo para hojas
        self.parent = None # ref al padres
        self.leaf = leaf # booleano indica si es hoja, todos por defecto lo son
        self.char = char # char leído para llegar al nodo actual
        self.length = length # largo del string 

    def set_parent(self, parent):
        """
            Setea el el padre del nodo actual y lo agrega al padre
        """
        self.parent = parent # seteo el padre
        parent.add_child(self) # lo agrego como hijo
    def set_params(self, char, l):
        """
            Cambia los valores de el char inicial y el largo en una bifurcación.

        """
        self.char = char
        self.length = l
    

    def add_child(self, son):
        self.children.append(son)
    
    def search(self, string, file, j =0):
        """
        1. Caso base: si es una hoja-> compara el string con el sufijo de la hoja, retorna el sufijo si son iguales, False sino
        2. Es nodo interno:
        """
        if self.leaf == True:
            if string == file[self.index:len(file)-1]: # compara con el sufijo referido en la hoja
                return file[self.index:len(file)-1]
            else: 
                return False
        else: 
            if j < len(string):
                current = string[j] # string actual a comparar
                for h in self.children:
                    if h.char == current: # si hace match el string actual con un char hijo
                        h.search(string, file, j + h.length)   # sigue buscando en el hijo, actualizando el valor de j
        
            return False # no encuentra match en los hijos o j > |string|
    def insert(self, index, file, j = 0):
        """
        1. Caso base: si es una hoja:
                si d>d':
                    caso bonito
                else:
                    ninguna de las anteriores, caso feo
                    
        2. nodo interno 

                         
        """

        str_in = file[index:]
        if self.leaf == True: # caso base
            str_leaf = file[self.index:]
            d = comparestr(str_in, str_leaf) # compara el string ingresado con el de la hoja 
            print("este es el d : {} y el str_len: {}".format(d, len(str_leaf)))
            if d>=j-self.length: # si difieren en un d
                new_v = Node(self.char, d-(j -self.length)) # creo un nodo interno
                new_v.set_parent(self.parent) # el nuevo nodo tendrá como padre al padre del actual
                self.set_params(str_leaf[d], len(str_leaf)-d)
                self.parent.children.remove(self) # elimina su existencia en la lista de hijos del padre
                self.set_parent(new_v) # cambio al padre y le asigno hijo
                new_h = Node(str_in[d], len(str_in)-d, True, index) # creo un nuevo hijo
                new_h.set_parent(new_v) # seteo al padre y lo agrego como hijo
            else:
                print("mi largo antes de search es " +str(self.length))
                listilla = self.searchVs(j, d)
                print("esta huea es de tipo ", listilla)
                node_vs = listilla[0]
                current_j = listilla[1]
                new_v = Node(node_vs.char, node_vs.length-current_j-d) # creo un nodo interno
                new_v.set_parent(node_vs.parent) # el nuevo nodo tendrá como padre al padre del actual
                node_vs.set_params(str_leaf[d], len(str_leaf)-d)
                node_vs.parent.children.remove(node_vs) # elimina su existencia en la lista de hijos del padre
                node_vs.set_parent(new_v) # cambio al padre y le asigno hijo
                new_h = Node(str_in[d], len(str_in)-d, True, index) # creo un nuevo hijo
                new_h.set_parent(new_v) # seteo al padre y lo agrego como hijo
        else: #recorriendo el Patricia

            if j < len(str_in): # no me he pasado
                current = str_in[j] # string aindexctual a comparar
                # print("current: " + current)
                ix = [h for h in self.children if h.char == current] # busco indices con match con current char
                # print("match encontrados: "+ str(len(ix)))
                if len(ix) !=0: # hubo match
                    h =  ix[0] #hijo con match
                    h.insert(index, file, j+h.length) # sigo recorriendo
                else:
                    
                    d_arr = [comparestr(file[s.index:], str_in) for s in self.descendents([])]
                    # print(d_arr)
                    d = min(d_arr)  
                    # print("str_in= " +str_in)
                    if j == d:
             
                        child = Node(current, len(file)-index-j, True, index) 
                        child.set_parent(self) # seteo como padre de child y lo agrego como hijo de self, caso bonito j = d
                    else:
                        new_v = Node(self.char, d-(j-self.length))
                        new_v.set_parent(self.parent)
                        self.parent.children.remove(self)
                        self.set_params(file[self.descendents([])[0].index:][d], self.length- d-(j-self.length))
                        self.set_parent(new_v)
                        new_h = Node(str_in[d], len(str_in)-d+1, True, index)
                        new_h.set_parent(new_v)
            else: # me paso en un nodo interno
        
                d = min([comparestr(file[s.index:], str_in) for s in self.descendents([])])  
                new_v = Node(self.char, d-(j-self.length))
                new_v.set_parent(self.parent)
                self.parent.children.remove(self)
                self.set_params(file[self.descendents([])[0].index:][d], self.length- d-(j-self.length))
                self.set_parent(new_v)
                new_h = Node(str_in[d], len(str_in)-d, True, index)
                new_h.set_parent(new_v)
        
    def descendents(self, desc):
        # print("toy en descent: " + str(len(desc)))
        for h in self.children:
            if h.leaf ==True:
                desc.append(h)
                # print("estos son mis descendientes: " + str(h.index))
            h.descendents(desc)
        return desc

    def searchVs(self, j, d):
        print("j es {} y d es {} y mi largo {} ".format(j,d, self.length))
        l = [1,2,4]
        if j-self.length <= d:
            print("voy a retornar {}, {}".format(self.length,j))
            return l
        self.parent.searchVs(j-self.length, d)

class PatriciaTree:
    def __init__(self, filename):
        self.root = Node(None, 0)
        self.file = open(filename, 'r').read()
    
    def insert(self, index):
        """
        1. Caso base: ver que no es un arbol vacio
            -> es vacío: agrega el T[index]
        2. else: recorre como en búsqueda
        """
        if len(self.root.children) == 0:
            child = Node(self.file[index], len(self.file)-index,True, index) # creamos una hoja 
            child.set_parent(self.root)# agregamos este hijo a la raiz
        else: 
            self.root.insert(index, self.file)
    def search(self, s):
        """
        1. Caso base:ver que no es un arbol vacio
        2. Si no es vacio, busco en la raiz
        """
        if len(self.root.children) == 0: # si no tiene hijos, es un arbol vacio
            return False
        else:
            self.root.search(s, self.file)
    
    def printTree(self, node, l=0):
        """
        """
        print("Level ", l, " ", len(node.children), end=":\n")
        for i in node.children:
            print(" {}, {} ".format(i.char, i.length))
        l += 1
        if len(node.children) > 0:
            for i in node.children:
                self.printTree(i, l)
        else:
            print("index {}".format(node.index))
if __name__ == '__main__':
    archivo = 'frutas.txt'
    arbolP = PatriciaTree(archivo)
    for i in range(len(arbolP.file)):
        print("Agregando {} \n".format(i))
        arbolP.insert(i)
        arbolP.printTree(arbolP.root)
        print()
    # arbolP.insert(1)
    # arbolP.insert(5)
    arbolP.printTree(arbolP.root)
    # arbolP.printTree(arbolP.root)


"""
        root
    $,1 - 
"""