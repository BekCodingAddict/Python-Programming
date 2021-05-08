from tkinter import*
from tkinter.filedialog import*

window=Tk(); window.geometry('800x500') 
label1=Label(window,text="The file name that you choose")
label1.pack()

##filename=askopenfilename(parent=window,filetypes=(("GIF File","*.gif"),("All file","*.*")))
# label1.configure(text=str(filename))

saveFl=asksaveasfile(parent=window,mode="w",defaultextension=".jpg",filetypes=(("JPG FILE","*jpg;*.jpeg"),("all file","*.*")))
label1.configure(text=saveFl); saveFl.close()
window.mainloop()