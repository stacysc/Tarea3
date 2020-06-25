# Tarea3
Variable aleatorias multiples. 

## Descripción: 
En el archivo xy.csv está el registro de la frecuencia relativa de dos variables aleatorias conjuntas en forma de tabla. También está el archivo xyp.csv donde vienen todos los pares (x, y) y su probabilidad asociada.

### Resultados
> Parte 1:  A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

En este caso, se debe calcula la PMF (Probability Mass function) de las variables *x* y *y*, para ello se debe sumar cada fila o columna correspondiente a cada valor de *x* y *y*, en el caso de *x*, va de 5 a 15, y en el caso de *y* va de 5 a 25. En el caso de la función de densidad para x, los valores de cada x corresponden a:

<p align="center">
 
|  X | Valor PMF |
|:--:|:---------:|
|  5 | 0.06714   |
|  6 | 0.07172   |
|  7 | 0.08327   |
|  8 | 0.09230   |
|  9 | 0.12226   |
| 10 | 0.14149   |
| 11 | 0.12172   |
| 12 | 0.09834   |
| 13 | 0.07686   |
| 14 | 0.05977   |
| 15 | 0.06519   |

 </p> 
 
Y en el caso de la función de densidad para y, se obtuvieron los siguientes valores: 

<div align="center">
 
 
| Y  | PMF |
|----|-----|
|  5 | 0.03698    |
|  6 | 0.03364    |
|  7 | 0.03105    |
|  8 | 0.03481    |
|  9 | 0.03546    |
| 10 | 0.03950    |
| 11 | 0.04947    |
| 12 | 0.04839    |
| 13 | 0.06363    |
| 14 | 0.08419    |
| 15 | 0.07856    |
| 16 | 0.08193    |
| 17 | 0.06626    |
| 18 | 0.05344    |
| 19 | 0.04440    |
| 20 | 0.03981    |
| 21 | 0.03691    |
| 22 | 0.03430    |
| 23 | 0.04137    |
| 24 | 0.02939    |
| 25 | 0.03657    |

</div> 
 
Para graficar las PMFs se creó el correspondiente intervalo de x de [5, 15] y el de y de [5, 25], que son los valores que se deben colocar en el eje de las abscisas. Al graficar la PMF de x resultó la gráfica: 

<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/denmarginalx.png">
</p>  
  
Y al graficar la PMF de y resultó la gráfica:

<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/denmarginaly.png">
</p> 
  
Como se puede observar en las gráficas anteriores, las gráficas se asemejan a la distribución normal o gaussiana. Por lo tanto, se definió la fórmula de la distribución gaussiana que corresponde a: <img src="https://latex.codecogs.com/gif.latex?\inline&space;f_X(x)&space;=&space;\frac{1.0}{\sqrt{2\pi\sigma^2}}e^{\frac{-0.5(x-\mu)^2}{\sigma^2}}"> y se calcularon los parámetros necesarios para calcularla, que son la media y la desviación estándar, se utilizó la función curve_fit() de python. En el caso de la función x, su media fue de 9.9048438, y su desviación estándar de 3.2994429; y en el caso de la función y, la media es de 15.0794609 y la desviación estándar de 6.0269377. 

Para el ajuste de la función x, se evaluaron los parametros de media y desviación en la función de gauss y se obtuvo un vector con los siguientes parámetros:
    
<p align="center">
 
| Posición  | Ajuste |
|----|-----|
|  0 | 0.04004973    |
|  1 | 0.06002396    |
|  3 | 0.08206464    |
|  4 | 0.10235143    |
|  5 | 0.11644964    |
|  6 | 0.12086174    |
|  7 | 0.11443159    |
|  8 | 0.09883469    |
|  9 | 0.07787164    |
| 10 | 0.05597005    |
| 11 | 0.03669766    |

</p>

Y graficando la curva con estos valores obtenidos, en comparación con la curva original obtenemos:

<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/curvaajustex.png">
</p> 

Por otro lado, haciendo el mismo procedimiento para la función y, se obtuvieron los valores:
     
<p align="center">  
 
| Posición  | Ajuste |
|----|-----|
|  0 | 0.01634814    |
|  1 | 0.02128147    |
|  2 | 0.02695125    |
|  3 | 0.03320473    |
|  4 | 0.03979833    |
|  5 | 0.04640595    |
|  6 | 0.05264127    |
|  7 | 0.05809287    |
|  8 | 0.06236821    |
|  9 | 0.06513996    |
| 10 | 0.06618744    |
| 11 | 0.06542558    |
| 12 | 0.06291634    |
| 13 | 0.05886039    |
| 14 | 0.05357062    |
| 15 | 0.04743229    |
| 16 | 0.0408569     |
| 17 | 0.03423738    |
| 18 | 0.02791127    |
| 19 | 0.02213617    |
| 20 | 0.01707927    |

</p> 

Y graficando la curva con estos valores obtenidos, en comparación con la curva original obtenemos:

