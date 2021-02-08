from tkinter import*
from tkinter.filedialog import*

def func_open():
  fileName=askopenfilename(parent=window,filetypes=(("Gif file","*gif"),("All file","*.*")))
  photo=PhotoImage(file=fileName)
  plable.configure(image=photo); plable.image=photo

def fuct_exit():
  window.quit()
  window.destroy()

window=Tk(); window.geometry('800x500')
window.title("Python File manager")

photo=PhotoImage()
plable=Label(window,image=photo)
plable.pack(expand=1,anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open File",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="Exit Program",command=fuct_exit)

window.mainloop()