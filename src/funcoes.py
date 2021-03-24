# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math

def quantizador(imagem, num_escala):#retorna a imagem quantizada
    ## Quantização ##
    # 255 / 31 = 8,22...
    # Assim, teremos uma imagem com 8 tons de cinza. A conta é feita desta forma para descartar a parte decimal dos números e alterar o vetor para que possua apenas 8 valores possíveis.
    n = num_escala #numero de escalas de cinza
    r = math.floor(255/n)
    img = np.uint8(imagem / r) * r #uint8 = integer (0 to 255).
    return img

def amostragem(imagem, escala_reducao):#retorna a imagem reduzida(amostragem)
    ## Amostragem ##
    # Reduzindo a imagem #
    # Seleciona uma em cada 2 colunas, e de cada coluna uma a cada duas linhas
    n = escala_reducao
    img_red = imagem[::n,::n]
    return img_red

def gera_histograma(img):
    # http://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html#gsc.tab=0
    # calcHist(images, channels, mask, histSize, ranges)
    # histSize: representa BIN count (pode agrupar intervalo de pixels)
    # ranges: ex: [0, 256]
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    #plt.plot(hist)
    #plt.show()
    return hist