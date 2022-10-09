import matplotlib.pyplot as plt
import csv


class Vehiculo():
    def __init__(self, transporte, contenedores, costo, normal, refrigerado, estanqueL, estanqueI, TonelajeTotal, solida, liquida, gas, pesonormal, pesoinflamable, pesorefrigerado):
        self.transporte = transporte
        self.contenedores = contenedores
        self.costo = costo
        self.normal = normal
        self.refrigerado = refrigerado
        self.estanqueL = estanqueL
        self.estanqueI = estanqueI
        self.TonelajeTotal = TonelajeTotal
        self.solida = solida
        self.liquida = liquida
        self.gas = gas
        self.pesonormal = pesonormal
        self.pesoinflamable = pesoinflamable
        self.pesorefrigerado = pesorefrigerado

    def Tcont(self):
        todo = self.transporte, self.contenedores, self.costo, self.normal, self.refrigerado, self.estanqueL, self.estanqueI
        return todo

    def normal(self):
        return self.normal

    def refri(self):
        return self.refrigerado

    def estanqueL(self):
        return self.estanqueL

    def estanqueI(self):
        return self.estanqueI

    def to():
        return self.contenedores

    def costo(self):
        return self.costo


class contenedor():
    def __init__(self, ID, Nombre, tamano, peso, masa, tipo, tipo2):
        self.ID = ID
        self.Nombre = Nombre
        self.peso = peso
        self.masa = masa
        self.tamano = tamano
        self.tipo = tipo
        self.tipo2 = tipo2

    def dartodo(self):
        todo = self.ID, self.Nombre, self.tamano, self.peso, self.masa, self.tipo
        return todo

    def tipo22(self):
        return self.tipo2

    def masa(self):
        return self.masa

    def peso(self):
        return self.peso

    def tamano(self):
        return self.tamano

    def tipo(self):
        return self.tipo


lista = []
proceso = []
containersN = []
containersR = []
estanqueL = []
estanqueI = []
barco = []
tren = []
Avion = []
Camion = []



def leer():
    with open("ejemplo_lista.csv") as f:
        reader = csv.reader(f, delimiter=";")
        # nos saltamos la primera linea
        next(reader, None)
        for row in reader:
            lista.append(row)


def connormal():
    pesof = 0
    peso = 0
    tipo2 = ""
    tipo22 = ""
    nombre = ""
    nombre2 = ""
    id = ""
    id2 = ""
    masa = ""
    masa2 = ""
    # recorremos toda la lista y verificamos si es lo que queremos
    for fila in proceso:
        if "normal" in fila:
            if "solida" in fila:
                if int(fila[4]) > 24000:
                    peso = int(fila[4])/24000
                    pesoi = int(peso)
                    pesof += peso-pesoi
                    # Para saber si hay sobras, darles sus atributos
                    if peso-pesoi < 1:
                        tipo22 = "/"+fila[2]
                        id2 = "/"+fila[0]
                        nombre2 = "/"+fila[1]
                        masa2 = "/"+fila[3]
                    # Le damos atributos a los containers normales
                    tipo2 = "/"+fila[2]
                    id = "/"+fila[0]
                    nombre = "/"+fila[1]
                    masa = "/"+fila[3]
                    # Como el peso es unas cuantas veces 24000 seran muchos de estos
                    for i in range(pesoi):
                        containerN = contenedor(
                            id, nombre, "grande", 24000, masa, "normal", tipo2)
                        containersN.append(containerN)
                    peso = 0
                    id = ""
                    nombre = ""
                    masa = ""
                    tipo2 = ""
                    for i in range(int(pesof)):
                        containerN = contenedor(
                            id2, nombre2, "grande", 24000, masa2, "normal", tipo22)
                        containersN.append(containerN)
    # El que queda flotando, que tiene menos de 24000 lo hacemos en uno pequeno
    pesofl = pesof - int(pesof)
    if float(pesofl) < 1:
        pesof = (pesof*24000)/100
        containerN = contenedor(
            id, nombre, "pequeno", pesof, masa2, "normal", tipo2)
        containersN.append(containerN)


def conrefrigerado():
    pesof = 0
    peso = 0
    tipo2 = ""
    tipo22 = ""
    nombre = ""
    nombre2 = ""
    id = ""
    id2 = ""
    masa = ""
    masa2 = ""

    for fila in proceso:
        if "refrigerado" in fila:
            if "solida" in fila:
                if int(fila[4]) > 20000:
                    # print(fila)
                    peso = int(fila[4])/20000
                    pesoi = int(peso)
                    pesof += peso-pesoi
                    if peso-pesoi < 1:
                        tipo22 = "/"+fila[2]
                        id2 = "/"+fila[0]
                        nombre2 = "/"+fila[1]
                        masa2 = "/"+fila[3]
                    tipo2 = "/"+fila[2]
                    id = "/"+fila[0]
                    nombre = "/"+fila[1]
                    masa = "/"+fila[3]
                    for i in range(pesoi):
                        containerN = contenedor(
                            id, nombre, "grande", 20000, masa, "refrigerado", tipo2)
                        containersR.append(containerN)
                    peso = 0
                    id = ""
                    nombre = ""
                    tipo2 = ""
                    masa = ""
                    for i in range(int(pesof)):
                        containerN = contenedor(
                            id2, nombre2, "grande", 20000, masa2, "refrigerado", tipo22)
                        containersR.append(containerN)
    pesofl = pesof - int(pesof)
    if float(pesofl) < 1:
        pesof = (pesof*20000)/100
        containerN = contenedor(
            id, nombre, "pequeno", pesof, masa2, "refrigerado", tipo2)
        containersR.append(containerN)


