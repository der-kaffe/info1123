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


@dataclass
class Estanque_P(Contenedores):
    tamaño: str = "pequeño"


@dataclass
class Estanque_G(Contenedores):
    tamaño: str = "grande"


@dataclass
class Refrigerado_P(Contenedores):
    tamaño: str = "pequeño"


@dataclass
class Refrigerado_G(Contenedores):
    tamaño: str = "grande"


lista = []
# Listas que contienen containers
normal = []


def leer():
    with open("ejemplo_lista.csv") as f:
        reader = csv.reader(f, delimiter=";")
        # nos saltamos la primera linea
        next(reader, None)
        for row in reader:
            lista.append(row)


def container():
    p = 0
    for i in range(len(lista)):
        if lista[i][2] == "normal" and lista[i][3] == "solida":
            p += int(lista[i][4])
    p /= 1000
    # Sobra un cantidad (0.algo) pero en el .ods siempre lo desprecia, se hará igual
    p = int(p)
    # Lo dividimos en el T. del container grande
    p /= 24000
    # Lo restante (0.algo), que siempre será menor a 1, entonces es fp<24000 que es un Con.G
    fp = p-int(p)
    Peso_pequenho = (fp*24000)/100
    p = int(p)
    # Eso significa que tenemos 28 containers grandes normales

    for i in range(p-1):
        x = Contenedor_G("Normal", "Solida", 24000)
        normal.append(x)
    for i in range(1):
        x = Contenedor_P("Normal", "Solida", Peso_pequenho)
        normal.append(x)
    # p = 0
    # for i in range(len(lista)):
    #     if lista[i][2] == "normal" and lista[i][3] == "liquida":
    #         p += int(lista[i][4])
    # p /= 1000
    # #Sobra un cantidad (0.algo) pero en el .ods siempre lo desprecia, se hará igual
    # p = int(p)
    # p /= 24000
    # # Lo restante (0.algo), que siempre será menor a 1, entonces es fp<24000 que es un Con.G
    # fp = p-int(p)
    # Peso_pequenho = (fp*24000)/100
    # p = int(p)
    # for i in range(p):
    #     x = Contenedor_G("Normal", "Liquida", 24000)
    #     normal.append(x)
    # for i in range(1):
    #     x = Contenedor_P("Normal", "Liquida", Peso_pequenho)
    #     normal.append(x)


leer()
container()
