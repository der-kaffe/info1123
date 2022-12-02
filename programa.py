from dataclasses import dataclass
import pandas as pd
import csv
import sys
from tkinter import *
from tkinter import messagebox
import time
import tkinter as tk
from PIL import ImageTk
import mysql.connector
from mysql.connector import errorcode
from fpdf import FPDF


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
        print("Ups ocurrio un error: ", err)
try:
    cursor = cnx.cursor()
except NameError:  # Este me ocurria cuando moodle estaba caído o por errores DNS
    print("Probablemente la conexión con el servidor fallo, intentarlo en otro momento o con otra conexión a internet")

# Creamos lo basico del pdf
pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('Arial', '', 10)


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

    def contenido(self):
        return self.Contenido()


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
    # with open("./ej2.csv") as f:
    reader = pd.read_csv('./ej2.csv', sep=',', header=0)
    # Eliminamos todo lo que hay en la tabla
    delete = 'delete from progra'
    cursor.execute(delete)
    # Añadimos lo nuevo a la tabla
    for row in range(len(reader)):
        data_product = {
            'id': int(reader['id'][row]),
            'nombre_Producto': reader['nombre_producto'][row],
            'tipo': reader['tipo'][row],
            'masa': reader['masa'][row],
            'peso': int(reader['peso'][row])
        }
        cursor.execute(add_product, data_product)
        cnx.commit()


# Listas que contienen containers
container_normal = []
estanque_liquida = []
estanque_gas = []
# Listas de Vehiculos
barcos = []
trenes = []
aviones = []
camiones = []
b_precio = 1000000000
t_precio = 10000000
a_precio = 1000000
c_precio = 500000


def container():
    # Las masa normales-solidos van en los containers si que los separamos
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
        if tipo_de_carga == "refrigerada":
            peso_estanque = 20000
        if tipo_de_carga == 'inflamable':
            peso_estanque = 22000
        p /= 1000
        # Lo dividimos en el T. del container grande
        p /= peso_estanque
        # Lo restante (0.algo), que siempre será menor a 1, entonces es fp<22000 que es un Con.G
        fp = p-int(p)
        Peso_pequenho = (fp*peso_estanque)/100
        p_int = int(p)
        for e in range(p_int):
            C = Estanque_G(tipo_de_carga, masa, peso_estanque)
            a.append(C)
        if Peso_pequenho < 11000:
            for e in range(1):
                C = Estanque_P(tipo_de_carga, masa, Peso_pequenho)
            a.append(C)
        else:
            for e in range(1):
                C = Estanque_G(tipo_de_carga, masa, Peso_pequenho)
            a.append(C)


def transporte(b, t, a, c):
    # Creamos una lista con  todos los containers en orden
    total = (container_normal) + (estanque_liquida) + (estanque_gas)
    prueba = []
    # Iteramos toda la lista total y lo añadimos a la lista prueba, si resulta que hay un total de X elementos correspondiente
    # A la cantidad maxima posible de containers que permite el vehiculo creamos un objeto que contenga la lista de containers
    for i in range(len(total)):
        prueba.append(total[i])
        if len(prueba) == 24000:
            T = Barco(b, prueba)
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
                T = Tren(t, prueba)
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
                T = Avion(a, prueba)
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
                T = Camion(c, prueba)
                camiones.append(T)
                prueba = []
                Camion.Capacidad = 0

    if len(camiones) >= 1:
        for i in range(len(camiones)):
            total.pop(0)


