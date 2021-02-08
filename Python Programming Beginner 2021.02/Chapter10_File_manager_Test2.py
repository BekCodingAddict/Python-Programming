from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import*

def func_open():
  fileName=askopenfilename(parent=window,filetypes=(("Gif File","*.gif"),("All Files","*.*")))
  photo=PhotoImage(file=fileName)
  plable.configure(image=photo); plable.image=photo
  return photo
def func_exit():
  window.quit()
  window.destroy()



def func_zoom():
  num=askinteger("Enter the number","Enter the zoom degree:", minvalue=2,maxvalue=5)
  if num==2:
    photo=photo.zoom(x=850,y=550)
    plable.configure(image=photo); plable.image=photo
  elif num==3:
    photo=photo.zoom(x=900,y=600)
  elif num==4:
    photo=photo.zoom(x=1000,y=700)
  elif num==5:
    photo=photo.zoom(x=1200,y=900)


def func_subsample():
  num2=askinteger("Enter the number","Enter the subsample degree:",minvalue=2,maxvalue=5)
  if num2==2:
    photo.subsample(x=750,y=450)
  elif num2==3:
    photo.subsample(x=700,y=400)
  elif num2==4:
    photo.subsample(x=600,y=300)
  elif num2==5:
    photo.subsample(x=500,y=350)


  
window=Tk();window.geometry('800x500')
window.title('Python File manager')

photo=PhotoImage()
plable=Label(window,image=photo)
plable.pack(expand=1,anchor=CENTER)

mainMenu=Menu(window)
window.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_cascade(label="Open File",command=func_open)
fileMenu.add_separator()
fileMenu.add_cascade(label="Zoom",command=func_zoom)
fileMenu.add_separator()
fileMenu.add_cascade(label="Wide",command=func_subsample)
fileMenu.add_separator()
fileMenu.add_cascade(label="Exit Program",command=func_exit)
window.mainloop()