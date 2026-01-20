# ¿Es un lujo la vida saludable en Cuba?
***Estudiante: Elias Fabré Rosa***

***Facultad de Matemática y Computación (MATCOM), La Habana***

***Proyecto de Ciencia de Datos - 1er Año***

En la Cuba actual, acceder a una alimentación saludable es un desafío crítico debido a la desconexión entre los ingresos y el costo de vida. Con un salario promedio de [6,449](https://www.onei.gob.cu/sites/default/files/publicaciones/2025-04/salario-medio-en-cifras-2024-edicion-2025.pdf) CUP, el trabajador estatal se enfrenta a un mercado donde productos esenciales consumen gran parte de su presupuesto.
Por tanto, este proyecto se fundamenta en la necesidad de documentar, mediante datos reales de 30 Mipymes y series temporales, cómo el factor económico se ha convertido en la principal barrera para la salud en Cuba, transformando la nutrición balanceada en un privilegio fuera del alcance de la mayoría.

## Base de Datos

Se analizaron 17 productos en 30 mipymes de Plaza de la Revolución, Centro Habana y Guanabo. Los alimentos identificados: 

Muslo de pollo
Pechuga de pollo
Higado de pollo
Picadillo de pollo
Huevo
Molleja de pollo
Lomo de cerdo
Atún
Pierna de cerdo
Garbanzos
Frijoles negros
Frijoles colorados
Arroz
Codito
Espaguetis
Leche en polvo
Azúcar blanca

Estos son frecuentes en las mipymes y pertenecen a grupos que la [OMS](https://www.who.int/es/news-room/fact-sheets/detail/healthy-diet) reconoce como necesarios para una dieta saludable, con el propósito de evaluar la relación costo-beneficio nutricional de cada uno.

La base de datos utilizada estan guardadas en un archivo .json

El archivo **valor_nutricional*** contiene los datos nutricionales principales (grasas, proteínas y carbohidratos) para cada producto. Por general, estos valores corresponden a una porción de 100 gramos del alimento en crudo. Las excepciones son: el huevo, cuyos datos se obtuvieron por unidad; el atún, por los nutrientes de una lata; el muslo de pollo, considerando solo la carne sin hueso; la leche en polvo, cuyo valor se basa en la porción equivalente a 2 cucharadas (16 gramos) necesaria para preparar un vaso de 8 onzas y la azucar es el valor nutricional de 1 cucharada (15 gramos).

Cada llave del json es el nombre del producto, las claves son los macronutrientes y los valores correspondiente la cantidad en gramo
Se tomaron los datos a partir de las etiquetas de los productos y también por la aplicación [Fitia](https://fitia.app/es/). 


Los datos de la ***evoluvión del precio*** en cada llave principal está la fecha donde se registró el precio de los productos y contiene otra llave para asociar el nombre del producto que se va a guarda. Los productos guardados en este archivo son: arroz, huevo, lomo de cerdo, pierna de cerdo, frijoles negros y frijoles colorados. 

La clave `unit` es la unidad de peso del producto que son *lb* para referirse a 1 libra del producto y *unidad* para asociar solamente a 1 huevo. 

La clave `min` y `max` es el precio mínimo y máximo registrado en el mes correspondiente a la llave de la fecha. 
Estos datos están registrados desde enero del 2024 hasta noviembre 2025 en la [ONEI](https://www.onei.gob.cu/publicaciones-economico?field_categoria_de_temas_target_id=495&field_year_value=2025&title=). 

Los datos en ***mipymes*** contiene los productos disponibles en las mipymes de los productos para analizar. Su estructura es:

La llave `mipyme` es la principal del json y contiene una lista con varios diccionarios, cada diccionario es una mipyme diferente. En cada mipyme encontramos las siguientes llaves:

 `id`: para identificar el número de identidad de la mipyme,

`nombre`: para registrar el nombre de la mipyme, 

`ubicación`: tiene como valor una serie de números que es la ubibación en el mapa de Google maps para poder encontrar la mipyme,

productos es una lista que contiene diccionarios, cada diccionario es un producto diferente. En estos diccionarios hay como llave:

`nombre`: para registrar el nombre del producto,

`cantidad`:para guardar la cantidad en gramos o las unidades en caso del huevo,

`unidad`: aquí está el peso de medida que casi siempre es en gramos excepto el huevo que se registra en unidad,

`precio`: es el costo en cup del producto

Los datos fueron obtenidos desde finales de noviembre y principios de diciembre del 2025.



