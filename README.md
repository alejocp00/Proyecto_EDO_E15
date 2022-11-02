# Proyecto EDO E15

## Integrantes

- Alejandro Camacho Pérez
- Carlos Arturo Pérez Cabrera
- Diana Laura Pérez Trujillo
- David Sánchez Iglesias

### Resumen MarkDown

Esto es *cursiva*

Esto es **bold**

Esto es algo

Lo de abajo es una linea

---

|$x$|$y_1$|$y_2$|
|:---:|:---:|:---:|
|1|2|3
|4|25|6|

>
> Quote
>
> MuliLine Quote

- List
- Of
- Lements

1. Numeral
2. List
3. Of
4. Elements
   1. With
   2. diferents
   3. levels

$$
A_{sub}
\frac{Numerador}{Denominador}
$$

# Informe

## Aspectos Generales

El presente proyecto propone tres implementaciones computacionales de los siguientes métodos para aproximar soluciones de Ecuaciones Diferenciales: Método de Euler, Método de Euler Mejorado y   git config --global user.email Método de Runge-Kutta. Para ello se han aprovechado las facilidades que brinda el lenguaje de programación Python y dos de sus bibliotecas: pandas y prettytable.

## Implementación

En la primera sección de código se presentan métodos y variables globales que serán usadas a lo largo del proyecto.
La variable "Epsilon" es una constante muy pequeña que servirá como apoyo para realizar operaciones de comparación de forma correcta.
Los métodos "Equal_To", "Great_Than" y "Less_Than" son métodos de comparación: igual que, mayor que y menor que, respectivamente.

A continuación se presentan las implementaciones de los tres métodos de aproximación ya presentados.

### Método de Euler

El Método de Euler recibe diferentes parámetros que intervendrán en su funcionamiento, como lo es, la función que se quiere aproximar, valores iniciales de las variables x e y, el máximo del intervalo donde se hará la aproximación y dos varibales h y d que representan el tamaño de paso fijo (que será usado en cada paso) y el número de decimales al que será redondeado el valor resultante, respectivamente.

La implementación del método utiliza la siguiente idea:

$$
x_{n+1}=x_n + h\\
y_{n+1}=y_n + h*f(x_n,y_n)
$$

Finalmente se devuelven los resultados obtenidos en una lista de tuplas de la forma (x,y) que representan el valor de y en cada x.

### Método de Euler mejorado

El Método de Euler mejorado es similar al Método de Euler, anteriormente visto, pero resulta ser más preciso que su predecesor.
Recibe como parámetros la función que se quiere aproximar, los valores iniciales de x e y, el máximo valor de x que se quiere aproximar, el tamaño de paso fijo y la cantidad de decimales a los que será redondeado el valor resultante.

El procedimiento se realiza como sigue:
$$
k_1=f(x_n,y_n)\\
u_{n+1}= y_n + h*k_1\\
k_2=f(x_{n+1},u_{n+1})\\
y_{n+1}=y_n+h*\frac{1}{2}(k_1+k_2)
$$

Si se toma $k=\frac{k_1+k_2}{2}$ la ecuación toma la forma del método de Euler.

Finalmente se devuelven los valores en una lista de tuplas de la forma (x,y).

### Método de Runge-Kutta

El Método de Runge-Kutta es el más preciso de los métodos presentados y el más usado en la práctica. En la implementación propuesta, el método recibe una función f, que será la función que se estará trabajando, valores iniciales de x e y, así como el máximo x del intervalo y dos valores h y d que representan el tamaño de paso fijo entre punto y punto, y la cantidad de decimales a redondear el valor resultante, respectivamente.

El trabajo con el método se realiza de la siguiente manera:

$$
k_1=f(x_n,y_n) \\
\enspace       \\
k_2=f(x_n+\frac{1}{2}h, y_n+\frac{1}{2}hk_1) \\
\enspace       \\
k_3=f(x_n+\frac{1}{2}h, y_n+\frac{1}{2}hk_2) \\
\enspace       \\
k_4=f(x_{n+1},y_n+hk_3)
$$
Donde:

$k_1:$ es la pendiente del método de Euler en $x_n\\$

$k_2:$ estimación de la pendiente en el punto medio del intervalo [$x_n,x_{n+1}$] utilizando el método de Euler para predecir la ordenada en ese punto.

$k_3:$ valor del método de Euler mejorado para la pendiente en el punto medio.

$k_4:$ La pendiente en el método de Euler en el punto $x_{n+1}$, utilizando la pendiente mejorada $k_3$ en el punto medio para pasar a $x_{n+1}$.

Luego se utiliza la siguiente fórmula para calcular cada una de las aproximaciones.
$$
y_{n+1}=y_n + \frac{h}{6}(k_1+2k_2+2k_3+k_4)
$$

Luego, si se toma $k=\frac{1}{6}(k_1+2k_2+2k_3+k_4)$ la ecuación toma la forma usada en el método de Euler.

### Métodos Auxiliares

En esta sección figuran los métodos Calculate_Values, Print_Table y Print_Deer_Info.

El método Calculate_Values sirve de puente entre los datos y el propio método de aproximación que se utilizará. El método recibe los siguientes parámetros: la función con la que se estará trabajando, el método que se utilizará, los valores mínimo y máximo de x, así como el valor inicial de y; una lista de los diferentes tamaños de paso fijo (h) que se estarán considerando y la cantidad de decimales a redondear.
Se devuelve una lista que contiene los valores obtenidos, usando el método especificado, para cada una de los diferentes valores del tamaño de paso fijo (h).

El método Print_Table es el visualizador de los resultados obtenidos al aplicar uno de los métodos de aproximación a una función. Con la ayuda de la biblioteca de Python prettyTable, se logra imprimir una tabla donde quedan reflejados los valores de x e y.
