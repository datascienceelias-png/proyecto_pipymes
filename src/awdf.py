import matplotlib.pyplot as plt

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
    plt.legend()
    plt.show()
print(comparación(4790,6945))


