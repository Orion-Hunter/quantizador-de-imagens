from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import Tk, Label, Menu, Button, Frame, W
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from lib import *
from cv2 import cv2
import numpy as np
import math
import tkinter as tk

from tkinter.ttk import *

import matplotlib

#configura a plotagem do matlab para a janela Tkinter
matplotlib.use("TkAgg")


figure = Figure(figsize=(5, 4), dpi=100)
# gs = figure.add_gridspec(2,2)
plt1 = figure.add_subplot(1, 1, 1)


global path_copy, resolution
# resolution = 4


def set_resolution(event):
    resolution = int(resolution_component.get())
    print(resolution)
    resolution_component.delete(0, tk.END)
    quantize_image(resolution)


def quantizador(imagem, num_escala):  # retorna a imagem quantizada
    ## Quantização ##
    # 255 / 31 = 8,22...
    # Assim, teremos uma imagem com 8 tons de cinza. A conta é feita desta forma para descartar a parte decimal dos números e alterar o vetor para que possua apenas 8 valores possíveis.
    n = num_escala  # numero de escalas de cinza
    r = math.floor(255/n)
    img = np.uint8(imagem / r) * r  # uint8 = integer (0 to 255).
    return img


def gera_histograma(img): #retorna o histograma
    # http://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html#gsc.tab=0
    # calcHist(images, channels, mask, histSize, ranges)
    # histSize: representa BIN count (pode agrupar intervalo de pixels)
    # ranges: ex: [0, 256]
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist


def select_image(): #abre o explore para selecionar a imagem(colorida) e abre ela(cinza) na janela junto com o histograma dela
    global panelA, path
    path = filedialog.askopenfilename(title='open')

    if len(path) > 0:
        image = cv2.imread(path)

        porcentagem = 0.5
        largura = int(image.shape[0]*porcentagem)
        altura = int(image.shape[1]*porcentagem)
        dim = (altura, largura)

        img_dim = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(img_dim, cv2.COLOR_BGR2GRAY)

        image = Image.fromarray(gray)

        image = ImageTk.PhotoImage(image)

        if panelA is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.grid(row=0, column=0)
            valor = gera_histograma(gray)
            plt1.plot(valor)
            canvas = FigureCanvasTkAgg(figure, root)
            canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)
        else:
            panelA.configure(image=image)
            panelA.image = image


def quantize_image(resol):#pega o valor do campo e seta para quantizar a imagem e mostrar ela na janela junto com o histograma
    global panelB
    print(resol)
    if resol is not None:
        image = cv2.imread(path)
        figure2 = Figure(figsize=(5, 4), dpi=100)
        plt2 = figure2.add_subplot(1, 1, 1)

        porcentagem = 0.5
        largura = int(image.shape[0]*porcentagem)
        altura = int(image.shape[1]*porcentagem)
        dim = (altura, largura)
        img_dim = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(img_dim, cv2.COLOR_BGR2GRAY)
        quantized_img = quantizador(gray, resol)

        img = Image.fromarray(quantized_img)
        img_jpg = ImageTk.PhotoImage(img)
        
        if panelB is None:
            panelB = Label(image=img_jpg)
            panelB.image = img_jpg
            panelB.grid(row=0, column=1, padx=10, pady=10)
            valor2 = gera_histograma(quantized_img)
            plt2.plot(valor2)
            canvas = FigureCanvasTkAgg(figure2, root)
            canvas.get_tk_widget().grid(row=1, column=1, padx=10, pady=10)
        else:
            panelB.configure(image=img_jpg)
            panelB.image = img_jpg
            valor2 = gera_histograma(quantized_img)
            plt2.plot(valor2)
            canvas = FigureCanvasTkAgg(figure2, root)
            canvas.get_tk_widget().grid(row=1, column=1, padx=10, pady=10)



# initialize the window toolkit along with the two image panels
root = Tk()
root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (root_width, root_height))


menu_bar = Menu(root)
filemenu = Menu(menu_bar, tearoff=0)
filemenu.add_command(label="Abrir Imagem", command=select_image)
menu_bar.add_cascade(label="File", menu=filemenu)

panelA = None
panelB = None

label = Label(root, text="Resolução do Quantizador: ")
label.place(x=root_width / 1.7, y=150)

resolution_component = Entry(root)
resolution_component.place(x=root_width / 1.7, y=170)
resolution_component.bind("<Return>", set_resolution)




root.config(menu=menu_bar)
root.mainloop()