def which_button4(button_press, transporte):
    # Definimos variables
    contenedor = 0
    estanque = 0
    peso = 0
    Peso_Normal = 0
    Peso_Refrigerada = 0
    Peso_Inflamable = 0
    solida = 0
    liquida = 0
    gas = 0
    # Creamos ventana con scoll
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', yscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.yview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')
    # Dependiendo de donde hacemos click la lista que usaremos  cambiara
    if transporte == "barco":
        vehiculo = aviones
    elif transporte == "tren":
        vehiculo = trenes
    elif transporte == "avion":
        vehiculo = aviones
    elif transporte == "camion":
        vehiculo = camiones
    # Recorremos la lista .Contenido de los objetos y despues lo agregamos al contador
    for i in range(len(vehiculo[button_press].Contenido)):
        if vehiculo[button_press].Contenido[i].masaa == "solida":
            solida += vehiculo[button_press].Contenido[i].kiloss
        if vehiculo[button_press].Contenido[i].masaa == "liquida":
            liquida += vehiculo[button_press].Contenido[i].kiloss
        if vehiculo[button_press].Contenido[i].masaa == "gas":
            gas += vehiculo[button_press].Contenido[i].kiloss
        if vehiculo[button_press].Contenido[i].tipo__carga == "normal":
            Peso_Normal += vehiculo[button_press].Contenido[i].kiloss
        if vehiculo[button_press].Contenido[i].tipo__carga == "refrigerado":
            Peso_Refrigerada += vehiculo[button_press].Contenido[i].kiloss
        if vehiculo[button_press].Contenido[i].tipo__carga == "inflamable":
            Peso_Inflamable += vehiculo[button_press].Contenido[i].kiloss
        if type(vehiculo[button_press].Contenido[i]) == (Contenedor_G):
            contenedor += 1
            peso += vehiculo[button_press].Contenido[i].kiloss
        elif type(vehiculo[button_press].Contenido[i]) == (Contenedor_P):
            contenedor += 1
            peso += vehiculo[button_press].Contenido[i].kiloss
        else:
            estanque += 1
            peso += vehiculo[button_press].Contenido[i].kiloss
    # Lo escribimos en tkinter
    texto = tk.Label(
        frame, text=f"{transporte} numero {[button_press]}\nCantidad de contenedores: {contenedor}\nCantidad de Estanques {estanque}\n\n\tP E S O S   T I P O DE C A R G A\n\nPeso Total: {peso}\nPeso Normal: {Peso_Normal}\nPeso Refrigerado: {Peso_Refrigerada}\nPeso Inflamable: {Peso_Inflamable}\n\n\tP E S O   M A S A\n\nPeso Solido: {solida}\nPeso liquido: {liquida}\n Peso gas: {gas}", wraplength=1100, background='white')
    texto.grid(column=0, row=0)
    texto = tk.Label(
        frame, text=f"{vehiculo[button_press].Contenido}", wraplength=1100, background='white')
    texto.grid(column=1, row=1)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def barcosV():
    # Creamos una ventana con scroll con la cantidad de botones respectivos
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', xscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.xview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')
    r = 0
    h = 0
    for x in range(len(barcos)):
        r += 1
        # Con este boton enviamos el tipo de lista que quermeos reccorrer y el boton presionado
        btn = Button(
            frame, command=lambda m=x: which_button4(m, "barco"), text=f"{x}")
        btn.grid(column=h, row=r)
        if r == 26:
            h += 1
            r = 0
    if len(barcos) == 0:
        n = Label(frame, text="No hay Barcos")
        n.grid(column=1, row=2)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def trenesV():
    # Creamos una ventana con scroll con la cantidad de botones respectivos
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', xscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.xview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')
    r = 0
    h = 0
    for x in range(len(trenes)):
        r += 1
        btn = Button(
            frame, command=lambda m=x: which_button4(m, "tren"), text=f"{x}")
        btn.grid(column=h, row=r)
        if r == 26:
            h += 1
            r = 0
    if len(trenes) == 0:
        n = Label(frame, text="No hay Trenes")
        n.grid(column=1, row=2)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def avionesV():
    # Creamos una ventana con scroll con la cantidad de botones respectivos
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', xscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.xview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')
    r = 0
    h = 0
    for x in range(len(aviones)):
        r += 1
        btn = Button(
            frame, command=lambda m=x: which_button4(m, "avion"), text=f"{x}")
        btn.grid(column=h, row=r)
        if r == 26:
            h += 1
            r = 0

    if len(aviones) == 0:
        n = Label(frame, text="No hay Aviones")
        n.grid(column=1, row=2)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))


