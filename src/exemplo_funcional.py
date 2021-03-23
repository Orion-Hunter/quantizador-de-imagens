#ex1 - para colorida
# Importing Image module from PIL package  
from PIL import Image  
import PIL  
  
# creating a image object (main image)  
im1 = Image.open(r"D:/lena.jpg")  
  
# quantize a image  
im1 = im1.quantize(100)
  
# to show specified image  
im1.show()  
#----------------------------------------------------------------------------------------

#ex2 - para preto e branco
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math

# Função: imread ( nome da imagem, [1=cor, 0=grayscape, -1=alpha])
# Cada coluna da imagem é armazenada em um subvetor, onde cada coluna é uma posição
img = cv2.imread('D:/lena.jpg', 0)
cv2.imshow('Original',img)

## Amostragem ##
# Reduzindo a imagem #
# Seleciona uma em cada 2 colunas, e de cada coluna uma a cada duas linhas
n = 2
img_red = img[::n,::n]

# Aumentando a imagem #
# Os pixels da imagem atual serão duplucados no eixo x e y. Assim, a imagem volta a ter o tamanho original, mas a partir da imagem reduzida
# Função: np.repeat(matriz, vezes, eixo). O eixo 0 é a altura e 1 a largura.
m = 2
img_aum = np.repeat(img_red, m, axis=0)
img_aum = np.repeat(img_aum, m, axis=1)

## Quantização ##
# 255 / 31 = 8,22...
# Assim, teremos uma imagem com 8 tons de cinza. A conta é feita desta forma para descartar a parte decimal dos números e alterar o vetor para que possua apenas 8 valores possíveis.
n = 4 #numero de escalas de cinza
r = math.floor(255/n)
img = np.uint8(img / r) * r #uint8 = integer (0 to 255).

# Salvar imagem no disco #
#cv2.imwrite('C:/Diretório', img_aum)

# Mostra uma imagem
# Função: cv.imshow(nome da janela, matriz)
cv2.imshow('Quantizada',img)
#cv2.imshow('reduzida',img_red)
#cv2.imshow('aumentada',img_aum)

# Funções para o funcionamento correto do python no Windows.
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------------------

#ex3 - para img preto e branco usando algoritmo de clusterização
#esse não consegui instalar a biblioteca T_T
#resto do codigo ta aqui: https://www.youtube.com/watch?v=O0suOccKLbs

import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

n_colors = 2
image_raw = io.imread('D:/lena.jpg')
image = np.array(image_raw, dtype=np.float64)/255
h,w,d = image.shape
image_array = np.reshape(image,(h*w, d))

plt.figure(1)
plt.clf()
plt.axis('off')
plt.title('Img Original')
plt.imshow(image)