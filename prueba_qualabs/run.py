
from flask import Flask, jsonify
import json

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


# 1. Crear una lista con todas las variables (diccionarios)
# que contienen la info de los archivos json cargados.
users = user_zero, user_one, user_two, user_three, user_four, user_five, user_six,\
    user_seven, user_eight, user_nine, user_ten, user_eleven, user_twelve,\
    user_thirteen, user_fourteen, user_fiveteen, user_sixteen, user_seventeen,\
    user_eighteen, user_nineteen

# Endpoint para mostrar los resultados 
@app.route("/parteA")
def ParteA():
    """
    No conozco ningún método python para leer el nombre del archivo
    que es cargado, lo quepuedo hacer es leer el atributo "name" que es
    bastante similar.
    """

    # 1. Crear arrays para almacenar los usuarios de cada authn_provider
    authn_provider_1 = []
    authn_provider_2 = []
    authn_provider_3 = []
    authn_provider_4 = []
    
    # 2.1 Hacer un for para ver que authn_provider tiene cada elemento,
    # luego almaceno el name del usuario relacionado con ese authn_provider.
    
    for i in users:
        if i["provider"]["auth_module"] == "authn.provider_1":
            authn_provider_1.append(i["name"])
        elif i["provider"]["auth_module"] == "authn.provider_2":
            authn_provider_2.append(i["name"])
        elif i["provider"]["auth_module"] == "authn.provider_3":
            authn_provider_3.append(i["name"])
        else:
            authn_provider_4.append(i["name"])
    
    # 2.2 Serializar los elementos de cada lista.
    authn_provider_1 = json.dumps(authn_provider_1)
    authn_provider_2 = json.dumps(authn_provider_2)
    authn_provider_3 = json.dumps(authn_provider_3)
    authn_provider_4 = json.dumps(authn_provider_4)

    # 2.3 grupar las listas creadas en una lista mayor "auth_module" como se pide.
    auth_module = []
    for x in (authn_provider_1, authn_provider_2, authn_provider_3, authn_provider_4):
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

    authz_provider_1 = json.dumps(authz_provider_1)
    authz_provider_2 = json.dumps(authz_provider_2)
    authz_provider_3 = json.dumps(authz_provider_3)
    authz_provider_4 = json.dumps(authz_provider_4)

    content_module = []
    for x in (authz_provider_1, authz_provider_2, authz_provider_3, authz_provider_4):
        content_module.append(x)    
    
    """
    Tuve problemas con los formatos de serializacion JSON de python, por lo que no logré
    que se muestre el "nombre" de las variables (lsitas). Sólo se muestran los valores,
    pero de manera correcta, dentro de sus variables correspondientes. Se puede verificar
    en la pestaña "datos sin procesar".
    """
    return jsonify(auth_module, content_module)


@app.route("/parteB")
def ParteB():
    
    # Crear un array para almacenar el conjunto de usuarios
    usuarios = []
    # Crear un array para almacenar los modulos que ya se hayan leído, sin repetirse.
    modules = []

    """
    1. Hacer un for para leer cada elemento.
    2. Dentro del for va a comparar cada elemento con "modules" para verificar si
    el elemento ya se leyó. En un principio el array va a recibir los elementos 
    (porque esta vacío) pero a medida que va leyendo el resto del array los va
    ignorando porque ya se agregaron.
    3. Si no existe el elemento en "modules" va a agregar el "name" del usuario a
    "usuarios". De esta manera van a quedar en "usuarios" la cantidad mínima
    de usuarios que usen todos los módulos sin repetirse.
    """
    for i in users:
        if (i["provider"]["content_module"] not in modules) and (i["provider"]["auth_module"] not in modules):
            modules.append(i["provider"]["content_module"])
            modules.append(i["provider"]["auth_module"])
            usuarios.append(i["name"])

    usuarios = json.dumps(usuarios)

    return jsonify(usuarios)


if __name__ == "__main__":
    app.debug = True
    app.run (host='0.0.0.0', port=8000)