def camionesV():
    # Creamos una ventana con scroll con la cantidad de botones respectivos
    ventana = Tk()
    Scrollbar = tk.Scrollbar(ventana)
    c = tk.Canvas(ventana, background='white', xscrollcommand=Scrollbar.set)
    Scrollbar.config(command=c.xview)
    Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame = tk.Frame(c)
    c.pack(side="left", fill="both", expand=True)
    c.create_window(0, 0, window=frame, anchor='nw')
    r = 0
    h = 0
    for x in range(len(camiones)):
        r += 1
        btn = Button(
            frame, command=lambda m=x: which_button4(m, "camion"), text=f"{x}")
        btn.grid(column=h, row=r)
        if r == 26:
            h += 1
            r = 0

    if len(camiones) == 0:
        n = Label(frame, text="No hay Camiones")
        n.grid(column=1, row=2)
    ventana.update()
    c.config(scrollregion=c.bbox("all"))

# "a" será el valor de los vehiculos y var será lo que aparecera en tkinter


def recalcularBarcos(a, var):
    # Calculamos en valor multiplicando el precio por la cantidad de objetos en la lista
    numero = a * int(len(barcos))

    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tprecios nuevos barco: {numero} ", align='C', fill=0, border=1)

    return var.set(numero)


def recalcularTrenes(a, var2):
    # Calculamos en valor multiplicando el precio por la cantidad de objetos en la lista
    numero = a * int(len(trenes))
    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tprecios nuevos trenes: {numero} ", align='C', fill=0, border=1)
    return var2.set(numero)


def recalcularAviones(a, var3):
    # Calculamos en valor multiplicando el precio por la cantidad de objetos en la lista
    numero = a * int(len(aviones))
    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tprecios nuevos aviones: {numero} ", align='C', fill=0, border=1)
    return var3.set(numero)


def recalcularCamiones(a, var4):
    # Calculamos en valor multiplicando el precio por la cantidad de objetos en la lista
    numero = a * int(len(camiones))
    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tprecios nuevos camiones: {numero} ", align='C', fill=0, border=1)
    return var4.set(numero)

# Insertamos los precios de los vehiculos


