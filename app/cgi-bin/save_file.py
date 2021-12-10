import cgi
import cgitb
import os
import filetype
import sys
from arreglo_sufijos import *
from arbol_patricia import *
import pickle

sys.setrecursionlimit(3000)
cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()

fileobj = form['file']
filename = fileobj.filename
#guardar archivo
# open('media/' + filename , 'wb').write(fileobj.file.read())
#leo archivo
file = fileobj.file.read().decode('utf-8')
# arreglo de sufijos
n = len(file)
A = list(range(n))
A = estebanSort(A, 0, n-1, n, file)

# arbol patricia
arbolP = PatriciaTree(file)
for i in range(n):
    arbolP.insert(i)
# arbolP.printTree(arbolP.root)
arbolP.preprocessing(arbolP.root)
tree_pickle = open("tree.pkl", 'wb')
pickle.dump(arbolP, tree_pickle)
tree_pickle.close()

infile = open("tree.pkl",'rb')
arbolP_read = pickle.load(infile)
infile.close()
# arbolP_read.printTree(arbolP_read.root)
html = f'''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Buscador</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <link rel="stylesheet" href="../css/form.css">
  </head>
  <body>
    <form  class="decor" autocomplete="off" method="post" action="" enctype="multipart/form-data">
      <div class="form-left-decoration"></div>
      <div class="form-right-decoration"></div>
      <div class="circle"></div>
      <div class="form-inner">
        <h1>Busca en tu texto</h1>
        <input type="text" list="results" name="search" id="search" placeholder="Ingresa tu búsqueda">
         <datalist id="results">

         </datalist>
        <p id="log">No has buscado nada</p>
        
      </div>
    </form>
    <script src ="../js/arbol.js"></script>
  </body>
</html>
'''
if  fileobj.filename:
    print(html,file=utf8stdout)