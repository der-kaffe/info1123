from dataclasses import dataclass
import csv
from tkinter import *
# Creamos clase padre


@dataclass
class Contenedores:
    contador = int
    tipo_carga: str
    masa: str
    kilos: int

    def __init__(self):
        Contenedores.contador += 1

    def kilos(self):
        return self.kilos

    def tipo_carga(self):
        return self.tipo_carga

    def masa(self):
        return self.masa


@dataclass
class Vehiculos:
    Costo = int
    capacidad = int
    tipoC: str


@dataclass
class Barco(Vehiculos):
    Costo: int = 1000000000
    Capacidad: int = 24000
    # self.topoP = tipoP
    # self.peso = peso


@dataclass
class Tren(Vehiculos):
    Costo: int = 10000000
    Capacidad: int = 250
    tipoC: str

    # def __init__(self, tipo):
    # self.tipoC = tipoC
    # self.topoP = tipoP
    # self.peso = peso


@dataclass
class Avion(Vehiculos):
    Costo: int = 1000000
    Capacidad: int = 10
    tipoC: str
    # def __init__(self, tipo):
    # self.tipoC = tipoC
    # self.topoP = tipoP
    # self.peso = peso


@dataclass
class Camion(Vehiculos):
    Costo: int = 500000
    Capacidad: int = 1
    tipoC: str
    # def __init__(self, tipo):
    # self.tipoC = tipoC
    # self.topoP = tipoP
    # self.peso = peso


@dataclass
# La clase hija se crea así, nombre_clase_hija(clase_padre)
class Contenedor_P(Contenedores):
    tamaño: str = "pequeño"
    contadorCP = 0

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos
        Contenedor_P.contadorCP += 1

    def cantidad():
        return Contenedor_P.contadorCP


@dataclass
class Contenedor_G(Contenedores):
    tamaño: str = "grande"
    contadorCG = 0

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos
        Contenedor_G.contadorCG += 1

    def cantidad():
        return Contenedor_G.contadorCG


@dataclass
class Estanque_P(Contenedores):
    tamaño: str = "pequeño"
    contadorEP = 0

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos
        Estanque_P.contadorEP += 1

    def cantidad():
        return Estanque_P.contadorEP


@dataclass
class Estanque_G(Contenedores):
    tamaño: str = "grande"
    contadorEG = 0

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos
        Estanque_G.contadorEG += 1

    def cantidad():
        return Estanque_G.contadorEG


lista = []
# Listas que contienen containers
normal = []
refrigerado = []
inflamable = []
C_all = []


def leer():
    with open("ejemplo_lista.csv") as f:
        reader = csv.reader(f, delimiter=";")
        # nos saltamos la primera linea
        next(reader, None)
        for row in reader:
            lista.append(row)


def container():
    x = ""
    y = ""
    for i in range(9):
        if i == 0:
            x = "normal"
            y = "solida"
            a = normal
            peso = 24000
        if i == 1:
            x = "normal"
            y = "liquida"
        if i == 2:
            x = "normal"
            y = "gas"
        if i == 3:
            x = "refrigerado"
            y = "solida"
            a = refrigerado
            peso = 20000
        if i == 4:
            x = "refrigerado"
            y = "liquida"
        if i == 5:
            x = "refrigerado"
            y = "gas"
        if i == 6:
            x = "inflamable"
            y = "solida"
            a = inflamable
            peso = 22000
        if i == 7:
            x = "inflamable"
            y = "liquida"
        if i == 8:
            x = "inflamable"
            y = "gas"
        p = 0
        for h in range(len(lista)):
            if lista[h][2] == x and lista[h][3] == y:
                p += int(lista[h][4])
        # Lo pasamos a tonelada
        p /= 1000
        # Lo dividimos en el T. del container grande
        p /= peso
        # Lo restante (0.algo), que siempre será menor a 1, entonces es fp<24000 que es un Con.G
        fp = p-int(p)
        Peso_pequenho = (fp*peso)/100
        p = int(p)
        # Eso significa que tenemos 28 containers grandes normales
        if i == 0:
            for e in range(p-1):
                C = Contenedor_G(x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Contenedor_P(x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(x, y, Peso_pequenho)
                a.append(C)
        elif i == 1 or i == 2:
            for e in range(p-1):
                C = Estanque_G(x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Estanque_P(x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(x, y, Peso_pequenho)
                a.append(C)
        elif i == 3:
            for e in range(p-1):
                C = Contenedor_G(x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Contenedor_P(x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(x, y, Peso_pequenho)
                a.append(C)
        elif i == 4 or i == 5:
            for e in range(p-1):
                C = Estanque_G(x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Estanque_P(x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(x, y, Peso_pequenho)
                a.append(C)
        elif i == 6:
            for e in range(p-1):
                C = Contenedor_G(x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Contenedor_P(x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(x, y, Peso_pequenho)
                a.append(C)
        elif i == 7 or i == 8:
            for e in range(p-1):
                C = Estanque_G(x, y, peso)
                a.append(C)
            if Peso_pequenho < 11000:
                for e in range(1):
                    C = Estanque_P(x, y, Peso_pequenho)
                a.append(C)
            else:
                for e in range(1):
                    C = Estanque_G(x, y, Peso_pequenho)
                a.append(C)


# Listas de Vehiculos
barcos = []
trenes = []
aviones = []
camiones = []


def transporte():
    C_all = refrigerado+normal+inflamable
    TC = len(C_all)
    tipoContenedor = ""
    for i in range(len(C_all)):
        print(TC, i)
        if (type(C_all[i])) == Contenedor_G:
            tipoContenedor = "Contenedor Grande"
        if (type(C_all[i])) == Contenedor_P:
            tipoContenedor = "Contenedor Pequeno"
        if TC/24000 >= 1:
            T = Barco(tipoContenedor)
            barcos.append()
            TC -= 24000
        elif TC/250 >= 1:
            T = Tren(tipoContenedor)
            trenes.append(T)
            TC -= 250
        elif TC/10 >= 1:
            T = Avion(tipoContenedor)
            aviones.append(T)
            TC -= 10
        elif TC/1 >= 1:
            T = Camion(tipoContenedor)
            camiones.append(T)
            TC -= 1
    print(len(barcos), len(trenes), len(aviones), len(camiones))
    # for i in range(len(aviones)):
    #     print(aviones[i].__dict__)
    #     print(aviones[i].__class__, i)
    # for i in range(len(camiones)):
    #     print(camiones[i].__dict__)
    #     print(camiones[i].__class__, i)


def mostrar_Vehiculo():
    a, b, c, d = len(barcos), len(trenes), len(aviones), len(camiones)
    mostrarV = Label(ventana,
                     text=f"Cantidad de Aviones, Trenes, Aviones y Camiones ={a}, {b}, {c}, {d}")
    mostrarV.pack()


leer()
container()
transporte()

# C_all = len(refrigerado+normal+inflamable)
# ventana = Tk()
# ventana.title("Proyecto")
# ventana.geometry("400x200")


# btn = Button(ventana, text="Vehiculos", command=mostrar_Vehiculo)
# btn.pack()
# # ventana.mainloop()
