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

La llave `mipyme` es la principal del json y contiene una lista con varios diccionarios, cada diccionario es una mipyme diferente. En cada mipyme encontramos las siguientes llaves:

 `id`: para identificar el número de identidad de la mipyme,

`nombre`: para registrar el nombre de la mipyme, 

`ubicación`: tiene como valor una serie de números que es la ubibación en el mapa de Google maps para poder encontrar la mipyme,

`productos`:  es una lista que contiene diccionarios, cada diccionario es un producto diferente. En estos diccionarios hay como llave:

`nombre`: para registrar el nombre del producto,

`cantidad`:para guardar la cantidad en gramos o las unidades en caso del huevo,

`unidad`: aquí está el peso de medida que casi siempre es en gramos excepto el huevo que se registra en unidad,

`precio`: es el costo en cup del producto

Los datos fueron obtenidos desde finales de noviembre y principios de diciembre del 2025.


Tambien se analizaron entre frutas y verduras 6 diferente y se guardaron en el archivo ***frutas_verduras.json***:

- Fruta bomba
- Guayaba
- Platano fruta
- Pepino
- Tomate
- Zanahoria

La estructura del archivo esta divido en 2 llaves principales, `frutas` y `verduras`, cada uno tiene una lista donde cada diccionario es un producto diferente asociado al tipo de alimento. Las claves son:
`unit`: Es la unidad de medida del producto

`cantidad`: Es la cantidad de la unidad de medida.

`precio`: Es el precio del producto asociado a la cantidad 


Estos alimentos frecuentes en el mercado cubano y pertenecen a los grupos que la [OMS](https://www.who.int/es/news-room/fact-sheets/detail/healthy-diet) reconoce como necesarios para una dieta saludable, con el propósito de evaluar la relación costo-beneficio nutricional de cada uno.

La base de datos utilizada estan guardadas en un archivo .json

El archivo ***valor_nutricional.json*** contiene los datos nutricionales principales (grasas, proteínas y carbohidratos) para cada producto. Por general, estos valores corresponden a una porción de 100 gramos del alimento en crudo. Las excepciones son: el huevo, cuyos datos se obtuvieron por unidad; el atún, por los nutrientes de una lata; el muslo de pollo, considerando solo la carne sin hueso; la leche en polvo, cuya cantidad de 40 gramos (equivalente a 2 cucharadas con una pequena loma) necesaria para preparar un vaso de 8 onzas o 240 ml y la azucar es el valor nutricional de 1 cucharada (15 gramos).

Cada llave del json es el nombre del producto, las claves son los macronutrientes y los valores correspondiente la cantidad en gramo
Se tomaron los datos a partir de las etiquetas de los productos y también por la aplicación [Fitia](https://fitia.app/es/). 


Los datos de la ***evoluvión_precios.json*** en cada llave principal está la fecha donde se registró el precio de los productos y contiene otra llave para asociar el nombre del producto que se va a guarda. Los productos guardados en este archivo son: arroz, huevo, lomo de cerdo, pierna de cerdo, frijoles negros y frijoles colorados. 

La clave `unit` es la unidad de peso del producto que son *lb* para referirse a 1 libra del producto y *unidad* para asociar solamente a 1 huevo. 

La clave `min` y `max` es el precio mínimo y máximo registrado en el mes correspondiente a la llave de la fecha. 
Estos datos están registrados desde enero del 2024 hasta noviembre 2025 en la [ONEI](https://www.onei.gob.cu/publicaciones-economico?field_categoria_de_temas_target_id=495&field_year_value=2025&title=). 


### Funciones programadas utilizadas en el Análisis 

La función **costo_promedio_nutr** fue creada para conocer el precio de obtener 1 gramo del macronutriente que el usuario desea analizar. Además revela cuales los alimentos más económicos con mayor cantidad del macronutriente. La funcón se basa en las siguiente formula:

*cantidad total de macronutriente = (valor nutricional del producto /100) * Cantidad total en gramos del producto*

Explicación: La divición entre el valor nutricional y 100 es para conocer la proporción del macronutriente. Significa que cada gramo del producto tiene X gramos del macronutriente seleccionado. Al multiplicarlo por la cantidad total en gramos del producto devuelve el total en gramos del macronutriente.
ejemplo si el frijol negro tiene 22g de proteina entonces 22/100 = 0,22g de proteina aporta 1 gramo de frijoles y si peso del producto es de 500g, 
0,22*500 = 110g de proteina total

*costo por gramo = precio / cantidad total de macronutriente*

Explicación: Se divide el precio del producto entre la cantidad total de macronutriente que contiene, y devuelve el costo para obtener 1 gramo de ese macronutriente. Por ejemplos si el precio del frijol es de 700cup, 700/110g = 6.36cup el costo de 1 gramo de proteina.

A diferencia de otros alimentos donde el peso varía y determina la cantidad total de nutrientes, el huevo se vende en un formato estándar por unidades. Debido a esta cantidad fija, se omite la división entre 100 (que busca la proporción por gramo) y se procede a multiplicar directamente el valor nutricional de un huevo por el número de unidades en el cartón para obtener el total del macronutriente.

En cada iteración, se busca el producto correspondiente en todas las MiPYMEs disponibles. Por cada coincidencia encontrada, se calcula el costo de obtener un gramo del macronutriente seleccionado y se añade a una lista. Una vez finalizada la búsqueda en todos los establecimientos, se calcula el promedio de los costos almacenados, se redondea el valor y se devuelve como el resultado final esperado.


**calcuar_macronutrientes**:
A partir de la cantidad de kcal que el usuario incerte en el argumento de la función, esta devuelve la cantidad en gramo de proteina, grasa y carbohidrato que este usuario debe consumir diario. Para ello se utilizaron los datos a partir de un articulo publicado por la [Dirección General de Salud Pública de Madrid, España](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.comunidad.madrid/sites/default/files/doc/sanidad/1._valor_energetico_saber_mas.pdf&ved=2ahUKEwj3kZS22PORAxWuSTABHQuFO2oQFnoECBwQAw&usg=AOvVaw0c4toutOgq-dTvHpn6qLhp) donde 1 gramo de proteina y carbohidrato aporta 4 kcal y 1 gramo de grasas 9 kcal. Para obtener la cantidad de cada macronutriente se utilizó la siguiente fórmula

cantidad_macronutriente =(PM/100 * kcal) / A

-PM es la proporción en % del macronutriente que se necesita 
-Kcal es la cantidad de kilocalorías que el usurio debe consumir diario
-A es la cantidad de kcal que aporta el macronutriente que se necesita


La función **precio_promedio_lb** tiene como objetivo calcular el precio promedio que una persona debe gastar en comprar 1 libra de cada producto. Pero el peso escurrido de las diferentes latas de atún de todas las mipymes nunca llega a 1 libra, por eso el análisis se basa en el precio promedio para comprar 1 lata. El resultado del de huevo es el promedio del valor de una unidad.

**datos_evolución_precio**
En esta función se preparan los datos necesarios para la gráfica de líneas donde muestra la evolución de los precios del huevo 
Retorna una lista con todas las fechas registradas de los precios de los productos y otra lista con el precio promedio en los productos. Ambas listas coinciden en la misma posición el precio de los productos con la fecha correspondiente.


















