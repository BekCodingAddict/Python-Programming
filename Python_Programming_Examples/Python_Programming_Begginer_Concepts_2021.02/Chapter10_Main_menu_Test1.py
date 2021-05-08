from tkinter import*
from tkinter import messagebox

window=Tk(); window.geometry('800x500')
mainMenu=Menu(window); window.config(menu=mainMenu,background="yellow")

def func_open():
  messagebox.showinfo("Info","Open Menu is choosed!")

def func_exit():
  window.quit()
  window.destroy()
  messagebox.showwarning("Info","Open Menu is choosed!")

fileMenu=Menu(mainMenu);
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_command(label="File Open",command=func_open) 
fileMenu.add_separator(background="red")
fileMenu.add_command(label="Exit",command=func_exit)
window.mainloop()
