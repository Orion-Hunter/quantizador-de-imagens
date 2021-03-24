import numpy as np
import math

def quantizador(imagem, num_escala):#retorna a imagem quantizada
    ## Quantização ##
    # 255 / 31 = 8,22...
    # Assim, teremos uma imagem com 8 tons de cinza. A conta é feita desta forma para descartar a parte decimal dos números e alterar o vetor para que possua apenas 8 valores possíveis.
    n = num_escala #numero de escalas de cinza
    r = math.floor(255/n)
    img = np.uint8(imagem / r) * r #uint8 = integer (0 to 255).
    return img
