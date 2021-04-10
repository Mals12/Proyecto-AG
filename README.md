# Proyecto Algoritmos Genéticos

## ¿Qué es un algortimo genético?
Un algoritmo es una serie de pasos organizados que describe el proceso que se debe seguir, para dar solución a un problema específico.
En los años 1970, de la mano de John Henry Holland, surgió una de las líneas más prometedoras de la inteligencia artificial, la de los algoritmos genéticos.
Un algoritmo genético es cuando se usan mecanismos que simulan los de la evolución de las especies de la biología para formular los pasos de un algoritmo.
Los algoritmos genéticos tienen la función de buscar la solución a un problema a traves del tiempo, buscan el mejor elemento (individuo) dentro de una población la cual va cambiando al paso del tiempo. Los algoritmos genéticos llevan un proceso:
* Población
* Función objetivo (Fitness)
* Selección
* Cruce
* Mutación
* Reemplazo
y esto se repite hasta llegar al objetivo deseado.
![](https://1.bp.blogspot.com/-82PtewK8HMQ/VqWj0Ts0BPI/AAAAAAAAAH0/n7OfLykvakU/s640/Diagrama-de-flujo.png)
 
## Población
En este apartado se define o se crea la población que se va a examinar. La tecnica para crear una población varia de acuerdo al tipo de población que tengamos. Para este proyecto la población de incio se creeo aleatoriamente como una lista donde cada elemento tiene una representacion de un vector de permutaciones.

## Función de aptitud (Fitness)
Esta función se usa para evaluar a la población, evalua su capacidad para adactarse. La función se define de acuerdo a los puntos que querramos evaluar en los individuos. Para este proyecto buscamos 0 ataques en los elementos de nuestra problación, por la forma de representación que tenemos, nuestros ataques se ven tomando la posición de las reinas como coordenadas en el plano, analizamos si la pendiente de la recta que pasa por dos de ellas es igual a 1 o -1 quiere decir que hay un ataque entre ellas.

## Selección de Padres
En esta etapa del algoritmo, como su nombre lo dice, seleccionamos a 2 elementos de la población para ser los padres. Existen muchas tecnicas de selección, para esto usaremos la selección por el método de muestreo deterministico, este método usa la función  de aptitup para obtener la probabilidad de que cada individuo sea seleccionado, y esta probabilidad se usa para saber cuantos elementos iguales a este se esperan en la siguiente generación. Apartir de lo anterior y otras cosas más es que se selecciona a los elementos más aptos para ser los padres.

## Cruza o Recombinación
En este apartado los padres seleccionados en la etapa anterior son "cruzados" para generar 2 elementos nuevos, los hijos. Existen muchos métodos de cruza, para este proyecto usaremos el metodo de la cruza a los extremos, el cual consiste en construir una tabla de extremos apartir de los elementos que componen a los padres. Funciona de la siguiente manera:
* Construir la tabla de extremos
* Se elige aleatoriamente un extremo inicial (current)
* Colocamos a current en el descendiente (hijo)
* Se remueve de todas las listas de extremos a current
* Examinamos la lista de estremos de current
  * Si tiene elmentos repetidos, se selecciona a dicho elemento como nuestro nuevo current, y retornamos al paso 3.
  * Si no hay elementos repetidos, se checan las listas de los elementos de la lista de extremos de current y se designa a la entrada con la lista más pequeña como nuestro nuevo current, y retornamos al paso 3. 
  * En caso de que las menores entradas tengan igual longitud en sus listas, se selecciona como current un número aleatorio, de las entradas faltantes en el descendiente, y volvemos al paso 3.
  * Se concluye al encontrar un current el cual tenga su lista vacia y el tamaño del descendiente se el esperado.
   * Si el tamaño no es el adecuado regresamos al paso 2. 

## Mutación
En esta etapa los individuos (hijos) generados en el apartado anterior son mutados. Existen diferentes tipos (métodos) para mutar individuos, en este caso estaremos usando el método de mutación por inserción. El cual consiste en tomar aleatoriamente 2 posiciones de los elementos del individuo y colocar el elemento de la segunda posición justo después del elemento de la primera posición y los elementos restantes se colocan en el orden que aparecen.

## Reemplazo
Cuando llegamos a esta función nuestra población ya sera del doble con la que iniciamos, así que debemos de elegir con que individuos nos quedaremos para reemplazar a la poblacion original y pasar a la siguiente generación. Existen distintas formas de hacer este reemplazo, uraremos el reemplazo generacional, el cual nos dice que todos los individuos nuevos, es decir los hijos mutados, son los que sobreviven y pasan a la siguiente generación, es decir la poblacion nueva reemplaza por completo a la poblacion anterior.