def estanqueLiquidos():
    pesof = 0
    peso = 0
    tipo2 = ""
    tipo22 = ""
    nombre = ""
    nombre2 = ""
    id = ""
    id2 = ""
    masa = ""
    masa2 = ""
    for fila in proceso:
        if "normal" in fila:
            if "liquido" or "gas" in fila:
                if int(fila[4]) > 24000:
                    peso = int(fila[4])/24000
                    pesoi = int(peso)
                    pesof += peso-pesoi
                    if peso-pesoi < 1:
                        id2 = "/"+fila[0]
                        tipo22 = "/"+fila[2]
                        nombre2 = "/"+fila[1]
                        masa2 = "/"+fila[3]
                    id = "/"+fila[0]
                    tipo2 = "/"+fila[2]
                    nombre = "/"+fila[1]
                    masa = "/"+fila[3]
                    for i in range(pesoi):
                        containerN = contenedor(  # Estanque de liquidos
                            id, nombre, "grande", 24000, masa, "EdL", tipo2)
                        estanqueL.append(containerN)
                    peso = 0
                    id = ""
                    nombre = ""
                    masa = ""
                    tipo2 = ""
                    for i in range(int(pesof)):
                        containerN = contenedor(
                            id2, nombre2, "grande", 24000, masa2, "EdL", tipo22)
                        estanqueL.append(containerN)
    pesofl = pesof - int(pesof)
    if float(pesofl) < 1:
        pesof = (pesof*24000)/100
        containerN = contenedor(
            id, nombre, "pequeno", pesof, masa2, "EdL", tipo2)
        estanqueL.append(containerN)


def estanqueIn():
    pesof = 0
    peso = 0
    tipo2 = ""
    tipo22 = ""
    nombre = ""
    nombre2 = ""
    id = ""
    id2 = ""
    masa = ""
    masa2 = ""
    for fila in proceso:
        if "inflamable" in fila:
            if "gas" or "liquida" in fila:
                if int(fila[4]) > 20000:
                    peso = int(fila[4])/20000
                    pesoi = int(peso)
                    pesof += peso-pesoi
                    if peso-pesoi < 1:
                        id2 = "/"+fila[0]
                        nombre2 = "/"+fila[1]
                        masa2 = "/"+fila[3]
                        tipo22 = "/"+fila[2]
                    id = "/"+fila[0]
                    tipo2 = "/"+fila[2]
                    nombre = "/"+fila[1]
                    masa = "/"+fila[3]
                    for i in range(pesoi):
                        containerN = contenedor(  # Estanque inflamable
                            id, nombre, "grande", 20000, masa, "EI", tipo2)
                        estanqueI.append(containerN)
                    peso = 0
                    tipo2 = ""
                    id = ""
                    nombre = ""
                    masa = ""
                    for i in range(int(pesof)):
                        containerN = contenedor(
                            id2, nombre2, "grande", 20000, masa2, "EI", tipo22)
                        estanqueI.append(containerN)
    pesofl = pesof - int(pesof)
    if float(pesofl) < 1:
        pesof = (pesof*20000)/100
        containerN = contenedor(
            id, nombre, "pequeno", pesof, masa2, "EI", tipo2)
        estanqueI.append(containerN)


# hist para los tipos de productos
histipo1 = []


