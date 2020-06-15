#Programa que busca y abre una imagen en formato png
import numpy as np #Libreria para el calculo matemático
import matplotlib.pyplot as plt #Libreria para el graficamiento matemático
from PIL import Image #Libreria para tratar imagenes png y jpg


I = Image.open("tienda.jpg") #Se abre la imagen tienda.png en la misma carpeta donde se guarde el programa
I1 = np.asarray(I,dtype=np.float32)/255 #convertimos la imagen en un arreglo lógico
plt.figure(figsize=(12,12)) #Creamos la figura donde se va a mostrar la imagen
plt.imshow(I1)  #Mostramos el array en plt
plt.axis('off') 
plt.show()
