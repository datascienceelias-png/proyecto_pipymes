import json


def cargar_json(ruta_relativa):
    with open(ruta_relativa, "r" , encoding="utf-8") as archivo:
        dato = json.load(archivo)
    return dato



def frutas(platano=129, fruta_bomba=150, guayaba=200):
    """
    Docstring for vegetales_verduras
    
    :param platano: El precio de 1 libra 
    :param fruta_bomba: Precio de 1 libra
    :param guayaba: Precio de 1 libra
    """
    p = platano * 10 
    f = fruta_bomba * 10
    g = guayaba * 10

    costo_mensual = p+f+g
    
    return p,f,g,costo_mensual



def verduras(r=500, p=500, col=600, t=600, z=500):
    gramoR = r / 453
    r_100 = 100 * gramoR
    
    gramoP = p / 453  
    p_100 = 100 * gramoP
    
    gramoCol = col / 453
    col_100 = 100 * gramoCol
    
    gramoT = t / 453
    t_100 = 100 * gramoT
    
    gramoZ = z / 453
    z_100 = 100 * gramoZ
    
    
    return r_100, p_100, col_100, t_100, z_100



def leche_polvo(precio_leche, precio_azucar):
    """
    Docstring for leche_polvo
    
    :param precio_leche: Precio promedio de 1 libra
    :param precio_azucar: Precio promedio de 1 libra
    """ 
    kg_leche = precio_leche*2.2 #Obtener el precio promedio de 1kg
    precio_gramo = kg_leche/1000 #Obtener precio por gramo
    cuchurada2_leche = 40* precio_gramo # Obtener el precio de obtener 40 gramo de leche en polvo que son para preparar un vaso 

    kg_azucar = precio_azucar*2.2
    precio_gramoA = kg_azucar/1000
    cuchurada1_azucar = 15 * precio_gramoA

    precio_vaso = cuchurada1_azucar + cuchurada2_leche #Obtener el precio total para 1 vaso de leche
 
    bolsa_leche = 1000/40 #Cantiada de vasos de leche de 8onzas que puedes hacer con 1kg de leche en polvo
    

    #valor_leche = [8, 11, 8] #Valor nutricional de la leche (proteina, carbohidrato, grasas)
    #valor_azucar = [0,15, 0]

    valor_nutricional = {"Proteina": 10, "Carbohidrato": 30, "Grasas": 10} #Sume la cantidad de carbohidratos de ambos productos

    return precio_vaso, bolsa_leche, valor_nutricional



def datos_evolución_precios(precios, producto):
    """
    Calcula el precio promedio mensual de un producto específico a lo largo del tiempo.

    El argumento "precios" es un diccionario donde las claves son meses y los valores son el precio de los productos.

    El argumento "producto" es el nombre del producto para el cual se desea ver la evolución de precios.

    Retorna dos listas: una con las fechas y otra con los precios promedios correspondientes.
    """

    fechas = []
    promedio_precio = []
    
    for mes in precios.keys(): #iterar sobre cada mes en el diccionario de precios, cada llave principal es un mes

        if producto == "huevo" and producto in precios[mes]: #Verificar si el producto existe en ese mes
            datos_producto = precios[mes][producto] #Obtener los datos del producto en ese mes

            promedio = (round((datos_producto["min"] + datos_producto["max"]) / 2)) * 30 #multiplicar por 30 para obtener el precio del cartón

            fechas.append(mes) #Agregar el mes y el precio a la lista
            promedio_precio.append(promedio)


    return fechas, promedio_precio



def calcular_macronutrientes(kcal):
    """
    Calcula la cantidad de macronutrientes en gramos según las calorías necesarias.
    """
    carbohidratos = (75/100 * kcal) / 4
    grasas = (15/100 * kcal) / 9
    proteinas = (10/100 * kcal) / 4

    return {
        "carbohidratos": round(carbohidratos),
        "grasas": round(grasas),
        "proteinas": round(proteinas)
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
            for products in (dic["productos"]): #products es una lista que tiene a los productos de una mipyme
                #print(products)
        
                if producto == "huevo" and products["nombre"] == "huevo":
                    precio_unidad = round((float(products["precio"]))/ 30) # El cartón de huevo siempre tiene 30 unidades
                    
                    lista_precio.append(precio_unidad) 
                    break


                elif producto == "atún" and products["nombre"] == "atún":  
                    lista_precio.append(float(products["precio"]))
                    break

                elif producto == "leche en polvo" and products["nombre"] == "leche en polvo":
                    lista_precio.append(float(products["precio"]))
                    break
                    
                elif products["nombre"] == producto and producto!= "huevo" and producto !="atún" and producto != "leche en polvo":
                    lb = float(products["cantidad"]) / 453.592 #Convertir en float los datos necesrios porque python los reconoce como str
                    precio_lb = float(products["precio"]) / lb
                    lista_precio.append(precio_lb)
                
                    
        output[producto] = round(sum(lista_precio) / len(lista_precio))    

        
    return output




def costo_promedio_nutr(data_mipyme, productos, valor_nutricional):
    """
    Calcula el costo promedio de 1 g de proteína para cada producto,

    EL argumento "producto" es una lista con los productos para analizar y el "valor nutricional" es el macronutriente que se desea analizar el precio. En estas listas coincide la posicion del
    nombre del producto con su valor nutricional.

    """
    salida = {}

    for i, nombre_nutri in enumerate(productos): # El código enumerate lo uso para obtener tanto como el nombre del producto como su posición para luego buscar en la lista del valor nutricional del producto correspondiente
        lista_costos = [] #Esta lista es para calcular el costo promedio, se reinicia los valores cuando en la iteracion cambia de producto

        for mipyme in data_mipyme["mipyme"]:
            for producto in mipyme["productos"]: #productos son diccionarios que contiene los datos de cada producto

                if producto["nombre"] == "huevo": 
                    precio = producto["precio"]
                    cantidad = producto["cantidad"]
                    macro_total = valor_nutricional[i] * cantidad #EL indice i es para buscar en la lista del valor nutricional el producto correspondiente
                    # EL valor nutricional del huevo no es por 100 gramos sino por unidad por eso no se divide entre 100
                    #Además el valor nutricional del huevo y la cantidad de huevo en los cartones que hay en las mipymes siempre es la misma. Lo único que cambia es el precio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           


                    if macro_total > 0: # Evitar división por cero cuando no hay proteina, grasa o carbohidrato en algunos alimentos
                        costo_por_gramo = precio / macro_total
                        lista_costos.append(costo_por_gramo)
                        
                        break #si en la iteración se encuentra el huevo, se salta los demas cádigos y se busca otra mipyme

                elif producto["nombre"] == nombre_nutri:
                        gramos = producto["cantidad"] 
                        precio = producto["precio"]

                        macro_total = (valor_nutricional[i] / 100) * gramos
                        #Como cada producto tiene un peso distinto, el valor nutricional de ese producto es mayor. Por eso se multiplica el valor nutricional por la cantidad del producto dividido entre 100

            if macro_total > 0: # Evitar división por cero cuando no hay carbohidratos en algunos alimentos
                    costo_por_gramo = precio / macro_total
                    lista_costos.append(costo_por_gramo)

        if len(lista_costos) > 0: # Verificar que la lista no esté vacía para evitar división por cero
            salida[nombre_nutri] = round(sum(lista_costos) / len(lista_costos), 2)#La función retorna un diccionario llamado "salida" donde cada llave es el nombre del producto y su valor es el precio redondeado
        else: salida[nombre_nutri] = 0.0 #En caso de que la lista esté vacía, asignar un valor de 0.0 para evitar errores

    return salida
        

