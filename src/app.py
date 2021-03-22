import tkinter as tk
from tkinter import filedialog

arquivo = filedialog.askopenfile()
for line in arquivo:
    print(line)

root = tk.Tk()

root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (root_width, root_height))


root.mainloop()