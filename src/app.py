from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import funcoes

root = Tk()
root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (root_width, root_height))

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid(row=1)

btn = Button(root, text='abrir image', command=open_img).grid(row=0, column=0)

root.mainloop()


#arquivo = filedialog.askopenfile()
#cv.imread(arquivo.name)

#root = tk.Tk()

#


#root.mainloop()