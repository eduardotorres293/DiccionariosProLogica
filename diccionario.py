animales = ("perro", "guepardo", "tigre", "jirafa", "cebra", "pinguino", "albatros", "caballo")

hechos = {
    "TienePelo": ("perro", "guepardo", "tigre", "jirafa", "cebra", "caballo"),
    "DaLeche": ("perro", "guepardo", "tigre", "jirafa", "cebra", "caballo"),
    "TienePlumas": ("pinguino", "albatros"),
    "Vuela": ("albatros"),
    "PoneHuevos": ("pinguino", "albatros"),
    "ComeCarne": ("guepardo", "tigre", "perro"),
    "TienePezuñas": ("jirafa", "cebra", "caballo"),
    "Leonado": ("guepardo"),
    "ManchasOscuras": ("guepardo", "jirafa"),
    "RayasNegras": ("tigre", "cebra"),
    "CuelloLargo": ("jirafa"),
    "Nada": ("pinguino"),
    "BlancoYNegro": ("pinguino"),
    "VuelaMuyBien": ("albatros"),
    "Mamifero": ("perro", "guepardo", "tigre", "jirafa", "cebra", "caballo"),
    "Ave": ("pinguino", "albatros"),
    "Carnivoro": ("guepardo", "tigre", "perro"),
    "Ungulado": ("jirafa", "cebra", "caballo"),
    "Guepardo": ("guepardo"),
    "Tigre": ("tigre"),
    "Jirafa": ("jirafa"),
    "Cebra": ("cebra"),
    "Pinguino": ("pinguino"),
    "Albatros": ("albatros"),
    "Perro": ("perro"),
    "Domesticado": ("perro"),
    "CuatroPatas": ("perro"),
    "ExcelenteOlfato": ("perro"),
    "Ladra": ("perro"),
    "Herbivoro": ("caballo"),
    "TieneCrin": ("caballo"),
    "TienenOrejasErgidas": ("caballo"),
    "TieneColaLarga": ("caballo"),
}

def esHecho(x, y):
    return y in hechos.get(x, ())

print("El perro tiene pelo?", esHecho("TienePelo", "perro"))
print("El perro es mamifero?", esHecho("Mamifero", "perro"))
print("El perro es ave?", esHecho("Ave", "perro"))
print("El guepardo es carnivoro?", esHecho("Carnivoro", "guepardo"))
print("El guepardo es leonado?", esHecho("Leonado", "guepardo"))
print("El tigre tiene rayas negras?", esHecho("RayasNegras", "tigre"))
print("El tigre es guepardo?", esHecho("Guepardo", "tigre"))
print("La jirafa es ungulado?", esHecho("Ungulado", "jirafa"))
print("La jirafa tiene cuello largo?", esHecho("CuelloLargo", "jirafa"))
print("La cebra es ungulado?", esHecho("Ungulado", "cebra"))
print("La cebra tiene rayas negras?", esHecho("RayasNegras", "cebra"))
print("El pinguino nada?", esHecho("Nada", "pinguino"))
print("El pinguino es ave?", esHecho("Ave", "pinguino"))
print("El albatros vuela muy bien?", esHecho("VuelaMuyBien", "albatros"))
print("El albatros es pinguino?", esHecho("Pinguino", "albatros"))
print("El caballo tiene crin?", esHecho("TieneCrin", "caballo"))
print("El caballo es herbivoro?", esHecho("Herbivoro", "caballo"))
print("El caballo come carne?", esHecho("ComeCarne", "caballo"))