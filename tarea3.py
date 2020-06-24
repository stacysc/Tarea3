import pandas as pd 
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import norm

plt.style.use('ggplot')


#Se extraen los datos de el archivo csv y se guardan en 'variables'
datos_a = pd.read_csv('xy.csv') 
xyp = pd.read_csv('xyp.csv') 
xy = datos_a.drop(['Unnamed: 0'], axis=1)

'''
Primera parte: Encontrar la mejor curva de ajuste (modelo probabilístico) para 
las funciones de densidad marginales de X y Y.
Para resolver esta parte lo que se debe hacer es calcular la PMF de cada variable.

'''

#Para obtener la PMF de x, debemos sumar cada una de las filas correspondientes a cada valor de x y y
PMF_x = np.sum(xy, axis = 1)
PMF_y = np.sum(xy, axis = 0)

print("La funcion de densidad discreta de x es:\n", PMF_x, "\nLa funcion de densidad discreta de y es:\n", PMF_y)

#Ahora debemos graficar las PMF resultantes 
#Creamos un linspace para representar cada valor de x y x en el eje x. 
abscisas_x = np.linspace(5, 15, 11)
abscisas_y = np.linspace(5, 25, 21)
    
#Y ahora graficamos
plt.figure()
plt.title('Funcion de densidad probabilistica de X') 
plt.xlabel('x') 
plt.ylabel('fx')
plt.plot(abscisas_x , PMF_x)
plt.show() 

plt.figure()
plt.title('Funcion de densidad probabilistica de Y') 
plt.xlabel('y') 
plt.ylabel('fy')
plt.plot(abscisas_y, PMF_y)
plt.show() 
 
#Observando las graficas se puede ver que siguen la forma de la curva normal 

#Ahora se define la curva gaussiana, junto con los para
def gauss(x, mu, sigma):
       return 1.0/np.sqrt(2*np.pi*sigma**2)*np.exp(-0.5*(x-mu)**2/sigma**2)

#Se calculan los parametros necesarios para calcular la curva gaussiana, que son la media y la desviacion estandar
param_x, _ = curve_fit(gauss, abscisas_x, PMF_x)
param_y, _ = curve_fit(gauss, abscisas_y, PMF_y) 

#Se calculan las curvas de ajuste para x y y, con los parametros calculados anteriormente
ajuste_x = gauss(abscisas_x, param_x[0], param_x[1])
ajuste_y = gauss(abscisas_y, param_y[0], param_y[1])

print("La curva de mejor ajuste para x es:\n", ajuste_x, "\nLa curva de mejor ajuste para y es:\n", ajuste_y)

plt.figure()
plt.title('Curva de Ajuste Gaussiana para X') 
plt.xlabel('x') 
plt.ylabel('fx')
plt.bar(abscisas_x, PMF_x, color = 'slateblue')
plt.plot(abscisas_x, ajuste_x, 'r--', linewidth=2, color = 'black')
plt.show() 

plt.figure()
plt.title('Curva de Ajuste Gaussiana para Y') 
plt.xlabel('y') 
plt.ylabel('fy')
plt.bar(abscisas_y, PMF_y, color = 'slateblue')
plt.plot(abscisas_y, ajuste_y, 'r--', linewidth=2, color = 'black')
plt.show()

'''
Parte 2: Asumir independencia de X y Y, ¿cuál es entonces la función de 
densidad conjunta que modela los datos?

Para resolver esta parte se debe seguir la fórmula fx,y(x,y) = fx(x)*fy(y),
ya que sabemos que son independientes. 

'''

#Definimos las variables N del tamaño de cada una de las PMF y definimos una lista vacia
N1 = len(PMF_x)
N2 = len(PMF_y)
PMF_conjunta = []

#Se hacen dos lazos para multiplicar cada funcion de densidad de cada x y y entre sí
for i in range (0,N1):
    for j in range (0,N2):
        resultado = PMF_x[i]*PMF_y[j]
        PMF_conjunta.append(resultado)

'''
Parte 3: Hallar los valores de correlación, covarianza y coeficiente de 
correlación (Pearson) para los datos y explicar su significado.

'''
#Calculamos la correlacion por medio de la doble sumatoria de Cxy = (x)(y)*fX,Y (x, y)
#Usamos los datos del documento csv xyp
x_p = xyp["x"]
y_p = xyp["y"]
f_p = xyp["p"]
N3 = 231
R_xy = 0
C_xy = 0
p = 0

for i in range (0,N3): 
    R_xy += x_p[i]*y_p[i]*f_p[i]
       
print("\nLa correlacion entre las funciones X y Y es de: ", R_xy)    

#Calculamos la covarianza por medio de la doble sumatoria de Cxy = (x − mux)(y − muy)*fX,Y (x, y)
for i in range (0,N3): 
    C_xy += (x_p[i]-param_x[0])*(y_p[i]-param_y[0])*f_p[i]
          
print("\nLa covarianza entre las funciones X y Y es: ", C_xy)

#Calculamos el coeficiente de correlacion por medio de la ecuacion p = Cxy/sigmax*sigmay
for i in range (0,N3):
    p += ((x_p[i]-param_x[0])/param_x[1])*((y_p[i]-param_y[0])/param_y[1])*f_p[i]

print("\nEl coeficiente de correlacion entre las funciones X y Y es: ", p)

'''
Parte 4: Graficar las funciones de densidad marginales (2D), la función de densidad 
conjunta (3D).

'''

#Se dibujan primero las densidades marginales (Ya se habia hecho en la parte 1)
plt.figure()
plt.title('Funcion de densidad probabilistica de X') 
plt.xlabel('x') 
plt.ylabel('fx')
plt.plot(abscisas_x , PMF_x)
plt.show() 

plt.figure()
plt.title('Funcion de densidad probabilistica de Y') 
plt.xlabel('y') 
plt.ylabel('fy')
plt.plot(abscisas_y, PMF_y)
plt.show() 


#Se dibuja ahora la densidad conjunta, se usa el vector calculado en la parte 2
fig = plt.figure()
ax = fig.add_subplot (111, projection = '3d')
ax.scatter3D(x_p, y_p, PMF_conjunta, c=PMF_conjunta, cmap = 'tab20b')
plt.show()

