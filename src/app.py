from tkinter import Tk, Label, Menu, Button, Frame, W
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from lib import *
from cv2 import cv2
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

def gera_histograma(img):
    # http://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html#gsc.tab=0
    # calcHist(images, channels, mask, histSize, ranges)
    # histSize: representa BIN count (pode agrupar intervalo de pixels)
    # ranges: ex: [0, 256]
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    #plt.plot(hist)
    #plt.show()
    return hist

def select_image():
	# grab a reference to the image panels
	global panelA, panelB
	# open a file chooser dialog and allow the user to select an input
	# image
	path = filedialog.askopenfilename(title='open')

	# ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		edged = quantizador(gray, 4)
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		# convert the images to PIL format...
		image = Image.fromarray(gray)
		edged = Image.fromarray(edged)
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		edged = ImageTk.PhotoImage(edged)

		# if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
			# while the second panel will store the edge map
			panelB = Label(image=edged)
			panelB.image = edged
			panelB.pack(side="right", padx=10, pady=10)
		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=edged)
			panelA.image = image
			panelB.image = edged

# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Selecionar Imagem", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()

