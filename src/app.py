from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from lib import *


root = Tk()
root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (root_width, root_height))

def open_file_selector():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img():
    x = open_file_selector()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    imagem_original = Label(root, image=img)
    imagem_original.image= img
    imagem_original.place(in_=root,relx=0.16, rely=0.25, anchor=N)
  

button_open_img = Button(root, 
             text='Abrir Imagem', 
             width=10,
             height=5,
             font=14,
             command=open_img
             )

button_open_img.place(relx=0.05, rely=0.05, anchor=N)



root.mainloop()

