

precio = {
    
    "Naranjas": 22.30,
    "Plátanos": 18.20,
    "Uvas": 25.50,
    "Manzanas": 15.75,
}

claves_ordenadas = sorted(precio, key=precio.get)

print(claves_ordenadas)


valores_ordenados = []

for clave in claves_ordenadas:
    valores_ordenados.append(round(precio[clave]))

diccionario = dict(zip(claves_ordenadas, valores_ordenados))

print(valores_ordenados)


#gr.barra_costo_promedio(claves_ordenadas, valores_ordenados)

lista = [6,3,4,5]
print(sorted.reverse(lista))