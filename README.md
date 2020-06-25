# Tarea3
Variable aleatorias multiples. 

## Descripción: 
En el archivo xy.csv está el registro de la frecuencia relativa de dos variables aleatorias conjuntas en forma de tabla. También está el archivo xyp.csv donde vienen todos los pares (x, y) y su probabilidad asociada.

### Resultados
> Parte 1:  A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico) para las funciones de densidad marginales de X y Y.

En este caso, se debe calcula la PMF (Probability Mass function) de las variables *x* y *y*, para ello se debe sumar cada fila o columna correspondiente a cada valor de *x* y *y*, en el caso de *x*, va de 5 a 15, y en el caso de *y* va de 5 a 25. En el caso de la función de densidad para x, los valores de cada x corresponden a:
<img src="https://render.githubusercontent.com/render/math?math=x_5=0.06714,x_6=0.07172, x_7=0.08327,x_8=0.09230,x_9=0.12226,x_10=0.14149,x_11=0.12172,x_12=0.09834,x_13=0.07686,x_14=0.05977,x_15=0.06519"> 
Y en el caso de la función de densidad para y, se obtuvieron los siguientes valores: <img src="https://render.githubusercontent.com/render/math?math=y_5=0.03698,y_6=0.03364,y_7=0.03105,y_8=0.03481,y_9=0.03546,y_10=0.03950,y_11=0.04947,y_12=0.04839,y_13=0.06363,y_14=0.08419,y_15=0.07856,y_16=0.08193,y_17=0.06626,y_18=0.05344,y_19=0.04440,y_20=0.03981,y_21=0.03691,y_22=0.03430,y_23=0.04137,y_24=0.02939,y_25=0.03657">
|  x | Valor PMF |
|:--:|:---------:|
|  5 |           |
|  6 |           |
|  7 |           |
|  8 |           |
|  9 |           |
| 10 |           |
| 11 |           |
| 12 |           |
| 13 |           |
| 14 |           |
| 15 |           |
 
Para graficar las PMFs se creó el correspondiente intervalo de x de [5, 15] y el de y de [5, 25], que son los valores que se deben colocar en el eje de las abscisas. Al graficar la PMF de x resultó la gráfica: 

<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/denmarginalx.png">
</p>  
  
Y al graficar la PMF de y resultó la gráfica:

<p align="center">
  <img src="https://github.com/stacysc/Tarea3/blob/master/denmarginaly.png">
</p> 
  
Como se puede observar en las gráficas anteriores, las gráficas se asemejan a la distribución normal o gaussiana. Por lo tanto, se definió la fórmula de la distribución gaussiana que corresponde a: <img src="https://render.githubusercontent.com/render/math?math=f_x(x)=1.0/np.sqrt(2*np.pi*sigma**2)*np.exp(-0.5*(x-mu)**2/sigma**2)"> y se calcularon los parámetros necesarios para calcularla, que son la media y la desviación estándar, se utilizó la función curve_fit() de python. En el caso de la función x, su media fue de 9.9048438, y su desviación estándar de 3.2994429; y en el caso de la función y, la media es de 15.0794609 y la desviación estándar de 6.0269377. 




