# EL desafio del cubano: "Mantener una alimentacion saludable":

## Base de Datos
Se analizaron 17 productos en 30 Mypimes en Plaza de la Recolucion, Centro Habana y Guanabo

En la base de datos del valor nutricional, se tomaron los datos a partir de las etiquetas de los productos y también por la aplicación [Fitia](https://fitia.app/es/). Estos valores presentan los macronutrientes de 100 gramos de cada producto en crudo, excepto el huevo que se obtuvo a partir de la unidad y la leche se covirtió de [litro a gramos](https://share.google/oaWMIUlMNlFlo1M0C). Además de que la leche en todas las mipymes se encuentran en un envase de caja de 1 litro.
En el caso del atún, el producto es en lata y solo se consideró el peso escurrido de igual forma el paquete de pollo ya que contiene hueso

Los datos de la evoluvión del precio del huvo se obtuvieron 
 desde enero del  2024 en la [ONEI](https://www.onei.gob.cu/publicaciones-economico?field_categoria_de_temas_target_id=495&field_year_value=2025&title=)

El dato del salario medio en La Habana lo obtuve desde la [ONEI](https://www.onei.gob.cu/sites/default/files/publicaciones/2025-04/salario-medio-en-cifras-2024-edicion-2025.pdf)

## Desarrollo

En la sección **requisitos para una dieta saludable**  adapté las proporciones de la OMS/FAO para el contexto cubano distrubuyendo dentro del rango más cantidad de carbohidratos que de grasas y proteina porque son los carbohidratos más baratos.


### Funciones
La función **precio_promedio_lb** tiene como objetivo calcular el precio promedio que una persona debe gastar en comprar 1 libra de cada producto. Pero el peso escurrido de las diferentes latas de atún de todas las mipymes nunca llega a 1 libra, por eso el análisis se basa en el precio promedio para comprar 1 lata. 
En el caso de la leche, todos los envases son en una caja que contiene 1 litro de leche aproximadamente de 1030g que son aproximadamente 2,27 libras (1034/453.592). Por tanto el resultado de la funcion de la leche es el promedio de costo de un envace de 1 litro de leche. 
El resultado del de huevo es el promedio del valor de una unidad.

La función **costo_promedio_nutr** fue creada para conocer el precio de obtener 1 gramo del macronutriente que el usuario desea analizar. Además revela cuales los alimentos más económicos con mayor cantidad del macronutriente. La funcón se basa en las siguiente formula:

**cantidad total de macronutriente = (valor nutricional del producto /100) * Cantidad total en gramos del producto**

-La divición entre el valor nutricional y 100 es para conocer la proporción del macronutriente. Significa que cada gramo del producto tiene X gramos del macronutriente seleccionado. Al multiplicarlo por la cantidad total en gramos del producto devuelve el total en gramos del macronutriente

**costo por gramo = precio / cantidad total de macronutriente**

-Se divide el precio del producto entre la cantidad total de macronutriente que contiene y devuelve el costo para obtener 1 gramo de ese macronutriente. Un ejemplo práctico para entenderlo es el siguiente ejemplo: si compras una caja de lapices en 100cup y la caja contiene 10 lapices entonces cada lápiz te cuestó 10cup



### Gráficos
En el gráfico de lineas donde se visualiza la evolución de los precios de alguns productos desde el enero 2024 hasta noviembre 2025 se tiene en cuenta el siguiente análisis. Para conocer la variación del precio en estos años se tuvo en cuenta la fórmula:

Variación(%) = (U-P)/P *100

U es el precio final(2025-12),
P es el precio inicial(2024-01) y 
se divide entre P porque es el precio inicial a partir donde se efectuó la variación del precio.


           