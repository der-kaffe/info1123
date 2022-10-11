from dataclasses import dataclass
import csv
from pygame import *
import pygame
# Creamos clase padre
pygame.init()


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

# ==========================================


@dataclass
class Vehiculos:
    Costo = int
    Capacidad = int
    # tipoC: str


@dataclass
class Barco(Vehiculos):
    Costo: int = 1000000000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Barco.Capacidad += 1


@dataclass
class Tren(Vehiculos):
    Costo: int = 10000000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Tren.Capacidad += 1
    # def __init__(self, tipo):
    # self.tipoC = tipoC
    # self.topoP = tipoP
    # self.peso = peso


@dataclass
class Avion(Vehiculos):
    Costo: int = 1000000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Avion.Capacidad += 1


@dataclass
class Camion(Vehiculos):
    Costo: int = 500000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Camion.Capacidad += 1
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

    def todo():
        todo = Contenedor_G.tamaño, Contenedor_G.tipo_carga, Contenedor_G.masa, Contenedor_G.kilos
        return

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
    for i in range(9):
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
#Contenedor_G =  83
#Contenedor_P =   3
#EstanqueG    = 139
#EstanqueP    =   6


def transporte():
    total = (normal_solida) + (estanque_liquida) + (estanque_gas)

    prueba = []

    print(len(total), "total")
    for i in range(len(total)):
        prueba.append(total[i])
        if len(prueba) == 24000:
            T = Barco(prueba)
            barcos.append(T)
            prueba = []
            Barco.Capacidad = 0
    prueba = []

    if len(barcos) >= 1:
        for i in range(len(barcos)*24000):
            total.pop(0)

    for i in range(len(total)):
        if Tren.Capacidad < 250:
            prueba.append(total[i])
            if len(prueba) == 250:
                T = Tren(prueba)
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
                T = Avion(prueba)
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
                T = Camion(prueba)
                camiones.append(T)
                prueba = []
                Camion.Capacidad = 0

    if len(camiones) >= 1:
        for i in range(len(camiones)):
            total.pop(0)

    print(len(barcos), "Barco")
    print(len(trenes), "Tren")
    print(len(aviones), "Avion")
    print(len(camiones), "Camion")
    print(len(prueba), "prueba")


# print(aviones[0].Contenido[0])  # EJEMPLO
# print(aviones[0].Contenido[0].tipo_carga)  # ejemplo
leer()
container()
transporte()
r = True


def btn(screen, boton, msj):
    if boton.collidepoint(mouse.get_pos()):
        #draw.rect(surface, color, rect)
        draw.rect(screen, (237, 128, 19), boton, 0)
    else:
        draw.rect(screen, (13, 12, 12), boton, 0)
    texto = fuente.render(msj, True, (220, 220, 220))
    screen.blit(texto, (boton.x+(boton.width-texto.get_width()) /
                2, boton.y+(boton.height-texto.get_height())/2))


def botones():
    for x in range(int(600/2)):
        for y in range(int(800/2)):
            boton = Rect(100, 100, 50, 50)
            btn(screen, boton, "hola")


screen = display.set_mode((800, 600))

#Rect(left, top, width, height)
boton = Rect(100, 100, 50, 50)
boton2 = Rect(300, 100, 50, 50)
fuente = font.SysFont("Calibri", 15)

while(r):
    screen.fill((255, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            r = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            if boton.collidepoint(mouse.get_pos()):
                print("Click A")
            if boton2.collidepoint(mouse.get_pos()):
                print("Click B")
    botones()
    # btn(screen,boton,"Avion")
    # btn(screen, boton2, "Camion")
    display.flip()
