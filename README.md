# ¿Es un lujo la vida saludable en Cuba?
***Estudiante: Elias Fabré Rosa***

***Proyecto de Ciencia de Datos - 1er Año***

En la Cuba actual, acceder a una alimentación básica es un desafío crítico debido a la desconexión entre los ingresos y el costo de vida. Con un salario promedio de 6,449 CUP, el trabajador estatal se enfrenta a un mercado donde productos esenciales consumen gran parte de su presupuesto.

Un ejemplo claro es el cartón de 30 huevos: con un precio promedio de 3,100 CUP, representa casi el 50% del salario mensual. Bajo esta realidad, un ciudadano solo podría costear un huevo diario, obteniendo apenas 6 gramos de proteína al día, una cifra insuficiente frente a los requerimientos biológicos mínimos.
Por tanto, este proyecto se fundamenta en la necesidad de documentar, mediante datos reales de 30 Mipymes y series temporales, cómo el factor económico se ha convertido en la principal barrera para la salud en Cuba, transformando la nutrición balanceada en un privilegio fuera del alcance de la mayoría.

## Estructura del repositorio
El archivo *análisis* contiene la historia basada en los datos junto con las 5 gráficos y el resultado de todo el análisis. En este sección se encuentra explicado como se llevó a cabo el proyecto
En la carpeta *data* se encuentra toda la base de datos utilizada y en la carpeta *src* están la biblioteca programada con las funciones utilizadas y el código de los gráficos. 

## Base de Datos

