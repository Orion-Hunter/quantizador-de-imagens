def amostragem(imagem, escala_reducao):#retorna a imagem reduzida(amostragem)
    ## Amostragem ##
    # Reduzindo a imagem #
    # Seleciona uma em cada 2 colunas, e de cada coluna uma a cada duas linhas
    n = escala_reducao
    img_red = imagem[::n,::n]
    return img_red