from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from lib import * 






def open_file_selector():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img(component):
    x = open_file_selector()
    img = Image.open(x)
    img = img.resize((500, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    imagem_original = Label(root, image=img)
    imagem_original.image= img
    imagem_original.place(in_=component)
  


##Seetings Main Window
root = Tk()
root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (root_width, root_height))

#Setting Main Menu
menu_bar = Menu(root)
filemenu = Menu(menu_bar, tearoff=0)
filemenu.add_command(label="Abrir Imagem", command=lambda: open_img(frame1))
menu_bar.add_cascade(label="File", menu=filemenu)

#Settings Components
label1= Label(root,text='Imagem Original')
label1.grid(row=16,column=0)
frame1 = Frame(root, bg="#FFFFFF", height=355, width=505, borderwidth=3)
frame1.grid(row=17, column=0, sticky=W, pady=7, padx=7)

label2= Label(root,text='Imagem Quantizada')
label2.grid(row=16,column=5)
frame2 = Frame(root, bg="#FFFFFF", height=355, width=505, borderwidth=3)
frame2.grid(row=17, column=5, sticky=W, pady=7, padx=7)



root.config(menu=menu_bar)
root.mainloop()

