from dataclasses import dataclass
import csv
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk
import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='A2022_jcardenas', password='A2022_jcardenas',
                                  host='db.inf.uct.cl',
                                  database='A2022_jcardenas')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cursor = cnx.cursor()

# Creamos clase padre


@dataclass
class Contenedores:
    contador = 0
    tipo__carga: str
    masaa: str
    kiloss: int

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo__carga = tipo_carga
        self.masaa = masa
        self.kiloss = kilos
        self.contador += 1

    def kilos(self):
        return self.kilos

    def tipo_carga(self):
        return self.tipo_carga

    def masa(self):
        return self.masa


@dataclass
class Vehiculos:
    Costoo: int
    Contenido: list

    def __init__(self, Costoo, Contenidoo):
        self.Costoo = Costo
        self.Contenidoo = Contenido


# ==========================================
# Creamos clases hijas


@dataclass
class Barco(Vehiculos):
    Capacidad = 0
    Capacidad += 1

    def todo(self):
        todo = f"costo: {Barco.Costo}", self.Contenido
        return todo


@dataclass
class Tren(Vehiculos):
    Capacidad = 0

    Capacidad += 1

    def todo(self):
        todo = f"costo: {Tren.Costo}", self.Contenido
        return todo


@dataclass
class Avion(Vehiculos):
    Capacidad = 0
    Capacidad += 1

    def todo(self):
        todo = f"costo: {Avion.Costo}", self.Contenido
        return todo


@dataclass
class Camion(Vehiculos):
    Capacidad = 0
    Capacidad += 1

    def todo(self):
        todo = f"costo: {Camion.Costo}", self.Contenido
        return todo


@dataclass
class Contenedor_P(Contenedores):
    tamaño: str = "pequeño"


@dataclass
class Contenedor_G(Contenedores):
    tamaño: str = "grande"

    def todo():
        todo = Contenedor_G.tamaño, Contenedor_G.tipo_carga, Contenedor_G.masa, Contenedor_G.kilos
        return

@dataclass
class Estanque_P(Contenedores):
    tamaño: str = "pequeño"


@dataclass
class Estanque_G(Contenedores):
    tamaño: str = "grande"


lista = []

add_product = ("INSERT INTO progra "
               "(id, nombre_Producto, tipo, masa, peso)"
               "VALUES (%(id)s, %(nombre_Producto)s, %(tipo)s, %(masa)s, %(peso)s)")


def leer():
    with open("ej2.csv") as f:
        reader = csv.reader(f, delimiter=",")
        # nos saltamos la primera linea
        next(reader, None)
        delete = 'delete from progra'
        cursor.execute(delete)
        for row in reader:
            data_product = {
                'id': int(row[0]),
                'nombre_Producto': row[1],
                'tipo': row[2],
                'masa': row[3],
                'peso': int(row[4])
            }
            cursor.execute(add_product, data_product)
            cnx.commit()
    # contarq = 'SELECT COUNT(DISTINCT nombre_Producto) FROM progra'
    # cursor.execute(contarq)
    # a = cursor.fetchall()
    # obj = [[] for i in range(int(a[0][0]))]
    # print(obj)

    # |  # |  # SELECT * FROM progra WHERE masa = 'gas' or masa = 'liquida', me muestra los liquidos y gases que deben ir separados
    # |  # |  # Quiza cambiar la variable contarq estaria bn
    # |  # |  # Recuerda que la clave esta en las query y fetchall(), es saber manipular la tabla


# Listas que contienen containers
container_normal = []
estanque_liquida = []
estanque_gas = []


def container():
    normalq = "select (sum(peso)/1000)/24000 from progra where masa = 'solida'"
    cursor.execute(normalq)
    p = cursor.fetchall()
    peso = float(p[0][0])
    int_p = int(peso)
    float_p = peso - int_p
    float_p = (float_p*peso)/100

    for e in range(int_p-1):
        C = Contenedor_G("normal", "solida", 24000)
        container_normal.append(C)
    if float_p < 11000:
        for e in range(1):
            C = Contenedor_P("normal", "solida", float_p)
        container_normal.append(C)
    else:
        for e in range(1):
            C = Contenedor_G("normal", "solida", float_p)
        container_normal.append(C)

    # print(container_normal)
    # print(len(container_normal))


def gas_liquido():
    peso_estanque = 22000
    # Conseguimos los nombres de todos los tipos de producto diferentes entre si
    p = 0
    prueba = "SELECT DISTINCT(nombre_Producto) FROM `progra` WHERE masa = 'liquida' or masa='gas'"
    cursor.execute(prueba)
    b = cursor.fetchall()
    # fetchall regresa una lista de tuplas
    for i in range(len(b)):
        # Recorremos la lista y despues conseguimos todos los valores con el nombre del producto
        query = f"SELECT * FROM `progra` WHERE nombre_Producto= '{b[i][0]}'"
        cursor.execute(query)
        fetchall = cursor.fetchall()
        for e in range(len(fetchall)):
            # Como se van creando diferentes listas, ya que estamos cambiando la variable 'query' el bucle
            # Necesitamos reiniciar el peso
            if e == 0:
                p = 0
            p += float(fetchall[e][4])
            tipo_de_carga = str(fetchall[e][2])
            masa = str(fetchall[e][3])
        if masa == 'gas':
            a = estanque_gas
        elif masa == 'liquida':
            a = estanque_liquida
        p /= 1000
        # Lo dividimos en el T. del container grande
        p /= 22000
        # Lo restante (0.algo), que siempre será menor a 1, entonces es fp<22000 que es un Con.G
        fp = p-int(p)
        Peso_pequenho = (fp*peso_estanque)/100
        p_int = int(p)
        for e in range(p_int):
            C = Estanque_G(tipo_de_carga, masa,peso_estanque)
            a.append(C)
        if Peso_pequenho < 11000:
            for e in range(1):
                C = Estanque_P(tipo_de_carga, masa, Peso_pequenho)
            a.append(C)
        else:
            for e in range(1):
                C = Estanque_G(tipo_de_carga, masa, Peso_pequenho)
            a.append(C)
    print(estanque_gas)
    print()
    print(estanque_liquida)
    print(len(estanque_gas))
    print(len(estanque_liquida))


leer()
container()
gas_liquido()
# transporte()