def principal_venetana(b_precio, t_precio, a_precio, c_precio):
    total = len(barcos) + len(trenes) + len(aviones) + len(camiones)

    # Hacemos una ventana principal
    ventana = Tk()
    ventana.title("Proyecto")
    vp = Frame(ventana)
    vp.grid(column=0, row=0, padx=(50, 30), pady=(10, 10))
    vp.columnconfigure(0, weight=1)
    vp.rowconfigure(0, weight=1)
    var = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()
    var4 = tk.StringVar()
    # Escribimos las caracteristicas generales pedidas
    totalvehiculos = Label(vp, text=f"Cantidad total de vehiculos: {total}")
    pdf.multi_cell(
        w=50, h=5, txt=f"Cantidad total de vehiculos: {str(total)}", align='C', fill=0, border=1)
    totalvehiculos.grid(column=1, row=1)
    # Imagenes y texto respectivo
    img = tk.PhotoImage(file="barco.png")
    totalvehiculos3 = Label(
        vp, text=f"\t\tCantidad: {len(barcos) }")
    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tCantidad  barcos: {str(len(barcos)) }", align='C', fill=0, border=1)

    totalvehiculos3.grid(column=1, row=2)

    totalvehiculos3 = Label(
        vp, image=img).grid(column=1, row=2)

    img2 = tk.PhotoImage(file="tren.png")
    totalvehiculos3 = Label(
        vp, text=f"\t\tCantidad: {len(trenes) }")
    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tCantidad trenes: {str(len(trenes)) }", align='C', fill=0, border=1)
    totalvehiculos3.grid(column=1, row=3)

    totalvehiculos3 = Label(
        vp, image=img2).grid(column=1, row=3)

    img3 = tk.PhotoImage(file="avion.png")
    totalvehiculos3 = Label(
        vp, text=f"\t\tCantidad: {len(aviones) }")
    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tCantidad aviones: {str(len(aviones)) }", align='C', fill=0, border=1)
    totalvehiculos3.grid(column=1, row=4)

    totalvehiculos3 = Label(
        vp, image=img3).grid(column=1, row=4)

    img4 = tk.PhotoImage(file="camion.png")
    totalvehiculos3 = Label(
        vp, text=f"\t\tCantidad: {len(camiones) }")
    pdf.multi_cell(
        w=50, h=5, txt=f"\t\tCantidad camiones: {str(len(camiones)) }", align='C', fill=0, border=1)
    totalvehiculos3.grid(column=1, row=5)

    totalvehiculos3 = Label(
        vp, image=img4).grid(column=1, row=5)

    totalvehiculos1 = Label(
        vp, text=f"Precio total de vehiculos: {len(barcos)*b_precio + len(trenes)*t_precio+len(aviones)*a_precio+len(camiones)*c_precio}")
    pdf.multi_cell(
        w=50, h=5, txt=f"Precio total de vehiculos: {str(len(barcos)*b_precio + len(trenes)*t_precio+len(aviones)*a_precio+len(camiones)*c_precio)}", align='C', fill=0, border=1)
    totalvehiculos1.grid(column=1, row=7)

    totalvehiculos1 = Label(
        vp, text=f"Precio de los barcos{len(barcos)*b_precio}")
    pdf.multi_cell(
        w=50, h=5, txt=f"Precio de los barcos {str(len(barcos)*b_precio)}", align='C', fill=0, border=1)
    totalvehiculos1.grid(column=1, row=8)

    totalvehiculos2 = Label(
        vp, text=f"Precio de los trenes: {len(trenes)*t_precio}")
    totalvehiculos2.grid(column=1, row=9)

    totalvehiculos3 = Label(
        vp, text=f"Precio de los aviones: {len(aviones)*a_precio }")
    totalvehiculos3.grid(column=1, row=10)

    totalvehiculos4 = Label(
        vp, text=f"Precio de los camiones: {len(camiones)*c_precio }")
    totalvehiculos4.grid(column=1, row=11)

    # Creamos botones
    btn = Button(vp, text="Barcos", command=barcosV)
    btn.grid(column=1, row=12)

    btn2 = Button(vp, text="Trenes", command=trenesV)
    btn2.grid(column=1, row=13)
    btn3 = Button(vp, text="Avion", command=avionesV)
    btn3.grid(column=1, row=14)

    btn4 = Button(vp, text="Camiones", command=camionesV)
    btn4.grid(column=1, row=15)
    # El recalculo de los valores
    el = tk.Label(vp, text='Barcos')
    el.grid(column=1, row=16)
    entrada = tk.Entry(vp)
    entrada.grid(column=1, row=17)
    btn = tk.Button(vp, text="recalcular precio de barcos", fg='blue',
                    command=lambda: recalcularBarcos(int(entrada.get()), var))
    btn.grid(column=1, row=18)

    res = tk.Label(vp, bg='plum', textvariable=var)
    res.grid(column=1, row=20)

    # El recalculo de los valores de los vehiculos
    el = tk.Label(vp, text='Trenes')
    el.grid(column=1, row=21)
    entrada2 = tk.Entry(vp)
    entrada2.grid(column=1, row=22)

    btn2 = tk.Button(vp, text="recalcular precio de trenes", fg='blue',
                     command=lambda: recalcularTrenes(int(entrada2.get()), var2))

    btn2.grid(column=1, row=23)
    res = tk.Label(vp, bg='plum', textvariable=var2)
    res.grid(column=1, row=24)
    # El recalculo de los valores
    el = tk.Label(vp, text='Aviones')
    el.grid(column=1, row=25)
    entrada3 = tk.Entry(vp)
    entrada3.grid(column=1, row=26)

    btn3 = tk.Button(vp, text="recalcular precio de aviones", fg='blue',
                     command=lambda: recalcularAviones(int(entrada3.get()), var3))

    btn3.grid(column=1, row=27)
    res = tk.Label(vp, bg='plum', textvariable=var3)
    res.grid(column=1, row=28)
    # El recalculo de los valores
    el = tk.Label(vp, text='Camiones')
    el.grid(column=1, row=29)
    entrada4 = tk.Entry(vp)
    entrada4.grid(column=1, row=30)

    btn4 = tk.Button(vp, text="recalcular precio de camiones", fg='blue',
                     command=lambda: recalcularCamiones(int(entrada4.get()), var4))

    btn4.grid(column=1, row=31)
    res = tk.Label(vp, bg='plum', textvariable=var4)
    res.grid(column=1, row=34)

    el = tk.Label(
        vp, text='*La informacion se envia automaticamente a el pdf despues de cerrar el GUI', font=('Arial', 8))
    el.grid(column=1, row=35)

    # Inicia el loop

    ventana.mainloop()


