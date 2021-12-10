import os
import pickle
import sys
import json

from arreglo_sufijos import *



utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

# recuperar la lista
infile = open("suff_list.pkl",'rb')
A = pickle.load(infile)
infile.close()

# variable de ambiente para recuperar el get HARDCODEADO
env_var = dict(os.environ)
string = env_var["QUERY_STRING"][7:][:-1]

#busco en el arr de sufijos
f, resp= A.searchSuffix(string.replace("%20", " "))

#eliminar duplicados

resp = list(set(resp))
dic = {}
for i in range(len(resp)):
    dic[i] = resp[i][:-1]

 

mystatus = "200 OK"
sys.stdout.write("Status: %s\n" % mystatus)
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n\n")
sys.stdout.write(json.dumps(dic))
