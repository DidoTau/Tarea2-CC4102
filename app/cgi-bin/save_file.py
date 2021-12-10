import cgi
import cgitb

import sys
from arreglo_sufijos import *
from arbol_patricia import *
import pickle

sys.setrecursionlimit(5500000)
cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()

fileobj = form['file']
filename = fileobj.filename

file = fileobj.file.read().decode('utf-8')
# arreglo de sufijos
SA = SuffixArray(file)


# arbol patricia
arbolP = PatriciaTree(file)
for i in range(len(file)):
    arbolP.insert(i)
# arbolP.printTree(arbolP.root)
arbolP.preprocessing(arbolP.root)

# guardando arbol patricia
tree_pickle = open("tree.pkl", 'wb')
pickle.dump(arbolP, tree_pickle)
tree_pickle.close()

#guardando lista de sufijos
with open("suff_list.pkl", "wb") as fp:
    pickle.dump(SA, fp)


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
      <div class="form-inner">
        <h1>Busca un string en el arreglo de sufijos</h1>
        <input type="text" list="results_suf" name="search_suf" id="search_suf" placeholder="Ingresa tu búsqueda">
         <datalist id="results_suf">
         </datalist>
        <p id="log_suf">No has buscado nada</p>
        
      </div>
      <div class="circle"></div>
      <div class="form-inner">
        <h1>Busca un sufijo en el árbol</h1>
        <input type="text" list="results" name="search" id="search" placeholder="Ingresa tu búsqueda">
         <datalist id="results">
         </datalist>
        <p id="log">No has buscado nada</p>
        
      </div>
    </form>
    <script src ="../js/sufijo.js"></script>
    <script src ="../js/arbol.js"></script>
    
  </body>
</html>
'''
if  fileobj.filename:
    print(html,file=utf8stdout)