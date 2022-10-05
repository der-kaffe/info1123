from dataclasses import dataclass

# Creamos clase padre


@dataclass
class Contenedores:
    tipo_carga: str
    masa: str
    kilos: int


@dataclass
class Vehiculos:
    Costo = int
    capacidad = int


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