Se analizaron 17 productos en 30 mipymes de Plaza de la Revolución, Centro Habana y Guanabo. Los alimentos identificados —muslo de pollo, pechuga de pollo, hígado de pollo, picadillo de pollo, huevo, molleja de pollo, lomo de cerdo, atún, pierna de cerdo, solomillo de cerdo, garbanzos, frijoles negros, frijoles colorados, leche de vaca, arroz, codito y espaguetis— son frecuentes en estas empresas y pertenecen a grupos que la [OMS](https://www.who.int/es/news-room/fact-sheets/detail/healthy-diet) reconoce como necesarios para una dieta saludable, con el propósito de evaluar la relación costo-beneficio nutricional de cada uno.

En la base de datos del **valor nutricional**, se tomaron los datos a partir de las etiquetas de los productos y también por la aplicación [Fitia](https://fitia.app/es/). Estos valores presentan los macronutrientes de 100 gramos de cada producto en crudo, excepto el huevo que se obtuvo a partir de la unidad y la leche se covirtió de [litro a gramos](https://share.google/oaWMIUlMNlFlo1M0C). Además de que la leche en todas las mipymes se encuentran en un envase de caja de 1 litro.
En el caso del atún, el producto es en lata y solo se consideró el peso escurrido de igual forma el paquete de pollo ya que contiene hueso.

Los datos de la **evoluvión del precio** del arroz, huevo, lomo de cerdo, pierna de cerdo, frijoles negros y frijoles colorados se obtuvieron desde enero del  2024 hasta noviembre 2025 en la [ONEI](https://www.onei.gob.cu/publicaciones-economico?field_categoria_de_temas_target_id=495&field_year_value=2025&title=)

El dato del salario medio en La Habana lo obtuve desde la [ONEI](https://www.onei.gob.cu/sites/default/files/publicaciones/2025-04/salario-medio-en-cifras-2024-edicion-2025.pdf)

## Desarrollo

#### Gráficos
En el **gráfico de lineas** donde se visualiza la evolución de los precios de alguns productos desde el enero 2024 hasta noviembre 2025 se tiene en cuenta el siguiente análisis. Para conocer la variación del precio en estos años se tuvo en cuenta la fórmula:

Variación(%) = (U-P)/P *100

U es el precio final(2025-12),
P es el precio inicial(2024-01) y 
se divide entre P porque es el precio inicial a partir donde se efectuó la variación del precio.

En la **gráfica de pastel** sobre las proporciones de los macronutientes se adaptaron las proporciones de la [OMS/FON](https://iris.who.int/server/api/core/bitstreams/f06e1673-3689-4cb1-8a37-762a3e9c5360/content) para el contexto cubano distrubuyendo dentro del rango más cantidad de carbohidratos que de grasas y proteina porque son los carbohidratos más baratos. 


**Precio promedio de los productos**:
El gráfico muestra el precio promedio que una persona debe gastar en comprar 1 libra de los producto. Pero el peso escurrido de las diferentes latas de atún de todas las mipymes nunca llega a 1 libra, por eso el análisis se basa en el precio promedio para comprar 1 lata. En el caso de la leche, todos los envases son en una caja que contiene 1 litro de leche aproximadamente de 1030g que son aproximadamente 2,27 libras (1034/453.592). Por tanto el resultado de la función de la leche es el promedio de costo de un envace de 1 litro de leche. El resultado del huevo es el promedio del valor de una unidad.

**Precio por gramo de cada macronutriente**:
El gráfico muestra el costo promedio, en CUP, de obtener 1 gramo de cada macronutriente (proteínas, grasas y carbohidratos) a partir de cada producto analizado.
Para cada producto, la altura de cada segmento de la barra apilada representa el precio promedio por gramo de ese macronutriente.
Por lo tanto, mientras más alta es la barra asociada a un macronutriente en un producto, más costoso resulta obtener 1 gramo de ese macronutriente a partir de dicho producto. En consecuencia, para cubrir las necesidades diarias de macronutrientes, los productos con barras más altas implican un mayor gasto económico.
Además, es posible comparar directamente los precios por gramo de un mismo macronutriente entre diferentes productos: observando todos los segmentos de proteína (del mismo color) en todos los productos, se puede identificar cuál producto ofrece la proteína más barata por gramo. De igual manera, comparando los segmentos de grasas entre todos los productos se identifica cuál es la fuente más económica de grasas, y así sucesivamente con los carbohidratos. Esta comparación es fundamental para optimizar el presupuesto nutricional: si necesitas proteína económica, eliges el producto con el segmento de proteína más bajo; si necesitas carbohidratos baratos, identificas el producto con el segmento de carbohidratos más bajo, y así para cada macronutriente. Si una barra no tiene el color asociado a un macronutrientes significa que ese producto no contiene ese tipo de nutriente.
En este análisis podemos demostrar que los productos más baratos no implica que tenga más grasas, proteina o carbohidrato que otro producto más costoso.

**Comparación entre el salario promedio y el costo para consumir las proteinas**:
Para visualizar los datos correspondientes se tuvieron en cuenta el costo para obtener 1 gramo de proteina de los frijoles y el muslo de pollo. Si ese valor lo multiplicas por la cantidad de proteina que la persona que ingreso la cantidad de kcal que deberia consumir, retorna el precio que la persona debe gastar diario en ese productro y si se multiplica por 30 obtienes el gasto mensual. 




### Funciones
La función **precio_promedio_lb** tiene como objetivo calcular el precio promedio que una persona debe gastar en comprar 1 libra de cada producto. Pero el peso escurrido de las diferentes latas de atún de todas las mipymes nunca llega a 1 libra, por eso el análisis se basa en el precio promedio para comprar 1 lata. 
En el caso de la leche, todos los envases son en una caja que contiene 1 litro de leche aproximadamente de 1030g que son aproximadamente 2,27 libras (1034/453.592). Por tanto el resultado de la funcion de la leche es el promedio de costo de un envace de 1 litro de leche. 
El resultado del de huevo es el promedio del valor de una unidad.

La función **costo_promedio_nutr** fue creada para conocer el precio de obtener 1 gramo del macronutriente que el usuario desea analizar. Además revela cuales los alimentos más económicos con mayor cantidad del macronutriente. La funcón se basa en las siguiente formula:

*cantidad total de macronutriente = (valor nutricional del producto /100) * Cantidad total en gramos del producto*

Explicación: La divición entre el valor nutricional y 100 es para conocer la proporción del macronutriente. Significa que cada gramo del producto tiene X gramos del macronutriente seleccionado. Al multiplicarlo por la cantidad total en gramos del producto devuelve el total en gramos del macronutriente

*costo por gramo = precio / cantidad total de macronutriente*

Explicación: Se divide el precio del producto entre la cantidad total de macronutriente que contiene, y devuelve el costo para obtener 1 gramo de ese macronutriente. Un ejemplo práctico para entenderlo es el siguiente: si compras una caja de lapices en 100cup y la caja contiene 10 lapices entonces cada lápiz te cuestó 10cup


**calcular_macronutrientes**:
Calcula la cantidad de cada macronutriente que una persona debe consumir al dia dependiendo de la cantidad de kilocalorias que debe consumir. Para ello se utilizaron los datos a partir de un articulo publicado por la [Dirección General de Salud Pública de Madrid, España](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.comunidad.madrid/sites/default/files/doc/sanidad/1._valor_energetico_saber_mas.pdf&ved=2ahUKEwj3kZS22PORAxWuSTABHQuFO2oQFnoECBwQAw&usg=AOvVaw0c4toutOgq-dTvHpn6qLhp) donde 1 gramo de proteina y carbohidrato aporta 4 kcal y 1 gramo de grasas 9 kcal




           