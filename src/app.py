import tkinter as tk
from tkinter import filedialog
import cv2 as cv

arquivo = filedialog.askopenfile()
cv.imread(arquivo.name)

root = tk.Tk()

root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (root_width, root_height))


root.mainloop()