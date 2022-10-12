from dataclasses import dataclass
import csv
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk
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

# ==========================================


@dataclass
class Vehiculos:
    Costo = int
    Capacidad = int


@dataclass
class Barco(Vehiculos):
    Costo: int = 1000000000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Barco.Capacidad += 1

    def todo(self):
        todo = f"costo: {Barco.Costo}", self.Contenido
        return todo


@dataclass
class Tren(Vehiculos):
    Costo: int = 10000000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Tren.Capacidad += 1

    def todo(self):
        todo = f"costo: {Tren.Costo}", self.Contenido
        return todo


@dataclass
class Avion(Vehiculos):
    Costo: int = 1000000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Avion.Capacidad += 1

    def todo(self):
        todo = f"costo: {Avion.Costo}", self.Contenido
        return todo


@dataclass
class Camion(Vehiculos):
    Costo: int = 500000
    Capacidad = 0

    def __init__(self, Contenido):
        self.Contenido = Contenido
        Camion.Capacidad += 1

    def todo(self):
        todo = f"costo: {Camion.Costo}", self.Contenido
        return todo


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
    print()

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


def which_button(button_press):
    contenedor = 0
    estanque = 0
    peso = 0
    Peso_Normal = 0
    Peso_Refrigerada = 0
    Peso_Inflamable = 0
    gas = 0
    liquida = 0
    solida = 0
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', yscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.yview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')
    for i in range(len(barcos[button_press].Contenido)):
        if barcos[button_press].Contenido[i].masa == "solida":
            solida += barcos[button_press].Contenido[i].kilos
        if barcos[button_press].Contenido[i].masa == "liquida":
            liquida += barcos[button_press].Contenido[i].kilos
        if barcos[button_press].Contenido[i].masa == "gas":
            gas += barcos[button_press].Contenido[i].kilos
        if barcos[button_press].Contenido[i].tipo_carga == "normal":
            Peso_Normal += barcos[button_press].Contenido[i].kilos
        if barcos[button_press].Contenido[i].tipo_carga == "refrigerado":
            Peso_Refrigerada += barcos[button_press].Contenido[i].kilos
        if barcos[button_press].Contenido[i].tipo_carga == "inflamable":
            Peso_Inflamable += barcos[button_press].Contenido[i].kilos
        if type(barcos[button_press].Contenido[i]) == (Contenedor_G):
            contenedor += 1
            peso += barcos[button_press].Contenido[i].kilos
        elif type(barcos[button_press].Contenido[i]) == (Contenedor_P):
            contenedor += 1
            peso += barcos[button_press].Contenido[i].kilos
        else:
            estanque += 1
            peso += barcos[button_press].Contenido[i].kilos
    texto = tk.Label(
        frame, text=f"vehiculo numero {[button_press]}\n,Cantidad de contenedores: {contenedor}\nCantidad de Estanques {estanque}\nPeso Total: {peso}\nPeso Normal: {Peso_Normal}\nPeso Refrigerado: {Peso_Refrigerada}\nPeso Inflamable: {Peso_Inflamable}\nPeso Solido: {solida}\nPeso liquido: {liquida}\n Peso gas: {gas}\n\n{Barco.todo(barcos[button_press])}", wraplength=1100, background='white')

    texto.grid(column=0, row=0)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def which_button2(button_press):
    contenedor = 0
    estanque = 0
    peso = 0
    Peso_Normal = 0
    Peso_Refrigerada = 0
    Peso_Inflamable = 0
    gas = 0
    solida = 0
    liquida = 0
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', yscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.yview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')

    for i in range(len(trenes[button_press].Contenido)):
        if trenes[button_press].Contenido[i].masa == "solida":
            solida += trenes[button_press].Contenido[i].kilos
        if trenes[button_press].Contenido[i].masa == "liquida":
            liquida += trenes[button_press].Contenido[i].kilos
        if trenes[button_press].Contenido[i].masa == "gas":
            gas += trenes[button_press].Contenido[i].kilos
        if trenes[button_press].Contenido[i].tipo_carga == "normal":
            Peso_Normal += trenes[button_press].Contenido[i].kilos
        if trenes[button_press].Contenido[i].tipo_carga == "refrigerado":
            Peso_Refrigerada += trenes[button_press].Contenido[i].kilos
        if trenes[button_press].Contenido[i].tipo_carga == "inflamable":
            Peso_Inflamable += trenes[button_press].Contenido[i].kilos
        if type(trenes[button_press].Contenido[i]) == (Contenedor_G):
            contenedor += 1
            peso += trenes[button_press].Contenido[i].kilos
        elif type(trenes[button_press].Contenido[i]) == (Contenedor_P):
            contenedor += 1
            peso += trenes[button_press].Contenido[i].kilos
        else:
            estanque += 1
            peso += trenes[button_press].Contenido[i].kilos
    texto = tk.Label(
        frame, text=f"Tren numero {[button_press]}\n,Cantidad de contenedores: {contenedor}\nCantidad de Estanques {estanque}\nPeso Total: {peso}\nPeso Normal: {Peso_Normal}\nPeso Refrigerado: {Peso_Refrigerada}\nPeso Inflamable: {Peso_Inflamable}\nPeso Solido: {solida}\nPeso liquido: {liquida}\n Peso gas: {gas}\n\n{Tren.todo(trenes[button_press])}", wraplength=1100, background='white')
    texto.grid(column=0, row=0)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def which_button3(button_press):
    contenedor = 0
    estanque = 0
    peso = 0
    Peso_Normal = 0
    Peso_Refrigerada = 0
    Peso_Inflamable = 0
    solida = 0
    liquida = 0
    gas = 0
    print(button_press)
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', yscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.yview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')

    for i in range(len(aviones[button_press].Contenido)):
        if aviones[button_press].Contenido[i].masa == "solida":
            solida += aviones[button_press].Contenido[i].kilos
        if aviones[button_press].Contenido[i].masa == "liquida":
            liquida += aviones[button_press].Contenido[i].kilos
        if aviones[button_press].Contenido[i].masa == "gas":
            gas += aviones[button_press].Contenido[i].kilos
        if aviones[button_press].Contenido[i].tipo_carga == "normal":
            Peso_Normal += aviones[button_press].Contenido[i].kilos
        if aviones[button_press].Contenido[i].tipo_carga == "refrigerado":
            Peso_Refrigerada += aviones[button_press].Contenido[i].kilos
        if aviones[button_press].Contenido[i].tipo_carga == "inflamable":
            Peso_Inflamable += aviones[button_press].Contenido[i].kilos
        if type(aviones[button_press].Contenido[i]) == (Contenedor_G):
            contenedor += 1
            peso += aviones[button_press].Contenido[i].kilos
        elif type(aviones[button_press].Contenido[i]) == (Contenedor_P):
            contenedor += 1
            peso += aviones[button_press].Contenido[i].kilos
        else:
            estanque += 1
            peso += aviones[button_press].Contenido[i].kilos
    texto = tk.Label(
        frame, text=f"vehiculo numero {[button_press]}\n,Cantidad de contenedores: {contenedor}\nCantidad de Estanques {estanque}\nPeso Total: {peso}\nPeso Normal: {Peso_Normal}\nPeso Refrigerado: {Peso_Refrigerada}\nPeso Inflamable: {Peso_Inflamable}\nPeso Solido: {solida}\nPeso liquido: {liquida}\n Peso gas: {gas}\n\n{Avion.todo(aviones[button_press])}", wraplength=1100, background='white')
    texto.grid(column=0, row=0)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def which_button4(button_press):
    contenedor = 0
    estanque = 0
    peso = 0
    Peso_Normal = 0
    Peso_Refrigerada = 0
    Peso_Inflamable = 0
    solida = 0
    liquida = 0
    gas = 0
    print(button_press)
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', yscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.yview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')

    for i in range(len(camiones[button_press].Contenido)):
        if camiones[button_press].Contenido[i].masa == "solida":
            solida += camiones[button_press].Contenido[i].kilos
        if camiones[button_press].Contenido[i].masa == "liquida":
            liquida += camiones[button_press].Contenido[i].kilos
        if camiones[button_press].Contenido[i].masa == "gas":
            gas += camiones[button_press].Contenido[i].kilos
        if camiones[button_press].Contenido[i].tipo_carga == "normal":
            Peso_Normal += camiones[button_press].Contenido[i].kilos
        if camiones[button_press].Contenido[i].tipo_carga == "refrigerado":
            Peso_Refrigerada += camiones[button_press].Contenido[i].kilos
        if camiones[button_press].Contenido[i].tipo_carga == "inflamable":
            Peso_Inflamable += camiones[button_press].Contenido[i].kilos
        if type(camiones[button_press].Contenido[i]) == (Contenedor_G):
            contenedor += 1
            peso += camiones[button_press].Contenido[i].kilos
        elif type(camiones[button_press].Contenido[i]) == (Contenedor_P):
            contenedor += 1
            peso += camiones[button_press].Contenido[i].kilos
        else:
            estanque += 1
            peso += camiones[button_press].Contenido[i].kilos
    texto = tk.Label(
        frame, text=f"vehiculo numero {[button_press]}\n,Cantidad de contenedores: {contenedor}\nCantidad de Estanques {estanque}\nPeso Total: {peso}\nPeso Normal: {Peso_Normal}\nPeso Refrigerado: {Peso_Refrigerada}\nPeso Inflamable: {Peso_Inflamable}\nPeso Solido: {solida}\nPeso liquido: {liquida}\n Peso gas: {gas}\n\n{Camion.todo(camiones[button_press])}", wraplength=1100, background='white')
    texto.grid(column=0, row=0)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def BarcosV():
    ventana2 = Toplevel(ventana)
    ventana2.title("Barcos")
    ventana2.geometry("500x500")
    vp = Frame(ventana2)
    vp.grid(column=0, row=0, padx=(50, 30), pady=(10, 10))
    r = 0
    c = 0
    # img = ImageTk.PhotoImage(file='avion.png')
    # PhotoImage(master=ventana2, width=10, height=10)
    for x in range(len(barcos)):
        r += 1
        btn = Button(
            vp, text=f"{x}", command=lambda m=x: which_button(m))
        btn.grid(column=c, row=r)
        if r == 28:
            c += 1
            r = 0
    if len(barcos) == 0:
        n = Label(ventana2, text="No hay barcos")
        n.grid(column=1, row=2)


