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
        self.desc = None

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

        Se asume que string termina con $
        """
        if self.leaf == True:
            string_sgte = file[self.index:self.index+len(string)-1]
            if string_sgte == string[:-1]:
                return [file[self.index:]]    
 
        else: 
            if j<= len(string)-2: # recursion   j >= len(string)-2
                current = string[j] # string actual a comparar
                for h in self.children:
                    if h.char == current: # si hace match el string actual con un char hijo
                        return h.search(string, file, j + h.length)   # sigue buscando en el hijo, actualizando el valor de j
   
            else: # estoy a medio camino, entonces sugiero los hijos, o en el nodo                                 j-self.length == len(string)-2: 
                my_children_desc = [h.desc for h in self.children]  # cantidad de descendientes de cada hijo
      
                order_children = [i[0] for i in sorted(enumerate(my_children_desc), key=lambda x:x[1], reverse = True)] # indices de hijos ordenados por cantidad de descendientes       
                some_desc = self.descendents([])[0] # tomo cualquier descendiente
            
                string_sgte = file[some_desc.index:some_desc.index+len(string)-1]
      
                if string_sgte == string[:-1]:
                    if len(my_children_desc)<3: # tiene menos de 3 hijos
                 
                        return [file[some_desc.index:some_desc.index+j]+ self.children[h_i].char for h_i in order_children]
                    else:
                        return [file[some_desc.index:some_desc.index+j] + self.children[h_i].char for h_i in order_children[:3]]
      

        return [] # no encuentra match en los hijos o j > |string|
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
            # print("este es el d : {} y el str_len: {}".format(d, len(str_leaf)))
            if d>=j-self.length: # si difieren en un d
                new_v = Node(self.char, d-(j -self.length)) # creo un nodo interno
                new_v.set_parent(self.parent) # el nuevo nodo tendrá como padre al padre del actual
                self.set_params(str_leaf[d], len(str_leaf)-d)
                self.parent.children.remove(self) # elimina su existencia en la lista de hijos del padre
                self.set_parent(new_v) # cambio al padre y le asigno hijo
                new_h = Node(str_in[d], len(str_in)-d, True, index) # creo un nuevo hijo
                new_h.set_parent(new_v) # seteo al padre y lo agrego como hijo
            else:
                # print("mi largo antes de search es " +str(self.length))
                node_vs,current_j = self.searchVs(j, d)
                # print("node vs char es:" + node_vs.char)
                new_v = Node(node_vs.char, d-(current_j - node_vs.length)) # creo un nodo interno
                new_v.set_parent(node_vs.parent) # el nuevo nodo tendrá como padre al padre del actual
                node_vs.set_params(str_leaf[d], node_vs.length - (d-(current_j - node_vs.length)))
                node_vs.parent.children.remove(node_vs) # elimina su existencia en la lista de hijos del padre
                node_vs.set_parent(new_v) # cambio al padre y le asigno hijo
                new_h = Node(str_in[d], len(str_in)-d, True, index) # creo un nuevo hijo
                new_h.set_parent(new_v) # seteo al padre y lo agrego como hijo
        else: #recorriendo el Patricia, nodo interno

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
                        self.set_params(file[self.descendents([])[0].index:][d], self.length- new_v.length)
                        self.set_parent(new_v)
                        new_h = Node(str_in[d], len(str_in)-d, True, index)
                        new_h.set_parent(new_v)
            else: # me paso en un nodo interno
        
                d = min([comparestr(file[s.index:], str_in) for s in self.descendents([])]) 
         
                new_v = Node(self.char, d-(j-self.length))
                new_v.set_parent(self.parent)
                self.parent.children.remove(self)
                self.set_params(file[self.descendents([])[0].index:][d], self.length- new_v.length)
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
        
        l = [1,2,4]
        if j-self.length <= d:
            
            return self, j
        return self.parent.searchVs(j-self.length, d)
    
    def setDesc(self):
        self.desc = len(self.descendents([]))
        

class PatriciaTree:
    def __init__(self, file):
        self.root = Node(None, 0)
        self.file = file
    
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
            return []
        else:
            return self.root.search(s, self.file)
    
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
        else: #llega a una
            print("index {}".format(node.index))
    
    def preprocessing(self, node):
        
        node.setDesc()
        if len(node.children) > 0:
            for i in node.children:
                self.preprocessing(i)

if __name__ == '__main__':
     archivo = open('../../frutas.txt', 'r').read()
     arbolP = PatriciaTree(archivo)
     for i in range(len(arbolP.file)):
#         # print("Agregando {} \n".format(i))
         arbolP.insert(i)
#         # arbolP.printTree(arbolP.root)
#         # print() 
#     # arbolP.insert(0)
#     # arbolP.insert(5)
#     arbolP.printTree(arbolP.root)
     arbolP.preprocessing(arbolP.root)
     print("BUSCANDO 'A_':")
     print(arbolP.search("A $"))


#     print("BUSCANDO 'A':")
#     print(arbolP.search("A$"))
#     print("BUSCANDO 'ANE':")
#     print(arbolP.search("ANE$"))
#     print("BUSCANDO 'ANANE':")
#     print(arbolP.search("ANANE$"))
#     print("BUSCANDO 'ANANA':")
#     print(arbolP.search("ANANA$"))
#     print("BUSCANDO 'N':")
#     print(arbolP.search("N$"))
#     print("BUSCANDO 'NE':")
#     print(arbolP.search("NE$"))

