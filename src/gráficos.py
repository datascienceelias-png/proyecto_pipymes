import matplotlib.pyplot as plt

def evolución_precios(precio, fecha):
    x = fecha
    y = precio

    plt.figure(figsize=(10, 6))
    plt.plot(x,y, marker = ".",linestyle='-', color = "b", label = "Evolución de los precios")
    plt.axhline(3547, color='r', linestyle='--', label= "55% del salario promedio")
    

    plt.xticks(rotation=45, ha='right') #rotar las etiquetes del eje x  

    plt.tight_layout() # para mejorarla visualizacion en el notbook

    plt.title("Evolución del precio del carton de huevo",fontweight="bold", fontsize=16)

    plt.xlabel("Fechas", fontweight="bold", fontsize=12)

    plt.ylabel("Precios", fontweight="bold", fontsize=13)

    plt.grid(True, alpha=0.3) #Activar las cuadrículas para mejor visualización
    #"alpha es para la intensidad que se quiere visualizar las cuadriculas"

    plt.legend()
    
    plt.show()




def proporción_macronutrientes(
    proporcion=[75, 15, 10],
    macronutrientes=['Carbohidratos', 'Grasas', 'Proteínas']
   
):
    colores = ["#3498db", "#F38D30", "#e74c3c"]
    explode = [0, 0, 0.1 ]

    plt.figure(figsize=(12, 7))

    plt.pie(proporcion, labels=macronutrientes, autopct='%1.1f%%', startangle = 60, explode=explode, colors=colores)

    plt.title('Proporción de Macronutrientes', fontsize=16,fontweight='bold')

    plt.legend()

   

    plt.show()




def barra_costo_promedio(productos, precio):

    plt.figure(figsize=(10, 6))

    plt.barh(productos, precio, color="#3498db")

    plt.title("Precio promedio de los carnicos",fontweight='bold', fontsize=16)


    plt.xlabel("Precios",fontweight='bold', fontsize=12)

    plt.ylabel("Productos",fontweight='bold',  fontsize=12)

    

    plt.show()




def barra_apilada(producto, carbohidratos, proteínas, grasa):
    x = producto      #Nombre de los productos
    y1 = proteínas #valor 1proteina
    y2 = grasa        #valor 2
    y3 = carbohidratos    #valor 3
    #colores = ["#1F74B1", "#F38D30", "#CC243C"]

    
    fig, ax = plt.subplots(figsize=(10, 6))

    #1era capa de la barra
    bar1 = ax.bar(x, y1, color="#e74c3c",label="Proteínas") 
    ax.bar_label(bar1, labels=y1, label_type="center") #"ax.bar_label" anaidir valores numericos a las barras

     #2da capa
    bar2 = ax.bar(x, y2, bottom=y1, color="#F38D30", label="Grasas")
    ax.bar_label(bar2, labels=y2, label_type="center") #la función de esta parte es para colocar los valores encima o dentro de cada barra apilada

    #3ra capa: Sumar las 2 capas anteriores para formar la capa faltante
    super_bottom = [p + g for p,g in zip(y1,y2)]
    bar3 = ax.bar(x, y3, bottom=super_bottom, color="#3498db", label="Carbohidratos")

    ax.bar_label(bar3, labels=y3, label_type="edge")

    plt.xticks(rotation=35, ha='right') #Rotación

    ax.legend(loc = "best") #Leyenda 
    
    fig.tight_layout() 

    #Títulos y Etiquetas:
    ax.set_title("Precios promedio g/$ por macronutriente",fontweight='bold', fontsize=17)
    ax.set_xlabel("Productos",fontweight='bold', fontsize=12)
    ax.set_ylabel("Precios",fontweight='bold',  fontsize=12)


    plt.show()




def comparación(frutas, verduras):
    salario_promedio = 6449
    
    eje_x = ["Salario promedio", "Frutas", "Verduras"]
    porcentajes_eje_y = []

    valores = [salario_promedio, frutas, verduras]

    for i in valores: #Para obtener el porcetaje de los precios de las frutas respecto al salario promedio
        x = (i/salario_promedio) * 100
        porcentajes_eje_y.append(x)

    color = ['#3498db', '#2ecc71', '#e74c3c']  
              

    plt.figure(figsize=(10,6))

    plt.bar(eje_x, porcentajes_eje_y, color = color)
    plt.title("Porcentaje del precio de frutas y verduras respecto al salario", fontsize=17,fontweight="bold")
    plt.ylabel("Porcentaje (%)", fontsize=14, fontweight="bold")

    plt.ylim(0,150) # Esto permite mostrara valores que superen en 100%. Lo utilizo para el caso de las verduras ya que sobrepasa el salario promedio

    plt.axhline(y=100, color = "b", linestyle ="--") #Esto crea una linea horizontal en el valor de 100%, coincide con el salario promedio

    #Mostrar el % arriba de los graficos
    for i in range(3): #Utilizo range(3) xq tengo 3 graficos para escribir arriba sus valores correspondientes
        #en esta parte hay 3 elementos que necesito, las cordenadas donde se encuentra la barra y el texto que quiero mostrar
        plt.text(i,porcentajes_eje_y[i], f"{porcentajes_eje_y[i]:.2f}%", ha="center", va="bottom") 

    plt.tight_layout() 
    
    plt.show()






        






    



    


   




 