def trenesV():
    ventana2 = Toplevel(ventana)
    ventana2.title("Trenes")
    ventana2.geometry("500x500")
    vp = Frame(ventana2)
    vp.grid(column=0, row=0, padx=(50, 30), pady=(10, 10))
    r = 0
    c = 0
    # img = ImageTk.PhotoImage(file='avion.png')
    # PhotoImage(master=ventana2, width=10, height=10)
    for x in range(len(trenes)):
        r += 1
        btn = Button(
            vp, text=f"{x}", command=lambda m=x: which_button2(m))
        btn.grid(column=c, row=r)
        if r == 28:
            c += 1
            r = 0
    if len(trenes) == 0:
        n = Label(ventana2, text="No hay trenes")
        n.grid(column=1, row=2)


def avionesV():
    ventana2 = Toplevel(ventana)
    ventana2.title("Aviones")
    ventana2.geometry("500x500")
    vp = Frame(ventana2)
    vp.grid(column=0, row=0, padx=(50, 30), pady=(10, 10))
    r = 0
    c = 0
    # img = ImageTk.PhotoImage(file='avion.png')
    # PhotoImage(master=ventana2, width=10, height=10)
    for x in range(len(aviones)):
        r += 1
        btn = Button(
            vp, text=f"{x}", command=lambda m=x: which_button3(m))
        btn.grid(column=c, row=r)
        if r == 28:
            c += 1
            r = 0
    if len(aviones) == 0:
        n = Label(ventana2, text="No hay aviones")
        n.grid(column=1, row=2)


