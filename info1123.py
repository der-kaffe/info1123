from dataclasses import dataclass
import csv

# Creamos clase padre


@dataclass
class Contenedores:
    tipo_carga: str
    masa: str
    kilos: int

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


@dataclass
class Barco(Vehiculos):
    Costo = 1000000000
    Capacidad = 24000


@dataclass
class Tren(Vehiculos):
    Costo = 10000000
    Capacidad = 250


@dataclass
class Avion(Vehiculos):
    Costo = 1000000
    Capacidad = 10


@dataclass
class Camion(Vehiculos):
    Costo = 500000
    Capacidad = 1


@dataclass
# La clase hija se crea así, nombre_clase_hija(clase_padre)
class Contenedor_P(Contenedores):
    tamaño: str = "pequeño"


@dataclass
class Contenedor_G(Contenedores):
    tamaño: str = "grande"

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos


@dataclass
class Estanque_P(Contenedores):
    tamaño: str = "pequeño"

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos


@dataclass
class Estanque_G(Contenedores):
    tamaño: str = "grande"

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos


@dataclass
class Refrigerado_P(Contenedores):
    tamaño: str = "pequeño"

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos


@dataclass
class Refrigerado_G(Contenedores):
    tamaño: str = "grande"

    def __init__(self, tipo_carga, masa, kilos):
        self.tipo_carga = tipo_carga
        self.masa = masa
        self.kilos = kilos


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


def transporte():
    C_all = refrigerado+normal+inflamable
    TC = len(C_all)


leer()
container()
transporte()
