# ¿Es un lujo la vida saludable en Cuba?
***Estudiante: Elias Fabré Rosa***

***Facultad de Matemática y Computación (MATCOM), La Habana***

***Proyecto de Ciencia de Datos - 1er Año***

En la Cuba actual, acceder a una alimentación saludable es un desafío crítico debido a la desconexión entre los ingresos y el costo de vida. Con un salario promedio de [6,449](https://www.onei.gob.cu/sites/default/files/publicaciones/2025-04/salario-medio-en-cifras-2024-edicion-2025.pdf) CUP, el trabajador estatal se enfrenta a un mercado donde productos esenciales consumen gran parte de su presupuesto.
Por tanto, este proyecto se fundamenta en la necesidad de documentar, mediante datos reales de 30 Mipymes y series temporales, cómo el factor económico se ha convertido en la principal barrera para la salud en Cuba, transformando la nutrición balanceada en un privilegio fuera del alcance de la mayoría.

## Base de Datos

Se analizaron 17 productos en 30 mipymes de Plaza de la Revolución, Centro Habana y Guanabo. Los alimentos identificados: 

- Muslo de pollo
- Pechuga de pollo
- Higado de pollo
- Picadillo de pollo
- Huevo
- Molleja de pollo
- Lomo de cerdo
- Atún
- Pierna de cerdo
- Garbanzos
- Frijoles negros
- Frijoles colorados
- Arroz
- Codito
- Espaguetis
- Leche en polvo
- Azúcar blanca.

Los datos se guardaron en ***mipymes.json***. Su estrucura es:

La llave `mipyme` es la principal del json y contiene una lista con varios diccionarios, cada diccionario es una mipyme diferente. En cada mipyme encontramos las siguientes llaves con el tipo de dato de guarda:

 `id`: para identificar el número de identidad de la mipyme (float)

`nombre`: para registrar el nombre de la mipyme (string), 

`ubicación`: tiene como valor una serie de números que es la ubibación en el mapa de Google maps para poder encontrar la mipyme  (string),

`productos`:  es una lista que contiene diccionarios, cada diccionario es un producto diferente. En estos diccionarios hay como llave:

`nombre`: para registrar el nombre del producto(string),

`cantidad`:para guardar la cantidad en gramos o las unidades en caso del huevo (float),

`unidad`: aquí está el peso de medida que casi siempre es en gramos excepto el huevo que se registra en unidad (string)

`precio`: es el costo en cup del producto (float)

Los datos fueron obtenidos desde finales de noviembre y principios de diciembre del 2025.


Tambien se analizaron entre frutas y verduras 6 diferente y se guardaron en el archivo ***frutas_verduras.json***:

- Fruta bomba
- Guayaba
- Platano fruta
- Pepino
- Tomate
- Zanahoria

La estructura del archivo esta divido en 2 llaves principales, `frutas` y `verduras`, cada uno tiene una lista donde cada diccionario de este es un producto diferente asociado al tipo de alimento. Las claves son y el tipo de dato que guardason:

`unit`: Es la unidad de medida del producto (string)

`cantidad`: Es la cantidad de la unidad de medida (float)

`precio`: Es el precio del producto asociado a la cantidad (float)


Estos alimentos son frecuentes en el mercado cubano y pertenecen a los grupos que la [OMS](https://www.who.int/es/news-room/fact-sheets/detail/healthy-diet) reconoce como necesarios para una dieta saludable.

Los datos de  ***evoluvión_precios.json*** en cada llave principal está la fecha donde se registró el precio de los productos, y contiene otra llave para asociar el nombre del producto que se va a guardar. Los productos guardados en este archivo son: arroz, huevo, lomo de cerdo, pierna de cerdo, frijoles negros y frijoles colorados. 

La clave `unit` es la unidad de peso del producto que son *lb* para referirse a 1 libra del producto y *unidad* para asociar solamente a 1 huevo. (string)

La clave `min` y `max` es el precio mínimo y máximo registrado en el mes correspondiente a la llave de la fecha. 
Estos datos están registrados desde enero del 2024 hasta noviembre 2025 en la [ONEI](https://www.onei.gob.cu/publicaciones-economico?field_categoria_de_temas_target_id=495&field_year_value=2025&title=). 


El archivo ***valor_nutricional.json*** contiene los datos nutricionales principales (grasas, proteínas y carbohidratos) para cada producto. Por general, estos valores corresponden a una porción de 100 gramos del alimento en crudo. Las excepciones son: el huevo, cuyos datos se obtuvieron por unidad; el atún, por los nutrientes de una lata; el muslo de pollo, considerando solo la carne sin hueso; la leche en polvo, cuya cantidad de 40 gramos (equivalente a 2 cucharadas con una pequena loma) necesaria para preparar un vaso de 8 onzas o 240 ml y la azucar es el valor nutricional de 1 cucharada (15 gramos).

Cada llave del json es el nombre del producto, las claves son los macronutrientes y los valores correspondiente la cantidad en gramo
Se tomaron los datos a partir de las etiquetas de los productos y también por la aplicación [Fitia](https://fitia.app/es/). 




### Funciones programadas utilizadas en el análisis 



***cargar_json***: Esta función es para cargar los datos necesarios en el archivo *análisis.ipynb* para el proyecto

***frutas***: Calcula el costo para consumir 10 libras de cada una de las frutas durante 30 días. Los datos necesarios se obtuvieron a partir del arhcivo *frutas_verduras*.

***verduras***: Retorna el costo de consumir 100g de remolacha, pepino, tomate y zanahoria. Para ello primero se obtiene el costo de consumir 1g de cada verdura y luego se multiplica por 100 que es la cantidad de gramos a consumir. Los datos se obtuvieron a partir del arhcivo *frutas_verduras*

***leche en polvo**: Retorna el precio de obtener 1 vaso de 8oz o 240ml de leche a partir de una bolsa de leche en polvo de 1kg su valor nutricional y la cantidad de vasos que puedes hacer con una bolsa. Para obtener este resultado primero se obtiene el precio de obtener 15 g de azúcar y 40 g de leche en polvo, que son los necesarios para preparar un vaso (sin tener en cuenta la proporción infantil), luego se suma este costo y se obtiene el resultado esperado. Además si divides 40g entre 1000g obtienes la cantidad de vasos que puedes hacer con una bolsa de 1kg de leche en polvo y el valor nutricional es la suma de los nutrientes del archvio *valor_nutricional.json".


***datos_evolución_precios***: Es utilizada para limpiar los datos del archivo "evolución_precios.josn" para graficar la evolución del precio del huevo. Retorna 2 listas una de con las fechas donde se registró el precio y la otra con los precios promediodonde coincide los indices. 


***calcuar_macronutrientes***:
A partir de la cantidad de kcal que el usuario incerte en el argumento de la función, esta devuelve la cantidad en gramo de proteina, grasa y carbohidrato que este usuario debe consumir diario. Para ello se utilizaron los datos a partir de un articulo publicado por la [Dirección General de Salud Pública de Madrid, España](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.comunidad.madrid/sites/default/files/doc/sanidad/1._valor_energetico_saber_mas.pdf&ved=2ahUKEwj3kZS22PORAxWuSTABHQuFO2oQFnoECBwQAw&usg=AOvVaw0c4toutOgq-dTvHpn6qLhp) donde 1 gramo de proteina y carbohidrato aporta 4 kcal y 1 gramo de grasas 9 kcal. Para obtener la cantidad de cada macronutriente se utilizó la siguiente fórmula

cantidad_macronutriente =(PM/100 * kcal) / A

-PM es la proporción en % del macronutriente que se necesita 
-Kcal es la cantidad de kilocalorías que el usurio debe consumir diario
-A es la cantidad de kcal que aporta el macronutriente que se necesita

***precio_promedio_lb***: tiene como objetivo calcular el precio promedio que una persona debe gastar en comprar 1 libra de cada producto de las mipymes. Excepto las latas de atún ya que el peso escurrido de las diferentes latas de atún de todas las mipymes nunca llega a 1 libra, por eso el análisis se basa en el precio promedio para comprar 1 lata. Además el resultado del de huevo es el promedio del valor de una unidad y en el caso de la leche en polvo es el precio promedio de obtener una bolsa de 1 kg. 
Para obtener este resultado primero se itera en una lista que contiene los productos para anlizar, luego en el diccionario *mipyme* donde estan todos los datos necesario y luego en una lista interna de esta base de datos (*productos*) donde estan los productos de las mipymes. En cada iteración de la lista que contiene los productos se busca su precio en todas las mipymes, se añaden a una lista y luego se calcula su precio promedio. En el caso de las excepciones se utiliza una condición para que cuando la ieración interna sea uno de esos productos se calcule de forma independiente.


***costo_promedio_nutr***: fue creada para conocer el precio de obtener 1 gramo del macronutriente que el usuario desea analizar. Además revela cuales los alimentos más económicos con mayor cantidad del macronutriente. La funcón se basa en las siguiente formula:

*cantidad total de macronutriente = (valor nutricional del producto /100) * Cantidad total en gramos del producto*

Explicación: La divición entre el valor nutricional y 100 es para conocer la proporción del macronutriente. Significa que cada gramo del producto tiene X gramos del macronutriente seleccionado. Al multiplicarlo por la cantidad total en gramos del producto devuelve el total en gramos del macronutriente.
ejemplo si el frijol negro tiene 22g de proteina entonces 22/100 = 0,22g de proteina aporta 1 gramo de frijoles y si peso del producto es de 500g, 
0,22*500 = 110g de proteina total

*costo por gramo = precio / cantidad total de macronutriente*

Explicación: Se divide el precio del producto entre la cantidad total de macronutriente que contiene, y devuelve el costo para obtener 1 gramo de ese macronutriente. Por ejemplos si el precio del frijol es de 700cup, 700/110g = 6.36cup el costo de 1 gramo de proteina.

A diferencia de otros alimentos donde el peso varía y determina la cantidad total de nutrientes, el huevo se vende en un formato estándar por unidades. Debido a esta cantidad fija, se omite la división entre 100 (que busca la proporción por gramo) y se procede a multiplicar directamente el valor nutricional de un huevo por el número de unidades en el cartón para obtener el total del macronutriente.

En cada iteración, se busca el producto correspondiente en todas las MiPYMEs disponibles. Por cada coincidencia encontrada, se calcula el costo de obtener un gramo del macronutriente seleccionado y se añade a una lista. Una vez finalizada la búsqueda en todos los establecimientos, se calcula el promedio de los costos almacenados, se redondea el valor y se devuelve como el resultado final esperado.

El gráfico donde se muestran estos datos es *barra_apilada* y muestra el costo promedio, en CUP, de obtener 1 gramo de cada macronutriente (proteínas, grasas y carbohidratos) a partir de cada producto analizado. Para cada producto, la altura de cada segmento de la barra apilada representa el precio promedio por gramo de ese macronutriente. Por lo tanto, mientras más alta es la barra asociada a un macronutriente en un producto, más costoso resulta obtener 1 gramo de ese macronutriente a partir de dicho producto. En consecuencia, para cubrir las necesidades diarias de macronutrientes, los productos con barras más altas implican un mayor gasto económico.
Además, es posible comparar directamente los precios por gramo de un mismo macronutriente entre diferentes productos: observando todos los segmentos de proteína (del mismo color) en todos los productos, se puede identificar cuál producto ofrece la proteína más barata por gramo. De igual manera, comparando los segmentos de grasas entre todos los productos se identifica cuál es la fuente más económica de grasas, y así sucesivamente con los carbohidratos. Si una barra no tiene el color asociado a un macronutrientes significa que ese producto no contiene ese tipo de nutriente






























