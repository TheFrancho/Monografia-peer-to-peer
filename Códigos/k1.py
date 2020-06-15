#Programa para mostrar clusters de datos generados aleatoriamente incoloros
import numpy as np #Libreria para el calculo matemático
import matplotlib.pyplot as plt #Librería para el graficamiento matemático
from sklearn.cluster import KMeans #Librería para el procesamiento de clusters

np.random.seed(7) #Generamos un número pseudo aleatorio

x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2)) #Generamos 3 clusters x1, x2 y x3
x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
X = np.concatenate((x1,x2,x3),axis=0) #Los concatenamos

plt.plot(X[:,0],X[:,1],'k.') #Se formaizan y se imprimen
plt.show()
