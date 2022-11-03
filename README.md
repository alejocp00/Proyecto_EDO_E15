# Informe

## Integrantes

- Alejandro Camacho Pérez
- Carlos Arturo Pérez Cabrera
- Diana Laura Pérez Trujillo
- David Sánchez Iglesias

## Aspectos Generales

El presente proyecto propone tres implementaciones computacionales de los siguientes métodos para aproximar soluciones de Ecuaciones Diferenciales con valor inicial:

- Método de Euler
- Método de Euler mejorado
- Método de Runge-Kutta
  
Para ello se han aprovechado las facilidades que brinda el lenguaje de programación Python y varias de sus bibliotecas:

- `prettytable` (para visualizar los resultados)
- `enum` (para mayor organización a la hora de seleccionar los métodos)
- `collections.abc` (para un mejor comentado de los métodos)

## Implementación

En la primera sección de código se presentan métodos y variables globales que serán usadas a lo largo del proyecto.
La variable `EPSILON` es una constante muy pequeña que servirá como apoyo para realizar operaciones de comparación de forma correcta.
Los métodos `Equal_To(a,b)`, `Great_Than(a,b)` y `Less_Than(a,b)` son métodos de comparación: igual que, mayor que y menor que, respectivamente. Dichos métodos fueron implementados de manera manual para evitar los posibles errores que trae consigo trabajar con números flotantes en computadoras.A continuación se presentan las implementaciones de los tres métodos de aproximación ya presentados.

### Método de Euler

El Método de Euler recibe diferentes parámetros que intervendrán en su funcionamiento, como lo es, la función que se quiere aproximar, valores iniciales de las variables x e y, el máximo del intervalo donde se hará la aproximación y dos varibales h y d que representan el tamaño de paso fijo (que será usado en cada paso) y el número de decimales al que será redondeado el valor resultante, respectivamente. La implementación del método utiliza la siguiente idea:

$$x_{n+1}=x_n + h$$

$$y_{n+1}=y_n + h*f(x_n,y_n)$$

Finalmente se devuelven los resultados obtenidos en una lista de tuplas de la forma (x,y) que representan el valor de y en cada x.

### Método de Euler mejorado

El Método de Euler mejorado es similar al Método de Euler, anteriormente visto, pero resulta ser más preciso que su predecesor.
Recibe como parámetros la función que se quiere aproximar, los valores iniciales de x e y, el máximo valor de x que se quiere aproximar, el tamaño de paso fijo y la cantidad de decimales a los que será redondeado el valor resultante.

El procedimiento se realiza como sigue:

$$k_1=f(x_n,y_n)$$

$$u_{n+1}= y_n + h*k_1$$

$$k_2=f(x_{n+1},u_{n+1})$$

$$y_{n+1}=y_n+h*\frac{1}{2}(k_1+k_2)$$

Si se toma $k=\frac{k_1+k_2}{2}$ la ecuación toma la forma del método de Euler. Finalmente se devuelven los valores en una lista de tuplas de la forma (x,y).

### Método de Runge-Kutta

El Método de Runge-Kutta es el más preciso de los métodos presentados y el más usado en la práctica. En la implementación propuesta, el método recibe una función f, que será la función que se estará trabajando, valores iniciales de x e y, así como el máximo x del intervalo y dos valores h y d que representan el tamaño de paso fijo entre punto y punto, y la cantidad de decimales a redondear el valor resultante, respectivamente.

El trabajo con el método se realiza de la siguiente manera:

$$k_1=f(x_n,y_n)$$

$$k_2=f(x_n+\frac{1}{2}h, y_n+\frac{1}{2}hk_1)$$

$$k_3=f(x_n+\frac{1}{2}h, y_n+\frac{1}{2}hk_2)$$

$$k_4=f(x_{n+1},y_n+hk_3)$$

Donde:

- $k_1:$ es la pendiente del método de Euler en $x_n$
- $k_2:$ estimación de la pendiente en el punto medio del intervalo [$x_n,x_{n+1}$] utilizando el método de Euler para predecir la ordenada en ese punto.
- $k_3:$ valor del método de Euler mejorado para la pendiente en el punto medio.
- $k_4:$ La pendiente en el método de Euler en el punto $x_{n+1}$, utilizando la pendiente mejorada $k_3$ en el punto medio para pasar a $x_{n+1}$.

Luego se utiliza la siguiente fórmula para calcular cada una de las aproximaciones.

$$y_{n+1}=y_n + \frac{h}{6}(k_1+2k_2+2k_3+k_4)$$

Si se toma $k=\frac{1}{6}(k_1+2k_2+2k_3+k_4)$ la ecuación toma la forma usada en el método de Euler.

### Métodos Auxiliares

En esta sección figuran los métodos `Calculate_Values(*args)`, `Print_Table(*args)` y `Print_Deer_Info(*args)`.

- `Calculate_Values` sirve de puente entre los datos y el propio método de aproximación que se utilizará. El método recibe los siguientes parámetros: la función con la que se estará trabajando, el método que se utilizará, los valores mínimo y máximo de x, así como el valor inicial de y; una lista de los diferentes tamaños de paso fijo (h) que se estarán considerando y la cantidad de decimales a redondear.
Se devuelve una lista que contiene los valores obtenidos, usando el método especificado, para cada una de los diferentes valores del tamaño de paso fijo (h).

