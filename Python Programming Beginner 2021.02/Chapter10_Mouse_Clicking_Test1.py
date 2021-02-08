from tkinter import*

def clickMouse(event):
  txt=""
  if event.num==1:
    txt+="The Left Button has clicked at("
  elif event.num==3:
    txt="The Right Button has clicked at ("

  txt+=str(event.y)+","+str(event.x)
  label1.configure(text=txt)

window=Tk(); window.geometry('800x500')
label1=Label(window,text="Here change")

window.bind("<Button>",clickMouse)
label1.pack(expand=1,anchor=CENTER); window.mainloop()