def cargando():
    containers = containersN+containersR+estanqueL + \
        estanqueI  # Lista con todos los containers
    lista = []
    p = []
    pesonormal = 0
    pesoinflamable = 0
    pesorefrigerado = 0
    solida = 0
    gas = 0
    liquida = 0
    peso = 0
    grande = 0
    peq = 0
    c = 0
    E_L = 0
    normal = 0
    refrigerado = 0
    inf = 0
    for i in range(len(containers)):
        lista.append((containers[i]))
        # print(containers[i].__dict__)
    for row in lista:
        if contenedor.tamano(containers[i]) == "grande":
            grande += 1
        if contenedor.tamano(containers[i]) == "pequeno":
            peq += 1
    grande = int(peq / 2) + grande  # Cantidad de contendores grandes
    peq = float(peq / 2) - int(peq / 2)  # Peque;os
    if peq == 0.5:
        grande += 1
        peq = 0
    for row in lista:
        # print(row.__dict__)
        p.append(row)
        c += 1
        # contadores y pesos varios
        if contenedor.tipo(p[-1]) == "EdL":
            E_L += 1
            peso += contenedor.peso(p[-1])
        if contenedor.tipo(p[-1]) == "normal":
            normal += 1
            peso += contenedor.peso(p[-1])
        if contenedor.tipo(p[-1]) == "refrigerado":
            refrigerado += 1
            peso += contenedor.peso(p[-1])
        if contenedor.tipo(p[-1]) == "EI":
            inf += 1
            peso += contenedor.peso(p[-1])
        if contenedor.masa(p[-1]) == "/solida":
            solida += contenedor.peso(p[-1])/100
        if contenedor.masa(p[-1]) == "/liquida":
            liquida += contenedor.peso(p[-1])/100
        if contenedor.masa(p[-1]) == "/gas":
            gas += contenedor.peso(p[-1])/100
        if contenedor.tipo22(p[-1]) == "/normal":
            pesonormal += contenedor.peso(p[-1])/100
            histipo1.append(contenedor.tipo22(p[-1]))
        if contenedor.tipo22(p[-1]) == "/inflamable":
            pesoinflamable += contenedor.peso(p[-1])/100
            histipo1.append(contenedor.tipo22(p[-1]))
        if contenedor.tipo22(p[-1]) == "/refrigerado":
            pesorefrigerado += contenedor.peso(p[-1])/100
            histipo1.append(contenedor.tipo22(p[-1]))
        if grande > 24000:
            # Usamos c como gatillo para tomarlo cuando esta la cantidad correcta de datos en p y los demas
            if c >= 24000:
                transporte = Vehiculo(
                    "barco", len(p), 1000000000, normal, refrigerado, E_L, inf, peso, solida, liquida, gas, pesonormal, pesoinflamable, pesorefrigerado)
                barco.append(transporte)
                peso = 0
                c = 0
                E_L = normal = refrigerado = inf = solida = liquida = gas = pesonormal = pesoinflamable = pesorefrigerado = 0
                grande -= 24000
                p = []
        elif 24000 > grande >= 250:
            if c >= 250:
                transporte = Vehiculo(
                    "tren", len(p), 10000000, normal, refrigerado, E_L, inf, peso, solida, liquida, gas, pesonormal, pesoinflamable, pesorefrigerado)
                tren.append(transporte)
                c = 0
                peso = 0
                E_L = normal = refrigerado = inf = solida = liquida = gas = pesonormal = pesoinflamable = pesorefrigerado = 0
                grande -= 250
                p = []
        elif 250 > grande >= 10:
            if c >= 10:
                transporte = Vehiculo(
                    "avion", len(p), 1000000, normal, refrigerado, E_L, inf, peso, solida, liquida, gas, pesonormal, pesoinflamable, pesorefrigerado)
                Avion.append(transporte)
                peso = 0
                E_L = normal = refrigerado = inf = solida = liquida = gas = pesonormal = pesoinflamable = pesorefrigerado = 0
                c = 0
                grande -= 10
                p = []

        elif 10 > grande > 0:
            if c >= 0:
                transporte = Vehiculo(
                    "camion", len(p), 500000, normal, refrigerado, E_L, inf, peso, solida, liquida, gas, pesoinflamable, pesorefrigerado)
                Camion.append(transporte)
                peso = 0
                c = 0
                E_L = normal = refrigerado = inf = solida = liquida = gas = pesonormal = pesoinflamable = pesorefrigerado = 0
                grande -= 1
                p = []


def numero():
    todoslosvehiculos = barco+tren+Avion+Camion
    print("La cantidad total de vehiculos es: ", len(todoslosvehiculos))
    print("barcos totales: ", len(barco))
    print("tren totales: ", len(tren))
    print("Aviones totales: ", len(Avion))
    print("Camion totales: ", len(Camion))


def mostrar_vehiculos():
    for i in range(len(barco)):
        print(barco[i].__dict__)
    for i in range(len(tren)):
        print(tren[i].__dict__)
    for i in range(len(Avion)):
        print(Avion[i].__dict__)
    for i in range(len(Camion)):
        print(Camion[i].__dict__)


leer()
connormal()
conrefrigerado()
estanqueLiquidos()
estanqueIn()
cargando()
mostrar_vehiculos()
numero()


histbarco = []
histrefri = []
histest = []
histinf = []
for i in range(len(barco)):
    normales = Vehiculo.normal(barco[i])
    if normales > 0:
        histbarco.append(normales)
    refri = Vehiculo.refri(barco[i])
    if refri > 1:
        histrefri.append(refri)
    estanque = Vehiculo.estanqueL(barco[i])
    if estanque > 0:
        histest.append(estanque)
    inflam = Vehiculo.estanqueI(barco[i])
    if inflam > 0:
        histinf.append(inflam)
# Conocemos el numero de los que son diferentes restando los que son iguales
listahist = set(histbarco) - set(histrefri) - set(histest) - set(histinf)

ax = plt.subplot(231)
ax1 = plt.subplot(233)
ax.set_title('diferentes')
ax.hist(listahist, ec="black")
ax1.set_title("tipos")
ax1.hist(histipo1, ec='black')
plt.show()
