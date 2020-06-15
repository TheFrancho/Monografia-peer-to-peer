#Programa que implementa el algoritmo k-means en un conjunto de datos separados incoloros
import numpy as np #Liberia para el cálculo mátemático
import matplotlib.pyplot as plt #Libería para el procesamiento matemático
from sklearn.cluster import KMeans #Librería para la implementación del algoritmo k-means

np.random.seed(7) #Generamos un números pseudo aleatorio

x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2)) #Generamos los 3 clusters de datos x1, x2 y x3
x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
X = np.concatenate((x1,x2,x3),axis=0) #Los concatenamos

n = 3 #Definimos en n el número de clusters a procesar
k_means = KMeans(n_clusters=n) #Se crea el objeto k_means con los n clusters
k_means.fit(X) #Formalizamos el k_means
centroides = k_means.cluster_centers_ #Creamos los centroides
etiquetas = k_means.labels_ #Y las etiquetas


plt.plot(X[etiquetas==0,0],X[etiquetas==0,1],'r.', label='cluster 1') #Mostramos cada uno de los clusters de un color rgb
plt.plot(X[etiquetas==1,0],X[etiquetas==1,1],'b.', label='cluster 2')
plt.plot(X[etiquetas==2,0],X[etiquetas==2,1],'g.', label='cluster 3')

plt.plot(centroides[:,0],centroides[:,1],'mo',markersize=8, label='centroides') #Generamos la plantilla a imprimir

plt.legend(loc='best')#Posiciona la leyenda de centroides y etiquetas en el mejor lugar posible
plt.show() #Muestra gráficamente todo