- `Print_Table` es el visualizador de los resultados obtenidos al aplicar uno de los métodos de aproximación a una función. Con la ayuda de la biblioteca de Python prettyTable, se logra imprimir una tabla donde quedan reflejados los valores de x e y.

- `Print_Deer_Info` se encarga de imprimir toda la información particular relacionada con el ejercicio 26 página 122.

## Ejercicios y resultados

En esta sección se muestran los resultados obtenidos al aplicar los métodos de aproximación a las funciones dadas en el libro de texto.

### Ejercicio 24, página 132

Para el problema se requiere una computadora con
impresora. En este problema de valor inicial utilice el método de Euler mejorado con tamaños de paso h = 0.1, 0.02,
0.004 y 0.0008 para aproximar con 5 cifras decimales el valor de la solución en 10 puntos igualmente espaciados del intervalo dado. Imprima los resultados en forma tabular con los encabezados apropiados para facilitar la comparación del efecto de variar el tamaño de paso h. Las primas representan derivadas con respecto a x.

$$y'= \frac{x}{1+y²},y(-1)=1;-1 \leq x \leq 1$$

#### Resultados método Euler mejorado

| x | y(h=0.1) | y(h=0.02) | y(h=0.004) | y(h=0.0008) |
|:---:|:---:|:---:|:---:|:---:|
| -1.0 |    1     |     1     |     1      |      1      |
| -0.8 | 0.90572  |  0.90569  |  0.90569   |   0.90569   |
| -0.6 | 0.82574  |  0.82569  |  0.82569   |   0.82569   |
| -0.4 | 0.76449  |  0.76443  |  0.76443   |   0.76443   |
| -0.2 | 0.72593  |  0.72586  |  0.72586   |   0.72586   |
| 0.0  | 0.71276  |  0.71268  |  0.71268   |   0.71268   |
| 0.2  | 0.72595  |  0.72586  |  0.72586   |   0.72586   |
| 0.4  | 0.76453  |  0.76443  |  0.76443   |   0.76443   |
| 0.6  | 0.82579  |  0.82569  |  0.82569   |   0.82569   |
| 0.8  | 0.90578  |  0.90569  |  0.90569   |   0.90569   |
| 1.0  | 1.00006  |    1.0    |    1.0     |     1.0     |

### Ejercicio 24, Página 142

Para el problema se requiere una computadora con
impresora. En estos problemas de valor inicial utilice el método de Runge-Kutta con tamaños de paso h = 0.2 , 0.1, 0.05 y 0.025 para aproximar a 6 cifras decimales los valores de la solución en 5 puntos igualmente espaciados del intervalo dado. Imprima los resultados en forma tabular con un encabezado apropiado que facilite la comparación del efecto de variar el tamaño de paso h. Las primas representan derivadas con respecto a x.

$$y'= \frac{x}{1+y²},y(-1)=1;-1 \leq x \leq 1$$

#### Resultados método Runge-Kutta

| x | y(h=0.2) | y(h=0.1) | y(h=0.05) | y(h=0.025) |
|:---:|:---:|:---:|:---:|:---:|
| -1.0 |    1     |    1     |     1     |     1      |
| -0.6 | 0.82569  | 0.825691 |  0.825691 |  0.825691  |
| -0.2 | 0.725856 | 0.725856 |  0.725857 |  0.725857  |
| 0.2  | 0.725856 | 0.725856 |  0.725857 |  0.725857  |
| 0.6  | 0.82569  | 0.825691 |  0.825691 |  0.825691  |
| 1.0  |   1.0    |   1.0    |    1.0    |    1.0     |

### Ejercicio 26, página 122

Suponga que en un pequeño bosque la población de venados P(t) inicialmente es de 25 individuos y satisface la ecuación logística  

$$\frac{dP}{dt} = 0.0225P − 0.0003P²$$  

(con t en meses). Utilice el método de Euler con
una calculadora programable o una computadora para aproximar la solución a 10 años, primero con un tamaño de paso h = 1 y después con h = 0.5, redondeando los valores aproximados de P a números enteros de venados. ¿Qué porcentaje de la población límite de 75 venados se obtiene
después de 5 años? ¿Después de 10 años?

#### Resultados método Euler

| x | y(h=1) | y(h=0.5) |
|:---:|:---:|:---:|
|  0.0  |   25   |    25    |
|  10.0 |  29.0  |   29.0   |
|  20.0 |  33.0  |   33.0   |
|  30.0 |  37.0  |   37.0   |
|  40.0 |  41.0  |   41.0   |
|  50.0 |  45.0  |   45.0   |
|  60.0 |  49.0  |   49.0   |
|  70.0 |  53.0  |   53.0   |
|  80.0 |  56.0  |   56.0   |
|  90.0 |  59.0  |   59.0   |
| 100.0 |  62.0  |   62.0   |
| 110.0 |  64.0  |   64.0   |
| 120.0 |  66.0  |   66.0   |

- Población de ciervos en $5$ años: $49$
- Porcentaje de población de ciervos en $5$ años con respecto a $75: 65.33\%$

- Población de ciervos en $10$ años: $66$
- Porcentaje de población de ciervos en $10$ años con respecto a $75: 88.0\%$

## Bibliografía

- "Ecuaciones Diferenciales y problemas con valores en la frontera. Cómputo y modelado. Cuarta edición" C. Henry Edwards, David E. Penney
