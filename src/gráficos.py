import matplotlib.pyplot as plt


def proporcion_macronutrientes(
    proporcion=[75, 15, 10],
    macronutrientes=['Carbohidratos', 'Grasas', 'Proteínas']
   
):
    colores = ["#1F74B1", "#F38D30", "#CC243C"]
    explode = [0, 0, 0.1 ]
    plt.figure(figsize=(12, 7))
    plt.pie(proporcion, labels=macronutrientes, autopct='%1.1f%%', startangle = 60, explode=explode, colors=colores)
    plt.title('Proporción de Macronutrientes', fontsize=16, fontweight='bold')
    plt.legend()

   

    plt.show()


def barra_costo_promedio(productos, precio):
    plt.figure(figsize=(10, 6))
    plt.barh(productos,precio, color="#1F74B1")
    plt.title("Precio promedio de cada producto",fontweight='bold', fontsize=16)
    plt.xlabel("Precios",fontweight='bold', fontsize=12)
    plt.ylabel("Productos",fontweight='bold',  fontsize=12)

    
    
    plt.show()

def barra_apilada(producto, carbohidratos, proteínas, grasa):
    x = producto      #Nombre de los productos
    y1 = proteínas #valor 1proteina
    y2 = grasa        #valor 2
    y3 = carbohidratos    #valor 3
    colores = ["#1F74B1", "#F38D30", "#CC243C"]

    
    fig, ax = plt.subplots(figsize=(10, 6))
    #1era capa de la barra
    ax.bar(x, y1, color="#CC243C",label="Proteínas") 

     #2da capa
    ax.bar(x, y2, bottom=y1, color="#F38D30", label="Grasas")

    #3ra capa: Sumar las 2 capas anteriores para formar la capa faltante
    super_bottom = [p + g for p,g in zip(y1,y2)]
    ax.bar(x, y3, bottom=super_bottom, color="#1F74B1", label="Carbohidratos")

    plt.xticks(rotation=45, ha='right') #Rotacion
    ax.legend(loc="upper right") #Leyenda
    fig.tight_layout() 

    #Titulos y Etiquetas:
    ax.set_title("Precios promedio g/$ por macronutriente",fontweight='bold', fontsize=17)
    ax.set_xlabel("Productos",fontweight='bold', fontsize=12)
    ax.set_ylabel("Precios",fontweight='bold',  fontsize=12)

    plt.show()

def evolución_precios(precio, fecha):
    x = fecha
    y = precio

    plt.figure(figsize=(10, 6))
    plt.plot(x,y, marker = ".",linestyle='-', color = "b", label = "Precio del huevo" )
    

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.title("Evolución del precio", fontsize=16)
    plt.xlabel("Fechas", fontsize=12)
    plt.ylabel("Precios", fontsize=13)
    plt.grid(True, alpha=0.3) #Activar las cuadrículas para mejor visualización
    
    plt.show()


    



    


   




 