def escribirPDF():
    contenedor = 0
    estanque = 0
    peso = 0
    Peso_Normal = 0
    Peso_Refrigerada = 0
    Peso_Inflamable = 0
    solida = 0
    liquida = 0
    gas = 0
    # Se haran 4 bucles con las 4 listas diferentes
    for e in range(4):
        if e == 0:
            vehiculo = aviones
        elif e == 1:
            vehiculo = trenes
        elif e == 2:
            vehiculo = aviones
        elif e == 3:
            vehiculo = camiones
        # Recorremos la lista .Contenido de los objetos y despues lo agregamos al contador
        for i in range(len(vehiculo)):
            for y in range(len(vehiculo[i].Contenido)):
                if vehiculo[i].Contenido[y].masaa == "solida":
                    solida += vehiculo[i].Contenido[y].kiloss
                if vehiculo[i].Contenido[y].masaa == "liquida":
                    liquida += vehiculo[i].Contenido[y].kiloss
                if vehiculo[i].Contenido[y].masaa == "gas":
                    gas += vehiculo[i].Contenido[y].kiloss
                if vehiculo[i].Contenido[y].tipo__carga == "normal":
                    Peso_Normal += vehiculo[i].Contenido[y].kiloss
                if vehiculo[i].Contenido[y].tipo__carga == "refrigerado":
                    Peso_Refrigerada += vehiculo[i].Contenido[y].kiloss
                if vehiculo[i].Contenido[y].tipo__carga == "inflamable":
                    Peso_Inflamable += vehiculo[i].Contenido[y].kiloss
                if type(vehiculo[i].Contenido[y]) == (Contenedor_G):
                    contenedor += 1
                    peso += vehiculo[i].Contenido[y].kiloss
                elif type(vehiculo[i].Contenido[y]) == (Contenedor_P):
                    contenedor += 1
                    peso += vehiculo[i].Contenido[y].kiloss
                else:
                    estanque += 1
                    peso += vehiculo[i].Contenido[y].kiloss
        pdf.multi_cell(
            w=50, h=5, txt=f"Contenedores: {contenedor}\n Estanques: {estanque}", align='C', fill=0, border=1)
        pdf.multi_cell(
            w=50, h=5, txt=f"Peso: {peso}", align='C', fill=0, border=1)
    pdf.multi_cell(
        w=50, h=5, txt=f"Peso normal: {Peso_Normal}\n Peso Refrigerado: {Peso_Refrigerada}\n Peso Inflamable: {Peso_Inflamable}", align='C', fill=0, border=1)

    pdf.multi_cell(
        w=50, h=5, txt=f"Peso solido: {solida}\nPeso liquido: {liquida}\nPeso gas: {gas}", align='C', fill=0, border=1)
    todo = barcos+trenes+aviones+camiones
    for i in range(len(todo)):
        pdf.multi_cell(
            w=199, h=5, txt=f"{todo[i].Contenido}", align='C', fill=0, border=1)


# try:
inicio = time.time()

for i in range(24):
    print(i, " ")

# leer()
# container()
# gas_liquido()
# transporte(b_precio, t_precio, a_precio, c_precio)
# principal_venetana(b_precio, t_precio, a_precio, c_precio)
# escribirPDF()
# pdf.output('hoja.pdf')
# fin = time.time()
# except:
#     print("Ups, ocurrio un error: ", sys.exc_info()[0])
