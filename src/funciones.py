import json
productos = ['muslo de pollo', 'pechuga de pollo', 'higado de pollo', 'picadillo de pollo', 'huevo', 'molleja de pollo', 'lomo de cerdo', 'atún', 'pierna de cerdo', 'solmillo de cerdo', 'garbanzos', 'frijoles negros', 'frijoles colorados', 'leche de vaca', 'arroz', 'codito', 'espaguetis']

def cargar_json(ruta_relativa):
    with open(ruta_relativa, "r" , encoding="utf-8") as archivo:
        dato = json.load(archivo)
    return dato

    

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



def costo_promedio_nutr(data_mipyme, productos, valor_nutricional):
    """
    Calcula el costo promedio de 1 g de proteína para cada producto,
    """
    output = {}

    for i, nombre_nutri in enumerate(productos):
        lista_costos = [] #Esta lista es para calcular el costo promedio, se reinicia los valores en cada iteracion

        for mipyme in data_mipyme["mipyme"]:
            for producto in mipyme["productos"]:

                if producto["nombre"] == "huevo": # EL costo del huevo no es por 100 gramos sino por unidad 
                    precio = float(producto["precio"])
                    gramos = float(producto["cantidad"])
                    macro_total = valor_nutricional[i] * gramos

                    if macro_total > 0: # Evitar división por cero cuando no hay carbohidratos en algunos alimentos
                        costo_por_gramo = precio / macro_total
                        lista_costos.append(costo_por_gramo)
                        
                        continue

                elif producto["nombre"] == nombre_nutri:
                        gramos = float(producto["cantidad"]) # Convertir en float, de lo contrario da error porque se lee como string
                        precio = float(producto["precio"])

                        macro_total = (valor_nutricional[i] / 100) * gramos

            if macro_total > 0: # Evitar división por cero cuando no hay carbohidratos en algunos alimentos
                costo_por_gramo = precio / macro_total
                lista_costos.append(costo_por_gramo)

        
        output[nombre_nutri] = round(promedio(lista_costos), 2)

    return output





def calcular_macronutrientes(kcal):
    """
    Calcula la cantidad de macronutrientes en gramos según las calorías necesarias.
    """
    carbohidratos = (0.74 * kcal) / 4
    grasas = (0.15 * kcal) / 9
    proteinas = (0.10 * kcal) / 4

    return {
        "carbohidratos_g": round(carbohidratos, 2),
        "grasas_g": round(grasas, 2),
        "proteinas_g": round(proteinas, 2)
    }


def precio_promedio_lb(listado_de_productos, mipyme):

    """
    Calcula el precio promedio de 1 libra de cada  prodcutos,

    El valor del huevo se tiene en cuenta por una unidad,

    En caso de las latas de atún como su peso es menor a de una libra, el analisis seria para saber el precio promedio para comprar una lata de atun


    """

    output = {}
    for producto in listado_de_productos:
        lista_precio = [] 

        for dic in mipyme["mipyme"]:
            for products in (dic["productos"]):
                #print(products)
        
                if producto == "huevo" and products["nombre"] == "huevo":
                    precio_unidad = round((float(products["precio"]))/ 30) # El cartón de huevo siempre tiene 30 unidades
                    
                    lista_precio.append(precio_unidad) 

                elif producto == "atún" and products["nombre"] == "atún":  
                    lista_precio.append(float(products["precio"]))

                elif products["nombre"] == producto and producto!= "huevo" and producto !="atún":
                    lb = float(products["cantidad"]) / 453.592 #Convertir en float los datos necesrios porque python los reconoce como str
                    precio_lb = float(products["precio"]) / lb
                    lista_precio.append(precio_lb)
                
                    
        output[producto] = round(promedio(lista_precio), 2)    

                    
        if producto == "leche de vaca":
            # convertir el promedio por libra al promedio por envase de 1030 g
            promedio_lb = promedio(lista_precio)
            libras_envase = 1030 / 453.592
            output[producto] = round(promedio_lb * libras_envase, 2)
        else:
            output[producto] = round(promedio(lista_precio), 2)

    return output

def datos_evolución_precios(precios, producto):
    """
    Calcula el precio promedio mensual de un producto específico a lo largo del tiempo.

    El argumento "precios" es un diccionario donde las claves son meses y los valores son el precio de los productos.

    El argumento "producto" es el nombre del producto para el cual se desea ver la evolución de precios.

    Retorna dos listas: una con las fechas y otra con los precios promedios correspondientes.
    """

    fechas = []
    promedio_precio = []
    for mes in precios.keys(): #Iterar por cada mes 
        fechas.append(mes) # las llaves son las fechas

         #los datos del precio del huevo son por unidad, por eso se multiplica por 30 para obtener el precio del cartón
        if producto == "huevo" and producto in precios[mes]: #acceder al producto en ese mes
            datos_producto = precios[mes][producto]
            promedio = (round((datos_producto["min"] + datos_producto["max"]) / 2)) * 30
            promedio_precio.append(promedio)
            continue
            
        elif producto in precios[mes]:
            datos_producto = precios[mes][producto]
            promedio = round((datos_producto["min"] + datos_producto["max"]) / 2) # Calcular el promedio
            promedio_precio.append(promedio)
            


            

       

    

    return fechas, promedio_precio




    
    

 