from dataclasses import dataclass

# Creamos clase padre


@dataclass
class Transporte:
    tipo_carga: str
    masa: str
    tonelaje: int


@dataclass
# La clase hija se crea así, nombre_clase_hija(clase_padre)
class Contenedor_P(Transporte):
    tamanho: str = "pequeño"


@dataclass
class Contenedor_G(Transporte):
    tamanho: str = "grande"


@dataclass
class Estanque_P(Transporte):
    tamanho: str = "pequeño"


@dataclass
class Estanque_G(Transporte):
    tamanho: str = "grande"
