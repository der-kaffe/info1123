from dataclasses import dataclass
import csv
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk
# Creamos clase padre


@dataclass
class Contenedores:
    contador = 0
    nombree: str
    tipo__carga: str
    masaa: str
    kiloss: int

    def __init__(self, nombree, tipo_carga, masa, kilos):
        self.nombree = nombre
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
    contadorCP: int = 0
    contadorCP += 1

    def cantidad():
        return Contenedor_P.contadorCP


@dataclass
class Contenedor_G(Contenedores):
    tamaño: str = "grande"
    contadorCG: int = 0
    contadorCG += 1

    def todo():
        todo = Contenedor_G.tamaño, Contenedor_G.tipo_carga, Contenedor_G.masa, Contenedor_G.kilos
        return

    def cantidad():
        return Contenedor_G.contadorCG


@dataclass
class Estanque_P(Contenedores):
    tamaño: str = "pequeño"
    contadorEP: int = 0
    contadorEP += 1

    def cantidad():
        return Estanque_P.contadorEP


@dataclass
class Estanque_G(Contenedores):
    tamaño: str = "grande"
    contadorEG: int = 0
    contadorEG += 1

    def cantidad():
        return Estanque_G.contadorEG


lista = []


def leer():
    with open("ejemplo_lista.csv") as f:
        reader = csv.reader(f, delimiter=";")
        # nos saltamos la primera linea
        next(reader, None)
        for row in reader:
            lista.append(row)


# Listas que contienen containers
normal_solida = []
estanque_liquida = []
estanque_gas = []
inflamable = []

C_all = []


def container():
    x = ""
    y = ""
    here = 0
    for i in range(9):
        # Daremos 9 vueltas en donde a sera una lista diferente dependiendo de la masa
        # Y x,y seran el tipo de carga, masa, respectivamente

        if i == 0:
            x = "normal"
            y = "solida"
            a = normal_solida
            peso = 24000
        if i == 1:
            x = "normal"
            y = "liquida"
            a = estanque_liquida
        if i == 2:
            x = "normal"
            y = "gas"
            a = estanque_gas
        if i == 3:
            x = "refrigerado"
            y = "solida"
            a = normal_solida
            peso = 20000
        if i == 4:
            x = "refrigerado"
            y = "liquida"
            a = estanque_liquida
        if i == 5:
            x = "refrigerado"
            y = "gas"
            a = estanque_gas
        if i == 6:
            x = "inflamable"
            y = "solida"
            a = normal_solida
            peso = 22000
        if i == 7:
            x = "inflamable"
            y = "liquida"
            a = estanque_liquida
        if i == 8:
            x = "inflamable"
            y = "gas"
            a = estanque_gas
        # p es el peso total dependiendo de el tipo de carga y la masa
        p = 0
        nombre = ""
        for h in range(len(lista)):
            if lista[h][2] == x and lista[h][3] == y:
                p += int(lista[h][4])
                nombre = str(lista[h][1])
                print(
                    nombre, (f"|||| peso <=- {p} |||| tipo <=- {x} |||| masa <=- {y}"))
    # Lo pasamos a tonelada
        p /= 1000
        # Lo dividimos en el T. del container grande
        p /= peso
        # Lo restante (0.algo), que siempre será menor a 1, entonces es fp<24000 que es un Con.G
        fp = p-int(p)
        Peso_pequenho = (fp*peso)/100
        p = int(p)
        # Creamos los objetos containers y lo ponemos en su lista correspondiente
        if i == 0:
            for e in range(p-1):
                C = Contenedor_G(nombre, x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Contenedor_P(nombre, x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(nombre, x, y, Peso_pequenho)
                a.append(C)
        elif i == 1 or i == 2:
            for e in range(p-1):
                C = Estanque_G(nombre, x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Estanque_P(nombre, x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(nombre, x, y, Peso_pequenho)
                a.append(C)
        elif i == 3:
            for e in range(p-1):
                C = Contenedor_G(nombre, x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Contenedor_P(nombre, x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(nombre, x, y, Peso_pequenho)
                a.append(C)
        elif i == 4 or i == 5:
            for e in range(p-1):
                C = Estanque_G(nombre, x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Estanque_P(nombre, x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(nombre, x, y, Peso_pequenho)
                a.append(C)
        elif i == 6:
            for e in range(p-1):
                C = Contenedor_G(nombre, x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Contenedor_P(nombre, x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(nombre, x, y, Peso_pequenho)
                a.append(C)
        elif i == 7 or i == 8:
            for e in range(p-1):
                C = Estanque_G(nombre, x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Estanque_P(nombre, x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(nombre, x, y, Peso_pequenho)
                a.append(C)
    # print(len(normal_solida), "<- normal")
    # print(len(estanque_liquida), "<-  Estanque_Li")
    # print(len(estanque_gas), "<- Estanque_Gas")
    # print(len(inflamable), "<- Inflamable")

    # for i in range(len(normal_solida)):
    # print(normal_solida[i])


# Listas de Vehiculos
barcos = []
trenes = []
aviones = []
camiones = []


def transporte():
    # Creamos una lista con  todos los containers en orden
    total = (normal_solida) + (estanque_liquida) + (estanque_gas)
    prueba = []
    # Iteramos toda la lista total y lo añadimos a la lista prueba, si resulta que hay un total de X elementos correspondiente
    # A la cantidad maxima posible de containers que permite el vehiculo creamos un objeto que contenga la lista de containers
    for i in range(len(total)):
        prueba.append(total[i])
        if len(prueba) == 24000:
            T = Barco(1000000000, prueba)
            barcos.append(T)
            # Se vacía la lista para que repetir el ciclo correctamente
            prueba = []
            # Lo mismo con Capacidad
            Barco.Capacidad = 0
    # Como el if anterior no se cumplió seguramente la lista prueba quedará con items adentro que tienen que ser vaciados
    prueba = []
    # La lista TOTAL sigue siendo la misma apesar de que subimos los containers al vehiculo
    # Si que simplemente los eliminamos
    if len(barcos) >= 1:
        for i in range(len(barcos)*24000):
            total.pop(0)
    # Repetimos para los demás vehiculos
    for i in range(len(total)):
        if Tren.Capacidad < 250:
            prueba.append(total[i])
            if len(prueba) == 250:
                T = Tren(10000000, prueba)
                trenes.append(T)
                prueba = []
                Tren.Capacidad = 0
    prueba = []

    if len(trenes) >= 1:
        for i in range(len(trenes)*250):
            total.pop(0)

    for i in range(len(total)):
        if Avion.Capacidad < 10:
            prueba.append(total[i])
            if len(prueba) == 10:
                T = Avion(1000000, prueba)
                aviones.append(T)
                prueba = []
                Avion.Capacidad = 0
    prueba = []
    if len(aviones) >= 1:
        for i in range(len(aviones)*10):
            total.pop(0)

    for i in range(len(total)):
        if Camion.Capacidad < 10:
            prueba.append(total[i])
            if len(prueba) == 1:
                T = Camion(500000, prueba)
                camiones.append(T)
                prueba = []
                Camion.Capacidad = 0

    if len(camiones) >= 1:
        for i in range(len(camiones)):
            total.pop(0)

# Identifica que boton se presiono


leer()
container()
transporte()

print(len(barcos), "<- BARCOS")
print(len(trenes), "<- TRENES")
print(len(aviones), "<- AVIONES")
print(len(camiones), "<- CAMIONES")
print(camiones[0])
print(camiones[0].Contenido[0])
print(aviones[0])
print(aviones[0].Contenido[0])
print(aviones[0].Contenido[8])