<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/curvaajustey.png">
</p> 

***

> Parte 2: Asumir independencia de X y Y, ¿cuál es entonces la función de densidad conjunta que modela los datos?

En este caso, como se asume que las funciones *x* y *y* son independientes entonces se tiene que la función de densidad conjunta corresponde a:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\inline&space;f_{X,Y}(x,y)&space;=&space;f_X(x)f_Y(y)">
</p> 

Como las funciones marginales se modelan con la distribución gaussiana la función de densidad conjunta también se puede expresar como:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\inline&space;f_{X,Y}(x,y)&space;=&space;\frac{1.0}{\sqrt{2\pi\sigma_x^2}}e^{\frac{-0.5(x-\mu_x)^2}{\sigma_x^2}}&space;\cdot&space;\frac{1.0}{\sqrt{2\pi\sigma_y^2}}e^{\frac{-0.5(y-\mu_y)^2}{\sigma_y^2}}">
</p> 

Por otro lado, previamente se calcularon los valores de las funciones *x* y *y* correspondientes a las funciones de densidad marginal de cada uno, entonces, para resolver esta parte se puede multiplicar cada uno de los valores calculados de x con cada uno de los valores calculados de y, de la siguiente manera:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\inline&space;\prod_{i=5}^{15}\prod_{j=5}^{25}f_X(x_i)f_Y(y_j)">
</p>

De esta manera se obtiene un vector con 231 valores, que tiene sentido al tener 11 valores para x y 21 para y. Algunos valores del vector resultante son:

<p align="center">
 
| Posición  | Probabilidad conjunta |
|---------- |-----------------------|
|    0      | 0.0024828371999999995 |
|    1      | 0.0022585895999999994 |
|    2      | 0.002084697           |
|    .      |           .           |
|    .      |           .           |
|    .      |           .           |
|    229    | 0.0019159340999999998 |
|    230    | 0.0023839982999999997 |

</p>

***

> Parte 3: Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) para los datos y explicar su significado.

* Correlación: Para calcular la correlación se utilizó la fórmula:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\inline&space;R_{XY}&space;=&space;\sum_{i}^{N}\sum_{j}^{M}x_iy_jf_{X,Y}(x_i,&space;y_j)">
</p>

Se utilizaron los datos del archivo csv 'xyp', por lo que se utilizó sólo un bucle for, y se obtuvo:
<p align="center">
   <img src="https://latex.codecogs.com/gif.latex?\inline&space;R_{XY}&space;=&space;149.54281000000012">
</p> 

Al ser el resultado un número relativamente alto, se podría pensar que entonces las funciones *x* y *y* no son independientes, al estar relacionadas de alguna forma, sin embargo, correlación no implica causalidad. En realidad la correlación indica la existencia de una relación lineal y proporcionalidad entre las dos funciones, es decir, si cambia el valor de x también lo hace el valor de y, y viceversa. 

* Covarianza: Para calcular la covarianza se utilizó la fórmula:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\inline&space;C_{XY}&space;=&space;\sum_{i}^{N}\sum_{j}^{M}(x_i-\overline{X})(y_j-\overline{Y})f_{X,Y}(x_i,&space;y_j)">
</p>

De nuevo se utilizaron los datos del archivo csv 'xyp', por lo que se utilizó sólo un bucle for, y se obtuvo:
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?\inline&space;C_{XY}&space;=&space;0.06669156989979619">
</p>

Como se puede observar, el valor de la covarianza es bastante pequeño, lo que tiene sentido, porque este parametro es el que indica la independencia de dos funciones, y como sabemos que las funciones *x* y *y* son independientes, entonces se esperaba un valor pequeño de covarianza, de casi cero.  

* Coeficiente de correlación: Para calcular este coeficiente se utilizó la fórmula:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\inline&space;\rho&space;=&space;\sum_{i}^{N}\sum_{j}^{M}(\frac{x_i-\overline{X}}{\sigma_x})(\frac{y_j-\overline{Y}}{\sigma_y})f_{X,Y}(x_i,y_j)">
</p>

También se utilizaron los datos del archivo csv 'xyp', por lo que se utilizó sólo un bucle for, y se obtuvo:
<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?\inline&space;\rho&space;=&space;0.0033537726681342793">
</p>

Se tiene que el coeficiente de correlación es la versión normalizada de la covarianza, y es un valor que está entre 0 y 1, se espera, que como las funciones *x* y *y* son independientes el coeficiente sea cero o un valor cercano a cero, lo que se cumple en este caso. 

***

> Parte 4: Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).
Las funciones de densidad marginal son las que ya se calcularon en la parte 1. La gráfica de la función de densidad marginal de x es:
<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/denmarginalx.png">
</p>  
  
Y la función de densidad marginal de y es:

<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/denmarginaly.png">
</p>

Por último, la función de densidad conjunta se graficó con la herramienta 3D de Scatter3D y se obtuvo la gráfica:
<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/grafico3D.png">
</p>