def CamionesV():
    ventana2 = Toplevel(ventana)
    ventana2.title("Camiones")
    ventana2.geometry("500x500")
    vp = Frame(ventana2)
    vp.grid(column=0, row=0, padx=(50, 30), pady=(10, 10))
    r = 0
    c = 0

    # PhotoImage(master=ventana2, width=10, height=10)
    for x in range(len(camiones)):
        r += 1
        btn = Button(
            vp, command=lambda m=x: which_button4(m), text=f"{x}")
        btn.grid(column=c, row=r)
        if r == 28:
            c += 1
            r = 0

    if len(camiones) == 0:
        n = Label(ventana2, text="No hay Camion")
        n.grid(column=1, row=2)


leer()
container()
transporte()
total = len(barcos) + len(trenes) + len(aviones) + len(camiones)

ventana = Tk()
ventana.title("Proyecto")
# ventana.geometry("1250x1250")

vp = Frame(ventana)

vp.grid(column=0, row=0, padx=(50, 30), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

img = tk.PhotoImage(file="barco.png")

totalvehiculos = Label(vp, text=f"Cantidad total de vehiculos: {total}")
totalvehiculos.grid(column=1, row=1)

img = tk.PhotoImage(file="barco.png")
totalvehiculos3 = Label(
    vp, text=f"\t\tCantidad: {len(barcos) }")
totalvehiculos3.grid(column=1, row=2)

totalvehiculos3 = Label(
    vp, image=img).grid(column=1, row=2)

img2 = tk.PhotoImage(file="tren.png")
totalvehiculos3 = Label(
    vp, text=f"\t\tCantidad: {len(trenes) }")
totalvehiculos3.grid(column=1, row=3)

totalvehiculos3 = Label(
    vp, image=img2).grid(column=1, row=3)

img3 = tk.PhotoImage(file="avion.png")
totalvehiculos3 = Label(
    vp, text=f"\t\tCantidad: {len(aviones) }")
totalvehiculos3.grid(column=1, row=4)

totalvehiculos3 = Label(
    vp, image=img3).grid(column=1, row=4)

img4 = tk.PhotoImage(file="camion.png")
totalvehiculos3 = Label(
    vp, text=f"\t\tCantidad: {len(camiones) }")
totalvehiculos3.grid(column=1, row=5)

totalvehiculos3 = Label(
    vp, image=img4).grid(column=1, row=5)

totalvehiculos1 = Label(
    vp, text=f"Precio total de vehiculos: {len(barcos)*1000000000 + len(trenes)*10000000+len(aviones)*1000000+len(camiones)*500000}")
totalvehiculos1.grid(column=1, row=7)


totalvehiculos1 = Label(
    vp, text=f"Precio de los barcos{len(barcos)*1000000000}")
totalvehiculos1.grid(column=1, row=8)

totalvehiculos2 = Label(
    vp, text=f"Precio de los trenes: {len(trenes)*10000000}")
totalvehiculos2.grid(column=1, row=9)


totalvehiculos3 = Label(
    vp, text=f"Precio de los aviones: {len(aviones)*1000000 }")
totalvehiculos3.grid(column=1, row=10)

totalvehiculos4 = Label(
    vp, text=f"Precio de los camiones: {len(camiones)*500000 }")
totalvehiculos4.grid(column=1, row=11)


btn = Button(vp, text="Barcos", command=BarcosV)
btn.grid(column=1, row=12)

btn2 = Button(vp, text="Trenes", command=trenesV)
btn2.grid(column=1, row=13)
btn3 = Button(vp, text="Avion", command=avionesV)
btn3.grid(column=1, row=14)

btn4 = Button(vp, text="Camiones", command=CamionesV)
btn4.grid(column=1, row=15)

ventana.mainloop()
