import numpy as np #Liberia para el cálculo matemático
import matplotlib.pyplot as plt #Librería para el graficamiento matemático
from sklearn.cluster import KMeans #Librería para la implementación de los métodos de k-means
from PIL import Image #Libreria para el manejo de imágenes

np.random.seed(1) #Generamos un valor pseuso aleatorio

I = Image.open("tienda.jpg") #En la variable I se obtiene la imagen tienda.jpg
I1 = np.asarray(I,dtype=np.float32)/255 #Se obtiene el array de datos de tienda.jpg

w, h = I.size #Se generan las variables w y h como el tamaño de I
colors = I.getcolors(w * h) #Se obtienen los colores como la multiplicación del tamaño por si mismo
num_colores = len(colors) #Se obtiene la cantidad de colores según la longitud de la variable colors
num_pixels = w*h #El número de pixeles es el cuadrado del tamaño

print (u'Número de pixels  = ', num_pixels) #Imprimimos el numero de pixeles y de colores
print (u'Número de colores = ', num_colores)

R = I1[:,:,0] #Generamos una matriz RGB
G = I1[:,:,1]
B = I1[:,:,2]


XR = R.reshape((-1, 1)) #Damos un remodelado y lo ingresamos en XR, XG Y XB
XG = G.reshape((-1, 1))
XB = B.reshape((-1, 1))
X = np.concatenate((XR,XG,XB),axis=1) #Concatenamos los colores

n = 60 #Generamos la cantidad de clusters o colores a obtener, en este casos son 60
k_means = KMeans(n_clusters=n) #Se crea la variable k_means con los métodos de k_means y n clusters
k_means.fit(X) #Le damos forma a la variable k_means

m = XR.shape #A partir de esta linea, se genera el proceso de optimización de colores
for i in range(m[0]):
    XR[i] = centroides[etiquetas[i]][0]
    XG[i] = centroides[etiquetas[i]][1]
    XB[i] = centroides[etiquetas[i]][2]
XR.shape = R.shape
XG.shape = G.shape
XB.shape = B.shape
XR = XR[:, :, np.newaxis]
XG = XG[:, :, np.newaxis]
XB = XB[:, :, np.newaxis]

Y = np.concatenate((XR,XG,XB),axis=2)

plt.figure(figsize=(12,12))
plt.imshow(Y)
plt.axis('off')
plt.show()

print (u'Número de pixels  = ', num_pixels)
print (u'Número de colores = ', n)

Y1 = np.floor(Y*255)
Image.fromarray(Y1.astype(np.uint8)).save("tienda_comprimida.jpg")
