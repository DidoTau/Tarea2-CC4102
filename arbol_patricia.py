
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
            Setea el indice del sufijo de una hoja 
        """
        self.parent = parent
    def set_params(self, char, l):
        """
            Cambia los valores de el char inicial y el largo en una bifurcación.

        """
        self.char = char
        self.length = l
    

    def add_child(self, son->Node):
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

class PatriciaTree:
    def __init__(self, filename):
        self.root = Node(None, None)
        self.file = open(filename, 'r')
    def insert(self, index, T):
        pass
    def search(self, node, s):
        """
        1. Caso base:ver que no es un arbol vacio
        2. Si no es vacio, busco en la raiz
        """
        if len(self.root.children) == 0: # si no tiene hijos, es un arbol vacio
            return False
        else:
            self.root.search(s, self.file)