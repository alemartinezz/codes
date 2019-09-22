#!/usr/local/bin/python3.7

from flask import Flask, jsonify
import json
from collections import ChainMap

app = Flask(__name__)


# 0. Cargar los valores de los archivos en variables.
with open('./users/u0.json') as u0, \
        open('./users/u1.json', 'r') as u1, \
        open('./users/u2.json', 'r') as u2, \
        open('./users/u3.json', 'r') as u3, \
        open('./users/u4.json', 'r') as u4, \
        open('./users/u5.json', 'r') as u5, \
        open('./users/u6.json', 'r') as u6, \
        open('./users/u7.json', 'r') as u7, \
        open('./users/u8.json', 'r') as u8, \
        open('./users/u9.json', 'r') as u9, \
        open('./users/u10.json', 'r') as u10, \
        open('./users/u11.json', 'r') as u11, \
        open('./users/u12.json', 'r') as u12, \
        open('./users/u13.json', 'r') as u13, \
        open('./users/u14.json', 'r') as u14, \
        open('./users/u15.json', 'r') as u15, \
        open('./users/u16.json', 'r') as u16, \
        open('./users/u17.json', 'r') as u17, \
        open('./users/u18.json', 'r') as u18, \
        open('./users/u19.json', 'r') as u19:
    user_zero = json.load(u0)
    user_one = json.load(u1)
    user_two = json.load(u2)
    user_three = json.load(u3)
    user_four = json.load(u4)
    user_five = json.load(u5)
    user_six = json.load(u6)
    user_seven = json.load(u7)
    user_eight = json.load(u8)
    user_nine = json.load(u9)
    user_ten = json.load(u10)
    user_eleven = json.load(u11)
    user_twelve = json.load(u12)
    user_thirteen = json.load(u13)
    user_fourteen = json.load(u14)
    user_fiveteen = json.load(u15)
    user_sixteen = json.load(u16)
    user_seventeen = json.load(u17)
    user_eighteen = json.load(u18)
    user_nineteen = json.load(u19)


# 1. Crear una lista de diccionarios con todas las variables (diccionarios)
# que contienen la info de los archivos json cargados.
users = []
for x in [user_zero, user_one, user_two, user_three, user_four, user_five, user_six,
            user_seven, user_eight, user_nine, user_ten, user_eleven, user_twelve,
            user_thirteen, user_fourteen, user_fiveteen, user_sixteen, user_seventeen,
            user_eighteen, user_nineteen]:

    users.append(x)


# Endpoint para mostrar los resultados 
@app.route("/parteA")
def ParteA():
    
    # Crear arrays para cada authn_provider
    authn_provider_1 = []
    authn_provider_2 = []
    authn_provider_3 = []
    authn_provider_4 = []
    
    # 2.1 Hacer for para comparar cada elemento con la condicion para cada authn_provider,
    # luego almacenar el name del usuario en el que aparece en el array creado.
    for i in users:
        if i["provider"]["auth_module"] == "authn.provider_1":
            authn_provider_1.append(i["name"])
        elif i["provider"]["auth_module"] == "authn.provider_2":
            authn_provider_2.append(i["name"])
        elif i["provider"]["auth_module"] == "authn.provider_3":
            authn_provider_3.append(i["name"])
        else:
            authn_provider_4.append(i["name"])

    # 2.3 grupar los diccionarios en una nueva lista de diccionarios
    auth_module = []
    for x in [authn_provider_1, authn_provider_2, authn_provider_3, authn_provider_4]:
        auth_module.append(x)

    # 2.4 Hacer lo mismo para los authz_provider
    authz_provider_1 = []
    authz_provider_2 = []
    authz_provider_3 = []
    authz_provider_4 = []

    for i in users:
        if i["provider"]["content_module"] == "authz.provider_1":
            authz_provider_1.append(i["name"])
        elif i["provider"]["content_module"] == "authz.provider_2":
            authz_provider_2.append(i["name"])
        elif i["provider"]["content_module"] == "authz.provider_3":
            authz_provider_3.append(i["name"])
        else:
            authz_provider_4.append(i["name"])

    content_module = []
    for x in [authz_provider_1, authz_provider_2, authz_provider_3, authz_provider_4]:
        content_module.append(x)
    
    return jsonify(authn_provider_1)

if __name__ == "__main__":
    app.debug = True
    app.run (host='0.0.0.0', port=8000)