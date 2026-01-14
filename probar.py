import json
def cargar_json(ruta_relativa):
    with open(ruta_relativa, "r" , encoding="utf-8") as archivo:
        dato = json.load(archivo)
    return dato

mipyme = cargar_json("data/mipymes.json")

def promedio(lista):
    """
    Calcula el promedio de una lista
    """
    suma = 0
    for i in lista:
        suma += i
    if len(lista) > 0:
        return suma / len(lista)
    return 0

proteina = [20, 23, 17, 16, 6, 18, 22, 17.5, 23, 21, 22, 22, 22.5, 3, 7, 15, 13]
productos = ['muslo de pollo', 'pechuga de pollo', 'higado de pollo', 'picadillo de pollo', 'huevo', 'molleja de pollo', 'lomo de cerdo', 'atún', 'pierna de cerdo', 'solmillo de cerdo', 'garbanzos', 'frijoles negros', 'frijoles colorados', 'leche de vaca', 'arroz', 'codito', 'espaguetis']
#rint(len(lista))


def costo_promedio_nutr(data_mipyme, productos, valor_nutricional):
    """
    Calcula el costo promedio de 1 g de proteína para cada producto,

    EL argumento "producto" es una lista con los productos para analizar y el "valor nutricional" es el macronutriente que se desea analizar el precio


    """
    salida = {}

    for i, nombre_nutri in enumerate(productos): # El código enumerate lo uso para obtener tanto como el nombre del producto como su posición para luego buscar en la lista del valor nutricional del producto correspondiente
        lista_costos = [] #Esta lista es para calcular el costo promedio, se reinicia los valores en cada iteración del for principal

        for mipyme in data_mipyme["mipyme"]:
            for producto in mipyme["productos"]: 

                if producto["nombre"] == "huevo": # EL costo del huevo no es por 100 gramos sino por unidad 
                    precio = float(producto["precio"])# Convertir en float, de lo contrario da error porque se lee como string
                    gramos = float(producto["cantidad"])
                    macro_total = valor_nutricional[i] * gramos #EL inidice i es para buscar en la lista del valor nutricional el producto correspondiente

                    if macro_total > 0: # Evitar división por cero cuando no hay carbohidratos en algunos alimentos
                        costo_por_gramo = precio / macro_total
                        lista_costos.append(costo_por_gramo)
                        
                        continue #si en la iteración se encuentra el huevo, se salta los demas codigos y salta a la mipyme siguiente

                elif producto["nombre"] == nombre_nutri:
                        gramos = float(producto["cantidad"]) 
                        precio = float(producto["precio"])

                        macro_total = (valor_nutricional[i] / 100) * gramos

            if macro_total > 0: # Evitar división por cero cuando no hay carbohidratos en algunos alimentos
                    costo_por_gramo = precio / macro_total
                    lista_costos.append(costo_por_gramo)

            
            salida[nombre_nutri] = round(promedio(lista_costos), 2) #La función retorna un diccionario llamado "salida" donde cada llave es el nombre del producto y su valor es el precio redondeado

    return salida


print(costo_promedio_nutr(mipyme, productos, proteina))
    