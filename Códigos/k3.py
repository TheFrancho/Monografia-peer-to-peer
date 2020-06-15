#Programa que proccesa 10 clusters de numeros del 0 al 9 y los acopla
import numpy as np #Liberia para calculo matemático
import matplotlib.pyplot as plt #Libreria para graficamiento matemático
from sklearn.cluster import KMeans #Libreria para manejar los clusters k-means
from sklearn.datasets import load_digits#ligreria para la carga de los clusters en forma de numeros

np.random.seed(7) #Instancia de un numero pseudo aleatorio

x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2)) #Se generan 3 rangos aleatorios x1, x2 y x3
x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
X = np.concatenate((x1,x2,x3),axis=0) #Se concatenan los 3 rangos

n = 10 #Generamos 10 clusters, uno para cada numero del 0 al 9
k_means = KMeans(n_clusters=n) #Generamos la variable k_means como un objeto Kmeans de n clusters
k_means.fit(X)#Le damos forma a la variable

digits = load_digits() #guarda una serie de digitos a ordenar
data = digits.data
data = 255-data
np.random.seed(1)
kmeans = KMeans(n_clusters=n,init='random') #iniciamos el algoritmo con los clusters y una semilla random
kmeans.fit(data) #le damos forma a kmeans
Z = kmeans.predict(data)


for i in range(0,n): #Imrpimimos en consola y pantalla cada uno de los clusters

    fila = np.where(Z==i)[0] # filas en Z donde están las imagenes de cada cluster
    num = fila.shape[0]      # numero imagenes de cada cluster
    r = np.floor(num/10.)    # numero de filas menos 1 en figura de salida

    print("cluster "+str(i))
    print(str(num)+" elementos")

    plt.figure(figsize=(10,10))
    for k in range(0, num):
        plt.subplot(r+1, 10, k+1)
        imagen = data[fila[k], ]
        imagen = imagen.reshape(8, 8)
        plt.imshow(imagen, cmap=plt.cm.gray)
        plt.axis('off')
    plt.show()
