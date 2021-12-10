from arbol_patricia import *
import requests
import os
from urllib.parse import urlparse
import pickle
import sys
import json
import urllib

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
# respuesta = request.GET.get('string')
# print(respuesta)

# https://docs.python-requests.org/en/latest/user/quickstart/

# https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python

# https://stackoverflow.com/questions/5074803/retrieving-parameters-from-a-url

# https://stackoverflow.com/questions/14468862/how-to-get-current-url-in-python-web-page
# parsed = urlparse(url) 
# print(urlparse.parse_qs(parsed.query)['string'])

# https://stackoverflow.com/questions/8709164/get-current-requested-url-in-python-without-a-framework

# recuperar el arbol
infile = open("tree.pkl",'rb')
arbolP = pickle.load(infile)
infile.close()

# variable de ambiente para recuperar el get HARDCODEADO
env_var = dict(os.environ)
string = env_var["QUERY_STRING"][7:]

#busco en el arbol
resp = arbolP.search(string.replace("%20", " "))
dic = {}
for i in range(len(resp)):
    dic[i] = resp[i]

 

mystatus = "200 OK"
sys.stdout.write("Status: %s\n" % mystatus)
sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n\n")
sys.stdout.write(json.dumps(dic))
