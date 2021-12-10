import os
import pickle
import sys
import json

from arbol_patricia import *



utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

# recuperar el arbol
infile = open("tree.pkl",'rb')
arbolP = pickle.load(infile)
infile.close()

# variable de ambiente para recuperar el get HARDCODEADO
env_var = dict(os.environ)
string = env_var["QUERY_STRING"][7:]

#busco en el arbol
resp = arbolP.search(string.replace("%20", " "))
resp = list(set(resp))
dic = {}
for i in range(len(resp)):
    dic[i] = resp[i]

 

mystatus = "200 OK"
sys.stdout.write("Status: %s\n" % mystatus)
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n\n")
sys.stdout.write(json.dumps(dic))
