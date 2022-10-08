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
    h = 0
    for i in range(len(lista)):
        if lista[i][2] == "normal" and lista[i][3] == "solida":
            print(lista[i][4])
            h += int(lista[i][4])
    h /= 1000
    # Sobra un 0.365 que en el .ods se desprecia, se hará igual
    h = int(h)
    # Lo dividimos en el T. del container grande
    h /= 24000
    # Lo restante (0.algo), que siempre será menor a 1, entonces es fh<24000 que es un Con.G
    fh = h-int(h)
    Peso_pequenho = (fh*24000)/100
    # print(h) Sobra un 0.003 que son 830 gramos, ni siquiera un kilo si que lo despreciamos
    h = int(h)
    # Eso significa que tenemos 28 containers grandes normales
    for i in range(h):
        x = Contenedor_G("Normal", "Solida", 24000)
        normal.append(x)
    for i in range(1):
        x = Contenedor_P("Normal", "Liquida", Peso_pequenho)
        normal.append(x)
    # for i in range(len(lista)):
    #     if lista[i][2] == "normal" and lista[i][3] == "liquida":
    #         print(lista[i][4])


leer()
container()
